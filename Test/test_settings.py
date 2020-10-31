from rasp.res.glob import encoder, decoder, profile_files_path, profiles_path
from rasp.lib.settings import Settings
import unittest
import os


class TestSettings(unittest.TestCase):
    def setUp(self):
        Settings.reset(hard=True)

    def test_save_profile_names(self):
        profile_name = "test"

        Settings.create_profile(profile_name)
        Settings.save_profile_names()

        profiles_dict = decoder.load(profiles_path)

        for name in profiles_dict:
            self.assertEqual(name, profile_name)

    def test_reset(self):
        profile_name = "test"

        old_profiles = dict(Settings._Settings__profiles)
        Settings.create_profile(profile_name)

        self.assertNotEqual(old_profiles, Settings._Settings__profiles)
        Settings.reset()

        self.assertEqual(old_profiles, Settings._Settings__profiles)

    def test_reset_hard(self):
        profile_name = "test"
        profile_filename = "testfile"

        old_profiles = tuple(Settings._Settings__profiles)
        Settings.create_profile(profile_name)

        self.assertEqual(Settings.save(), 0)

        Settings.reset(hard=True)

        for profile in old_profiles:
            self.assertEqual(
                os.path.exists("{profile_files_path}/{profile.filename}.json"),
                False)

        self.assertEqual(os.path.exists(profile_filename), False)

    def test_load(self):
        pass

    def test_save(self):
        pass

    def test_save_profiles(self):
        pass

    def test_delete(self):
        pass

    def test_rename(self):
        pass

    def test_select(self):
        pass

    def test_selected_after_load(self):
        pass
