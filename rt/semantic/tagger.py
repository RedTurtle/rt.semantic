
import nltk
nltk.download('maxent_treebank_pos_tagger')


def tag(text):
    """
    Tokenizes and POS-tags text.
    """
    return nltk.pos_tag(nltk.word_tokenize(text))


def extract_keywords(pos_tags, count=10):
    """
    Filter for nouns and return the most frequent ones
    """
    noun_types = ['NN', 'NNS', 'NP']
    nouns = [noun for noun, tag in pos_tags if tag in noun_types]
    freq = nltk.FreqDist(nouns)
    return freq.keys()[:count]

