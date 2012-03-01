
from zope.schema import getFieldsInOrder
from zope.schema.interfaces import IText
from plone.dexterity.utils import iterSchemata
from rt.semantic.tagger import tag, extract_keywords

def set_semantic_data(obj, event):
    text = []
    for schema in iterSchemata(obj):
        fields = getFieldsInOrder(schema)
        for field in fields:
            if IText.providedBy(field):
                text.append(field.get(obj))
    full_text = "\n".join(text)
    pos_tags = tag(full_text)
    return extract_keywords(pos_tags)

