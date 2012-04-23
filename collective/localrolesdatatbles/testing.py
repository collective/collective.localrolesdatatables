from plone.testing import z2

from plone.app.testing import *
import collective.localrolesdatatbles

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=collective.localrolesdatatbles,
                                additional_z2_products=[],
                                gs_profile_id='collective.localrolesdatatbles:default',
                                name="collective.localrolesdatatbles:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.localrolesdatatbles:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.localrolesdatatbles:Functional")

