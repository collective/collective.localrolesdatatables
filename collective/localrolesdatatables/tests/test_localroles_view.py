import unittest2 as unittest
from collective.localrolesdatatables.tests import base


class TestCatalogLocalRolesView(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def setUp(self):
        super(TestCatalogLocalRolesView, self).setUp()
        from collective.localrolesdatatables import localroles_view
        self.view = localroles_view.CatalogLocalRolesView(self.folder,
                                                      self.layer['request'])
        #TODO: add localroles and add tests

    def test_roles(self):
        roles = self.view.roles()
        self.assertEquals(len(roles), 3)
        roleids = [r['id'] for r in roles]
        self.assertIn('Contributor', roleids)
        self.assertIn('Editor', roleids)
        self.assertIn('Reader', roleids)

    def test_localroles(self):
        lroles = self.view.localroles(self.portal)
        self.assertEqual(lroles, [])

    def test_filter_localroles(self):
        pass

    def test_buildQuery(self):
        query = self.view.buildQuery()
        self.assertIn('Language', query)
        self.assertIn('hasLocalRoles', query)
        self.assertIn('path', query)
        self.assertTrue(query['hasLocalRoles'])
        self.assertEqual(query['Language'], 'all')

    def test_role_settings_from_brains(self):
        brains = self.portal.portal_catalog()
        role_settings = self.view.role_settings_from_brains(brains)
        self.assertEqual(len(role_settings), 1)
        self.assertEqual(role_settings.values()[0]['type'], 'Folder')
        self.assertEqual(role_settings.keys()[0], brains[0].getURL())

    def test_role_settings(self):
        role_settings = self.view.role_settings()
        self.assertEqual(len(role_settings), 0)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
