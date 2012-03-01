import unittest

from plone.behavior.interfaces import IBehavior
from zope.component import getUtilitiesFor

from rt.semantic.testing import REDTURTLE_SEMANTIC_INTEGRATION_TESTING

class TestBehavior(unittest.TestCase):

    layer = REDTURTLE_SEMANTIC_INTEGRATION_TESTING

    def test_behavior_registered(self):
        self.assertTrue(u'rt.semantic.behavior.ISemantic' in
                        [name for name, interface in list(getUtilitiesFor(IBehavior))])