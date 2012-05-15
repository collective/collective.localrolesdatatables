from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE


class Fixture(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.localrolesdatatables
        import collective.js.datatables
        # Load ZCML
        self.loadZCML(package=collective.localrolesdatatables)
        self.loadZCML(package=collective.js.datatables)

        # Install product and call its initialize() function
        z2.installProduct(app, 'collective.localrolesdatatables')
        z2.installProduct(app, 'collective.js.datatables')

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'collective.localrolesdatatables:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'collective.localrolesdatatables')
        z2.uninstallProduct(app, 'collective.js.datatables')

FIXTURE = Fixture()


#FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
#                    zcml_package=collective.localrolesdatatables,
#                    additional_z2_products=[],
#                    gs_profile_id='collective.localrolesdatatables:default',
#                    name="collective.localrolesdatatables:FIXTURE")
INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.localrolesdatatables:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.localrolesdatatables:Functional")
