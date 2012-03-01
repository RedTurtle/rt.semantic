
from zope.configuration import xmlconfig

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile


class RedturtleSemantic(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import rt.semantic
        xmlconfig.file('configure.zcml',
                       rt.semantic,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'rt.semantic:default')


REDTURTLE_SEMANTIC_FIXTURE = RedturtleSemantic()
REDTURTLE_SEMANTIC_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(REDTURTLE_SEMANTIC_FIXTURE, ),
                       name="RedturtleSemantic:Integration")
REDTURTLE_SEMANTIC_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(REDTURTLE_SEMANTIC_FIXTURE, ),
                       name="RedturtleSemantic:Functional")

