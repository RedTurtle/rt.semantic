import nltk
nltk.download('maxent_treebank_pos_tagger')

def tag(text):
    """
    Tokenizes and POS-tags text.
    """
    return nltk.pos_tag(nltk.word_tokenize(text))
