from zope.interface import alsoProvides
from zope import schema

from z3c.form.interfaces import IDisplayForm
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider


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

