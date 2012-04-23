from zope import component
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish
import pprint

import logging
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.workflow.browser.sharing import STICKY
logger = logging.getLogger('collective.localrolesdatatables')

class LocalRolesView(BrowserView):
    """View to display localroles"""

    STICKY = STICKY

    def roles(self):
        """Return list of roles"""
        sharing_view = component.getMultiAdapter((self.context, self.request),
                                                 name="sharing")
        return sharing_view.roles()

    def localroles(self, context, results=None):
        if results is None:
            results = {}

        sharing_view = component.getMultiAdapter((context, self.request),
                                                 name="sharing")
        role_settings = sharing_view.role_settings() #a list of dict

        if len(role_settings) == 1:
            activated = role_settings[0]['roles'].values()
            if True in activated:
                results[context.absolute_url()] = role_settings

        if IFolderish.providedBy(context):
            for id, item in context.contentItems():
                self.localroles(item, results)

        return results

    def role_settings(self):
        """recursive call"""
        results={}
        return self.localroles(self.context, results)

    __call__ = ViewPageTemplateFile('localroles_view.pt')
