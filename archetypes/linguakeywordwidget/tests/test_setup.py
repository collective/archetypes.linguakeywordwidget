import unittest2 as unittest
from archetypes.linguakeywordwidget.tests import base


class IntegrationTestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_skins(self):
        skins = self.portal.portal_skins
        selection = skins._getSelections()
        for theme in selection:
            self.assertIn('linguakeywordwidget', selection[theme].split(','))


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
