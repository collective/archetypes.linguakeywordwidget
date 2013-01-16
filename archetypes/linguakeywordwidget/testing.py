from plone.app.testing import *
import archetypes.linguakeywordwidget
profile = 'archetypes.linguakeywordwidget:default'


FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=archetypes.linguakeywordwidget,
                                additional_z2_products=[],
                                gs_profile_id=profile,
                                name="archetypes.linguakeywordwidget:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="archetypes.linguakeywordwidget:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="archetypes.linguakeywordwidget:Functional")

