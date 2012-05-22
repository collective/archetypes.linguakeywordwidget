from Products.CMFCore.utils import ContentInit
from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore.permissions import AddPortalContent
from archetypes.linguakeywordwidget.config import PROJECTNAME, WITH_SAMPLE_TYPES
from archetypes.linguakeywordwidget.widget import LinguaKeywordWidget


def initialize(context):
    if WITH_SAMPLE_TYPES:
        import demo
        demo   # pyflakes
        content_types, constructors, ftis = process_types(
            listTypes(PROJECTNAME),
            PROJECTNAME)

        ContentInit(
            PROJECTNAME + ' Content',
            content_types=content_types,
            permission=AddPortalContent,
            extra_constructors=constructors,
            ).initialize(context)

if WITH_SAMPLE_TYPES:
    # setup sample types
    from Products.GenericSetup import EXTENSION, profile_registry
    profile_registry.registerProfile('linguakeywordwidget_sampletypes',
        'LinguaKeywordWidget Sample Content Types',
        'Extension profile including linguakeywordwidget sample content types',
        'profiles/sample_types',
        'archetypes.linguakeywordwidget',
        EXTENSION)
