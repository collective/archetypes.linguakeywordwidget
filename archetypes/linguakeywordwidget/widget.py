from types import StringType

from Acquisition import aq_base, aq_inner
from AccessControl import ClassSecurityInfo

from Products.Archetypes.utils import shasattr
from Products.Archetypes.Registry import registerWidget, registerPropertyType
from Products.Archetypes.Widget import KeywordWidget


class LinguaKeywordWidget(KeywordWidget):
    _properties = KeywordWidget._properties.copy()
    _properties.update({
        'macro': "linguakeyword",
#        'size': '5',
#        'helper_js': ('linguakeyword.js',),
#        'vocab_source': 'portal_catalog',
        })

    security = ClassSecurityInfo()
    security.declarePublic('process_form')

    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False, validating=True):
        """process keywords from form where this widget has a list of
        available keywords and any new ones"""

        first = super(LinguaKeywordWidget, self).process_form(instance,
                                      field,
                                      form,
                                      empty_marker=empty_marker,
                                      emptyReturnsMarker=emptyReturnsMarker,
                                      validating=validating)

        if not first and emptyReturnsMarker:
            return empty_marker

        if first is empty_marker:
            return empty_marker

        language = instance.Language()
        keywords = first[0]
        linguakeywords = []

        for keyword in keywords:
            if keyword.startswith('%s-' % language):
                linguakeywords.append(keyword)
            else:
                linguakeywords.append('%s-%s' % (language, keyword))

        return linguakeywords, first[1]

registerWidget(LinguaKeywordWidget,
               title='LinguaKeyword',
               description=('MultiLanguage keyword widget'),
               used_for=('Products.Archetypes.Field.LinesField',)
               )
