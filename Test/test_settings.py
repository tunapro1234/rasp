from rasp.lib.settings import SettingProfile, Settings
import unittest


class TestSettings(unittest.TestCase):
    def test_load_settings(self):
        Settings.create_profile(SettingProfile("test", "tuna", "filetuna"))
        Settings.
