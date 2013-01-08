Introduction
============

This addon is an archetypes multilingual keyword widget for Plone.

How to use
==========

As any widget for Archetypes::

  from Products.Archetypes.atapi
  from archetypes.linguakeywordwidget.widget import LinguaKeywordWidget
  atapi.Schema((
    atapi.LinesField('subject',
       multiValued=1,
       accessor="Subject",
        widget=LinguaKeywordWidget()),
  ))

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
======================

keywordalias achieve same goal in a different way. With keyword alias
your keywords are translated in backoffice. With linguakeywords you have
just different keywords.

Credits
=======

Companies
---------

|cirb|_ CIRB / CIBG

* `Contact CIRB <mailto:irisline@irisnet.be>`_

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

People
------

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. |cirb| image:: http://www.cirb.irisnet.be/logo.jpg
.. _cirb: http://cirb.irisnet.be
.. _sitemap: http://support.google.com/webmasters/bin/answer.py?hl=en&answer=183668&topic=8476&ctx=topic
.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _documentation: http://plone.org/documentation/kb/installing-add-ons-quick-how-to
.. _redomino.keywordalias: https://github.com/redomino/redomino.keywordalias
