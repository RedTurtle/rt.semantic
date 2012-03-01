from plone.directives import form


class IArticle(form.Schema):
    form.model('article.xml')
