from rasp.res.glob import *
import os


# region boş
class SettingStruct:
    def __init__(self, theme=default_theme, setting_1=0, setting_2=0):
        self.theme = theme
        self.setting_1 = setting_1
        self.setting_2 = setting_2


default_settings = SettingStruct()


class SettingProfile:
    def __init__(self,
                 name: str,
                 filename: any,
                 settings: SettingStruct = default_settings):

        self.name = name
        self.filename = filename
        self.settings = settings
        # self.__dict__["settings"] = self.settings.__dict__


default_profile = SettingProfile(
    name="master",
    filename="default_settings",
    settings=default_settings,
)
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
    __selected_profile_name = default_profile.name
    __default_profile_name = default_profile.name
    __selected_profile = default_profile
    __profiles = [default_profile]

    @classmethod
    def __find_profile(cls, attr_to_search: str, attr_value: str):
        for index, profile in enumerate(cls.__profiles):
            if getattr(profile, attr_to_search) == attr_value:
                return index

        return None

    @classmethod
    def create_profile(cls, profile: SettingProfile):
        # Eğer aynı isimde bir profil bulunursa
        if cls.__find_profile("name", profile.name) is not None:
            return "name used before"

        # Eğer profil kaydedilecekse ve aynı dosya isiminde bir profil bulunursa
        if profile.filename is not None and cls.__find_profile(
                "filename", profile.filename) is not None:
            return "filename used before"

        cls.__profiles.append(profile)
        return 0

    @classmethod
    def delete_profile(cls, name: str):
        # ana profil silinemez
        if name == default_profile.name:
            return "master profile cannot be deleted"

        elif (id := cls.__find_profile("name", name)) is not None:
            del cls.__profiles[id]

            if name == cls.__default_profile_name:
                cls.__default_profile_name = default_profile.name
            if name == cls.__selected_profile_name:
                cls.__selected_profile_name = default_profile.name
                cls.__selected_profile = default_profile

            return 0

        return "profile not found"

    @classmethod
    def rename_profile(cls, name: str, new_name: str, filename: bool):
        attr = "name" if not filename else "filename"
        if name == default_profile.name:
            return "master profile cannot be touched"

        elif (id := cls.__find_profile("name", name)) is not None:
            if cls.__find_profile(attr, new_name) is None:
                cls.__profiles[id].name = new_name

                if name == cls.__default_profile_name:
                    cls.__default_profile_name = new_name
                if name == cls.__selected_profile_name:
                    cls.__selected_profile = cls.__profiles[id]
                    cls.__selected_profile_name = new_name

                return 0
            return "name used before"

        return "profile not found"

    @classmethod
    def update_profile_settings(cls, name: str, new_settings: SettingStruct):
        if name == default_profile.name:
            return "master profile cannot be touched"

        elif (id := cls.__find_profile("name", name)) is not None:
            cls.__profiles[id].settings = new_settings
            return 0

        return "profile not found"

    @classmethod
    def change_default_profile(cls, name: str):
        if name == cls.__default_profile_name:
            return 0

        elif cls.__find_profile("name", name) is not None:
            cls.__default_profile_name = name
            return 0

        return "profile not found"

    @classmethod
    def select_profile(cls, name: str):
        if name == cls.__selected_profile_name:
            return 0

        elif (id := cls.__find_profile("name", name)) is not None:
            cls.__selected_profile = cls.__profiles[id]
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
            for profile in cls.__profiles:
                if profile.name != default_profile.name:
                    try:
                        os.remove(f"{profile_files_path}/{profile.filename}.json")
                    except FileNotFoundError:
                        pass

        cls.__selected_profile_name = default_profile.name
        cls.__default_profile_name = default_profile.name
        cls.__selected_profile = default_profile
        cls.__profiles = [default_profile]

    @classmethod
    def save_profile_names(cls):
        try:
            encoder.dump(
                {
                    profile.name: profile.filename
                    for profile in cls.__profiles
                    if profile.name != default_profile.name
                },
                profiles_path,
            )
        except:
            return 1
        return 0

    @classmethod
    def save_profile(cls, name):
        profile = name if type(name) == SettingProfile else cls.__profiles[
            cls.__find_profile("name", name)]

        if profile.name == default_profile.name:
            return 0

        try:
            encoder.dump(
                {key:(value.__dict__ if key == "settings" else value) for key, value in profile.settings.__dict__.items()},
                f"{profile_files_path}/{profile.filename}.json",
            )
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
        profiles_dict = decoder.load(profiles_path)

        for name, filename in profiles_dict.items():
            cls.__profiles.append(
                SettingProfile(
                    name, filename,
                    SettingStruct(*decoder.load(
                        "{profile_files_path}/{filename}.json"))))