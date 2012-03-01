from rwproperty import getproperty, setproperty
from zope.interface import alsoProvides
from zope import schema

from z3c.form.interfaces import IDisplayForm
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
#from plone.behavior.interfaces import ISchemaAwareFactory
from plone.behavior.annotation import AnnotationStorage


class ISemantic(form.Schema):
    """
    Marker/Form interface for Semantic behavior
    """
    tags = schema.Tuple(title = u'Semantic tags',
                        description = u'Semantic keyword field',
                        value_type = schema.TextLine(),
                        required = False,
                        missing_value = ())

    form.omitted('tags')
    form.no_omit(IDisplayForm, 'tags')

alsoProvides(ISemantic, IFormFieldProvider)


class Semantic(AnnotationStorage):
    """
    Automatically calculate semantic tags and store them in annotation.
    """
    def __init__(self, context):
        self.context = context

    @getproperty
    def tags(self):
       return set(self.context.tags)

    @setproperty
    def tags(self, value):
        semantics = ()
        setattr(self.context, 'tags', semantics)
