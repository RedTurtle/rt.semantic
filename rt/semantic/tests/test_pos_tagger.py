import unittest

from Products.CMFCore.utils import getToolByName

from rt.semantic.testing import\
    REDTURTLE_SEMANTIC_INTEGRATION_TESTING

from rt.semantic.tagger import tag

class TestPOSTagger(unittest.TestCase):

#    layer = REDTURTLE_SEMANTIC_INTEGRATION_TESTING

    the_sentence = 'The quick brown fox jumps over the lazy dog'

    def test_pos_tag(self):
        tagged = tag(self.the_sentence)
        self.assertEqual([('The', 'DT'), ('quick', 'NN'), ('brown', 'NN'), 
                          ('fox', 'NN'), ('jumps', 'NNS'), ('over', 'IN'), 
                          ('the', 'DT'), ('lazy', 'NN'), ('dog', 'NN')], tagged)
        