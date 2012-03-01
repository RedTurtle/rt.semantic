import nltk

nltk.download('maxent_treebank_pos_tagger')


def initialize(context):
    from upgrades import config
    config.register_profile()
    config.scan()
