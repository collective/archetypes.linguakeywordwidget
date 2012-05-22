Introduction
============

This addon is an archetypes multilingual keyword widget for Plone.

How it works
============

Keywords are stored in catalog but prefixes with language code before write
and unprefixed before display. It means if you have widget / viewlet /view
that access to data you must first remove language that way::

    keywords = context.Subject()
    linguakeywords = []
    language = context.Language()
    for keyword in value:
        if keyword.startswith('%s-' % language):
            linguakeywords.append(keyword[len(language) + 1:])
        else:
            linguakeywords.append(keyword)
    return linguakeywords


redomino.keywordalias_
----------------------

keywordalias achieve same goal in a different way. With keyword alias
your keywords are translated in backoffice. With linguakeywords you have
just different keywords.

.. _redomino.keywordalias: https://github.com/redomino/redomino.keywordalias
