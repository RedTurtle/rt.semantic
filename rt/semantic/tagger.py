import nltk


def tag(text):
    """
    Tokenizes and POS-tags text.
    """
    return nltk.pos_tag(nltk.word_tokenize(text))
