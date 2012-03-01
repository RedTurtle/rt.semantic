import unittest
import nltk

from Products.CMFCore.utils import getToolByName

from rt.semantic.testing import\
    REDTURTLE_SEMANTIC_INTEGRATION_TESTING

from rt.semantic.tagtext import tag_this_text 

class TestPOSTagger(unittest.TestCase):

#    layer = REDTURTLE_SEMANTIC_INTEGRATION_TESTING

    the_sentence = 'The quick brown fox jumps over the lazy dog'

    def test_pos_tag(self):
        text = nltk.word_tokenize(self.the_sentence)
        tagged = tag_this_text(text)
        self.assertEqual([('The', 'DT'), ('quick', 'NN'), ('brown', 'NN'), 
                          ('fox', 'NN'), ('jumps', 'NNS'), ('over', 'IN'), 
                          ('the', 'DT'), ('lazy', 'NN'), ('dog', 'NN')], tagged)
        