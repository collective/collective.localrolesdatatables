from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-collective.localrolesdatatables:default'


def upgrade_1000_to_1001(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(PROFILE,
                                   'controlpanel',
                                   run_dependencies=False,
                                   purge_old=False)
    setup.runImportStepFromProfile(PROFILE,
                                   'collective.localrolesdatatables',
                                   run_dependencies=False,
                                   purge_old=False)

    qi = getToolByName(context, 'portal_quickinstaller')
    if not qi.isProductInstalled('collective.js.datatables'):
        qi.installProduct('collective.js.datatables')
