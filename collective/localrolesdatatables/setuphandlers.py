from Products.CMFCore.utils import getToolByName


def setupVarious(context):
    marker = 'collective.localrolesdatatables.marker.txt'
    if context.readDataFile(marker) is None:
        # Not your add-on
        return
    portal = context.getSite()
    catalog = getToolByName(portal, 'portal_catalog')
    catalog.reindexIndex('hasLocalRoles', portal.REQUEST)
