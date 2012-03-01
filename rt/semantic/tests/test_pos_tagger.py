import unittest
from os.path import dirname, join

from rt.semantic.tagger import tag, extract_keywords
import rt.semantic.tests

class TestPOSTagger(unittest.TestCase):

    def setUp(self):
        path = join(dirname(rt.semantic.tests.__file__), 'data', 'alicereview.txt')
        with open(path,'r') as fd:
            self.alicetext = fd.read()

    def test_pos_tag(self):
        sentence = 'The quick brown fox jumps over the lazy dog'
        tagged = tag(sentence)
        self.assertEqual([('The', 'DT'), ('quick', 'NN'), ('brown', 'NN'),
                          ('fox', 'NN'), ('jumps', 'NNS'), ('over', 'IN'),
                          ('the', 'DT'), ('lazy', 'NN'), ('dog', 'NN')], tagged)

    def test_empty_text(self):
        self.assertEqual([], tag(''))

    def test_extract_keywords(self):
        pos_tags = tag(self.alicetext)
        most_important = extract_keywords(pos_tags)
        self.assertEqual(most_important,
                         ['door', 'table', 'house', 'notices', 'time', 'baby',
                          'day', 'finds', 'head', 'mushroom'])

