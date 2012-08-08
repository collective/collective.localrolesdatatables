from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-collective.localrolesdatatables:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)

#    catalog = getToolByName(context, 'portal_catalog')
#    catalog.reindexIndex('hasLocalRoles', context.REQUEST)
