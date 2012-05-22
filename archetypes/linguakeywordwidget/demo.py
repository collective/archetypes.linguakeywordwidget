""" demonstrates the use of archetypes.linguakeywordwidget """

from Products.Archetypes.atapi import LinesField
from Products.Archetypes.atapi import BaseSchema
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import BaseContent
from Products.Archetypes.atapi import registerType

from archetypes.linguakeywordwidget.config import PROJECTNAME
from archetypes.linguakeywordwidget.widget import LinguaKeywordWidget


schema = BaseSchema.copy() + Schema((

    LinesField(
            'subject',
            multiValued=1,
            accessor="Subject",
        widget=LinguaKeywordWidget()),

     ))


class RefBrowserDemo(BaseContent):
    """
    Demo from archetypes.linguakeywordwidget
    """
    content_icon = "document_icon.gif"
    schema = schema

registerType(RefBrowserDemo, PROJECTNAME)
