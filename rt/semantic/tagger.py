import nltk

def tag(text):
    return nltk.pos_tag(nltk.word_tokenize(text))