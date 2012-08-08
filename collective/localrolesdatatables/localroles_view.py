from time import time
from zope import component
from zope.component import getMultiAdapter
from zope import interface
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish

from plone.indexer import indexer

import logging
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.workflow.browser.sharing import STICKY
logger = logging.getLogger('collective.localrolesdatatables')


@indexer(interface.Interface)
def hasLocalRoles(obj):
    if hasattr(obj, '__ac_local_roles__'):
        roles = getattr(obj, '__ac_local_roles__')
        return len(roles) > 1


class CatalogLocalRolesView(BrowserView):
    """View to display localroles"""

    STICKY = STICKY
    index = ViewPageTemplateFile('localroles_view.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal_catalog = None
        self.portal_state = None
        self.portal_url = None
        self.sharing_view = None

    def __call__(self):
        self.update()
        return self.index()

    def update(self):
        self.request.set('disable_plone.leftcolumn', 1)
        self.request.set('disable_plone.rightcolumn', 1)
        if self.portal_state is None:
            self.portal_state = getMultiAdapter((self.context, self.request),
                                                 name="plone_portal_state")
        if self.portal_url is None:
            self.portal_url = self.portal_state.portal_url
        if self.sharing_view is None:
            self.sharing_view = getMultiAdapter((self.context, self.request),
                                                 name="sharing")
        if self.portal_catalog is None:
            self.portal_catalog = getToolByName(self.context, 'portal_catalog')

    def roles(self):
        """Return list of roles"""
        return self.sharing_view.roles()

    def localroles(self, context):
        sharing_view = getMultiAdapter((context, self.request),
                                      name="sharing")
        role_settings = sharing_view.role_settings()

        return self.filter_localroles(role_settings)

    def filter_localroles(self, role_settings):
        """return subset of real localroles"""
        localroles = []

        for role_setting in role_settings:
            activated = role_setting['roles'].values()
            if True in activated:
                localroles.append(role_setting)

        return localroles

    def buildQuery(self):
        context_path = '/'.join(self.context.getPhysicalPath())
        query = {'Language': 'all',
                 'hasLocalRoles': True,
                 'path': context_path}
        return query

    def role_settings(self):
        """extract role_settings mapping for every contents"""
        t1 = time()

        query = self.buildQuery()
        brains = self.portal_catalog(**query)
        logger.info(len(brains))

        results = self.role_settings_from_brains(brains)

        t2 = time()
        logger.info(t2 - t1)

        return results

    def role_settings_from_brains(self, brains):
        results = {}
        for brain in brains:
            ob = brain.getObject()
            results[ob.absolute_url()] = {'localroles': self.localroles(ob),
                                          'title': ob.Title(),
                                          'type': ob.portal_type}
        return results


class ObjectLocalRolesView(CatalogLocalRolesView):
    """View to display localroles"""

    def localroles(self, context, results=None):
        """Change the way localroles are computed"""
        if results is None:
            results = {}

        role_settings = self.sharing_view.role_settings()  # a list of dict
        localroles = self.filter_localroles(role_settings)

        if localroles:
            results[context.absolute_url()] = {'localroles': localroles,
                                               'title': context.Title(),
                                               'type': context.portal_type}

        if IFolderish.providedBy(context):
            for iid, item in context.contentItems():  # @UnusedVariable
                self.localroles(item, results)

    def role_settings(self):
        """extract role_settings mapping for every contents"""
        t1 = time()
        results = {}
        self.localroles(self.context, results)
        t2 = time()
        logger.info(len(results))
        logger.info(t2 - t1)
        return results
