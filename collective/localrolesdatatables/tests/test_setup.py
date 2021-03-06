import unittest2 as unittest
from collective.localrolesdatatables.tests import base


class TestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_catalog(self):
        catalog = self.portal.portal_catalog
        self.assertTrue('hasLocalRoles' in catalog.indexes())

    def test_datatables_installed(self):
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled('collective.js.datatables'))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
