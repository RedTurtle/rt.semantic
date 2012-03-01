# -*- coding: utf-8 -*-

from zope import schema
from zope.interface.declarations import alsoProvides

from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form
from z3c.form.interfaces import IEditForm, IDisplayForm

from rt.semantic import semanticMessageFactory as _


class ISemantic(form.Schema):
    """
    Semantic behavior interface
    """
    semantic = schema.Tuple(
        title=_("label_semantic", default=u"Semantic"),
        description=_("help_semantic", default=u""),
        required=False,
        value_type=schema.TextLine(),
        missing_value=(),
    )
    form.omitted('semantic')
    form.no_omit(IDisplayForm, 'semantic')
    form.no_omit(IEditForm, 'semantic')

alsoProvides(ISemantic, IFormFieldProvider)

