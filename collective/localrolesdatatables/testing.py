from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import collective.localrolesdatatables

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                    zcml_package=collective.localrolesdatatables,
                    additional_z2_products=[],
                    gs_profile_id='collective.localrolesdatatables:default',
                    name="collective.localrolesdatatables:FIXTURE")
INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.localrolesdatatables:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.localrolesdatatables:Functional")
