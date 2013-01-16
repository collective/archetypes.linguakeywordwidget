import unittest2 as unittest
from archetypes.linguakeywordwidget.tests import base
from plone import api


class IntegrationTestLingua(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_getLinguaKeywords(self):
        document = api.content.create(container=self.portal,
                                      type="Document",
                                      title="Test document")
        document.setSubject(['en-tag 1', 'en-tag 2', 'tag 3'])
        document.reindexObject()
        fieldName = 'subject'
        field = document.getField(fieldName)
        keywords = document.getLinguaKeywords(fieldName,
                                              field.accessor,
                                              'portal_catalog')
        self.assertEqual(len(keywords), 2)
        self.assertIn('tag 1', keywords)
        self.assertIn('tag 2', keywords)

    def test_getLinguaKeywordsFromValues(self):
        value = ('en-tag 1', 'en-tag 2')
        keywords = self.portal.getLinguaKeywordsFromValue(value)
        self.assertEqual(len(keywords), 2)
        self.assertIn('tag 1', keywords)
        self.assertIn('tag 2', keywords)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
