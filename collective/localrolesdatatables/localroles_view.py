from time import time
from zope import component
from zope import interface
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish
import pprint

from plone.indexer import indexer

import logging
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.workflow.browser.sharing import STICKY
logger = logging.getLogger('collective.localrolesdatatables')

@indexer(interface.Interface)
def hasLocalRoles(obj):
    if hasattr(obj, '__ac_local_roles__'):
        roles = getattr(obj, '__ac_local_roles__')
        return len(roles)>1

class CatalogLocalRolesView(BrowserView):
    """View to display localroles"""

    STICKY = STICKY

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self._catalog = None
        self.request.set('disable_plone.leftcolumn',1)
        self.request.set('disable_plone.rightcolumn',1)


    def roles(self):
        """Return list of roles"""
        sharing_view = component.getMultiAdapter((self.context, self.request),
                                                 name="sharing")
        return sharing_view.roles()

    def localroles(self, context):
        sharing_view = component.getMultiAdapter((context, self.request),
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

    def role_settings(self):
        """extract role_settings mapping for every contents"""
        t1 = time()

        results={}
        query = {'Language':'all', 'hasLocalRoles':True}
        brains = self.catalog()(**query)
        logger.info(len(brains))

        for brain in brains:
            ob = brain.getObject()
            results[ob.absolute_url()] = {'localroles': self.localroles(ob),
                                          'title': ob.Title()}

        t2 = time()
        logger.info(t2-t1)

        return results

    def catalog(self):
        if self._catalog is None:
            self._catalog = getToolByName(self.context, 'portal_catalog')
        return self._catalog

    __call__ = ViewPageTemplateFile('localroles_view.pt')



class ObjectLocalRolesView(CatalogLocalRolesView):
    """View to display localroles"""

    def localroles(self, context, results=None):
        """Change the way localroles are computed"""
        if results is None:
            results = {}

        sharing_view = component.getMultiAdapter((context, self.request),
                                                 name="sharing")
        role_settings = sharing_view.role_settings() #a list of dict
        localroles = self.filter_localroles(role_settings)

        if localroles:
            results[context.absolute_url()] = {'localroles':localroles,
                                               'title': context.Title()}

        if IFolderish.providedBy(context):
            for id, item in context.contentItems():
                self.localroles(item, results)

    def role_settings(self):
        """extract role_settings mapping for every contents"""
        t1 = time()
        results={}
        self.localroles(self.context, results)
        t2 = time()
        logger.info(len(results))
        logger.info(t2-t1)
        return results