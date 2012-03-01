import unittest

from rt.semantic.tagger import tag


class TestPOSTagger(unittest.TestCase):

    def test_pos_tag(self):
        sentence = 'The quick brown fox jumps over the lazy dog'
        tagged = tag(sentence)
        self.assertEqual([('The', 'DT'), ('quick', 'NN'), ('brown', 'NN'),
                          ('fox', 'NN'), ('jumps', 'NNS'), ('over', 'IN'),
                          ('the', 'DT'), ('lazy', 'NN'), ('dog', 'NN')], tagged)

    def test_empty_text(self):
        self.assertEqual([], tag(''))
