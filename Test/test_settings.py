from rasp.lib.settings import Settings
import unittest


class TestSettings(unittest.TestCase):
    def test_settings(self):
        print(dict(Settings.__profiles[0]))