import nltk


def tag(text):
    """
    Tokenizes and POS-tags text.
    """
    return nltk.pos_tag(nltk.word_tokenize(text))

def extract_nouns(text):
    tags = tag(text)
    import pdb; pdb.set_trace()
