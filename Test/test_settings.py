from rasp.res.glob import encoder, decoder, profile_files_path, profiles_path
from rasp.lib.settings import SettingProfile, Settings
import unittest
import os


class TestSettings(unittest.TestCase):
    def setUp(self):
        Settings.reset()

    def test_save_profiles(self):
        profile_name = "test"
        profile_filename = "testfile"
        Settings.create_profile(
            SettingProfile(profile_name, "tuna", profile_filename))
        Settings.save()

        profiles_dict = decoder.load(profiles_path)

        for name, filename in profiles_dict.items():
            self.assertEqual(name, profile_name)
            self.assertEqual(filename, profile_filename)

    def test_reset(self):
        profile_name = "test"
        profile_filename = "testfile"

        old_profiles = tuple(Settings._Settings__profiles)
        Settings.create_profile(
            SettingProfile(profile_name, "tuna", profile_filename))

        self.assertNotEqual(list(old_profiles), Settings._Settings__profiles)
        Settings.reset()

        self.assertEqual(list(old_profiles), Settings._Settings__profiles)

    def test_reset_hard(self):
        profile_name = "test"
        profile_filename = "testfile"

        old_profiles = tuple(Settings._Settings__profiles)
        Settings.create_profile(
            SettingProfile(profile_name, "tuna", profile_filename))

        self.assertEqual(Settings.save(), 0)

        Settings.reset(hard=True)

        for profile in old_profiles:
            self.assertEqual(os.path.exists("{profile_files_path}/{profile.filename}.json"), False)
        
        self.assertEqual(os.path.exists(profile_filename), False)
