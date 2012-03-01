from zope.i18nmessageid import MessageFactory
import nltk


nltk.download('maxent_treebank_pos_tagger')
semanticMessageFactory = MessageFactory('rt.semantic')
