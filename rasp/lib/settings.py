from rasp.res.glob import *
import os


# region boş
class SettingStruct:
    def __init__(self, theme=default_theme, setting_1=0, setting_2=0, *kw):
        self.theme = theme
        self.setting_1 = setting_1
        self.setting_2 = setting_2


default_settings = SettingStruct()
default_profile_name = "master"

# endregion
"""
Settings.delete_profile()
Settings.change_default_profile()
Settings.selected_profile: name

Settings.load_from_file(profile_name)
Settings.load_all_settings()

"""


class Settings:
    # default ve selectedın farkı yeni oluşturulan profiller default üzerinden oluşturulacak
    __profiles = {default_profile_name: default_settings}
    __selected_profile_name = default_profile_name
    __default_profile_name = default_profile_name
    __current_settings = default_settings

    @classmethod
    def create_profile(cls, name: str, settings: SettingStruct = None):
        settings = SettingStruct() if settings is None else settings
        if name not in cls.__profiles:
            cls.__profiles[name] = settings
            return 0
        return "name used before"

    @classmethod
    def delete_profile(cls, name: str):
        # ana profil silinemez
        if name == default_profile_name:
            return "master profile cannot be deleted"

        elif name in cls.__profiles:
            del cls.__profiles[name]
            try:
                os.remove(f"{profile_files_path}/{name}.json")
            except FileNotFoundError:
                pass

            if name == cls.__default_profile_name:
                cls.__default_profile_name = default_profile_name
            if name == cls.__selected_profile_name:
                cls.__selected_profile_name = default_profile_name
                cls.__current_settings = default_settings

            return 0

        return "profile not found"

    @classmethod
    def rename_profile(cls, name: str, new_name: str, filename: bool):
        if name == default_profile_name:
            return "master profile cannot be renamed"

        elif name in cls.__profiles:
            if new_name not in cls.__profiles:
                cls.__profiles[new_name] = cls.__profiles[name]
                cls.delete_profile(name)

                if name == cls.__default_profile_name:
                    cls.__default_profile_name = new_name
                if name == cls.__selected_profile_name:
                    cls.__current_settings = cls.__profiles[new_name]
                    cls.__selected_profile_name = new_name

                return 0
            return "name used before"

        return "profile not found"

    @classmethod
    def update_profile_settings(cls, name: str, new_settings: SettingStruct):
        if name == default_profile_name:
            return "master profile cannot be touched"

        elif name in cls.__profiles:
            cls.__profiles[name] = new_settings
            return 0

        return "profile not found"

    @classmethod
    def change_default_profile(cls, name: str):
        if name == cls.__default_profile_name:
            return 0

        elif name in cls.__profiles:
            cls.__default_profile_name = name
            return 0

        return "profile not found"

    @classmethod
    def select_profile(cls, name: str):
        if name == cls.__selected_profile_name:
            return 0

        elif name in cls.__profiles:
            cls.__current_settings = cls.__profiles[name]
            cls.__selected_profile_name = name
            return 0

        return "profile not found"

    @classmethod
    def reset(cls, hard=False):
        if hard:
            try:
                os.remove(profiles_path)
            except FileNotFoundError:
                pass

            for name in cls.__profiles:
                if name != default_profile_name:
                    try:
                        os.remove(f"{profile_files_path}/{name}.json")
                    except FileNotFoundError:
                        pass

        cls.__profiles = {default_profile_name: default_settings}
        cls.__selected_profile_name = default_profile_name
        cls.__default_profile_name = default_profile_name
        cls.__current_settings = default_settings

    @classmethod
    def save_profile_names(cls):
        try:
            encoder.dump(
                {
                    "default":
                    cls.__default_profile_name,
                    "selected":
                    cls.__selected_profile_name,
                    "profiles": [
                        name for name in cls.__profiles
                        if (name != default_profile_name)
                    ]
                },
                profiles_path,
            )
        except:
            return 1
        return 0

    @classmethod
    def save_profile(cls, name, settings: SettingStruct = None):
        settings = cls.__profiles[name] if settings is None else settings

        if name == default_profile_name:
            return 0

        try:
            encoder.dump(settings.__dict__,
                         f"{profile_files_path}/{name}.json")
        except:
            return 1
        return 0

    @classmethod
    def save(cls):
        if (rv := cls.save_profile_names()) != 0:
            return rv

        try:
            for profile in cls.__profiles:
                if (rv := cls.save_profile(profile)) != 0:
                    return rv

        except:
            return 1
        return 0

    @classmethod
    def load(cls):
        loaded = decoder.load(profiles_path)

        for name in loaded["profiles"]:
            cls.__profiles[name] = SettingStruct(
                *decoder.load(f"{profile_files_path}/{name}.json"))

        cls.__current_settings = cls.__profiles[loaded["selected"]]
        cls.__selected_profile_name = loaded["selected"]
        cls.__default_profile_name = loaded["default"]
