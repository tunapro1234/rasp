import dbex


# region boş
class SettingStruct:
    def __init__(self, setting_1, setting_2):
        self.setting_1 = setting_1
        self.setting_2 = setting_2


default_settings = SettingStruct(
    setting_1=0,
    setting_2=0,
)


class SettingProfile:
    def __init__(self,
                 name: str,
                 author: str,
                 filename: any,
                 settings: SettingStruct = default_settings):

        self.name = name
        self.author = author
        self.filename = filename
        self.settings = settings

    def __dict__(self):
        return {
            "name": self.name,
            "author": self.author,
            "filename": self.filename,
            "settings": dict(self.settings),
        }


default_profile = SettingProfile(
    name="master",
    author="TUNAPRO1234",
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
    __default_profile_name = default_profile.name
    __selected_profile = default_profile.name
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
            if name == cls.__default_profile_name:
                cls.__default_profile_name = default_profile.name
            if name == cls.__selected_profile:
                cls.__selected_profile = default_profile.name

            del cls.__profiles[id]
            return 0

        return "profile not found"

    @classmethod
    def rename_profile(cls, name: str, new_name: str, filename: bool):
        attr = "name" if not filename else "filename"
        if name == default_profile.name:
            return "master profile cannot be touched"

        elif (id := cls.__find_profile("name", name)) is not None:
            if cls.__find_profile(attr, new_name) is None:
                if name == cls.__default_profile_name:
                    cls.__default_profile_name = new_name
                if name == cls.__selected_profile:
                    cls.__selected_profile = new_name

                cls.__profiles[id].name = new_name
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
    def change_selected_profile(cls, name: str):
        if name == cls.__selected_profile:
            return 0

        elif cls.__find_profile("name", name) is not None:
            cls.__selected_profile = name
            return 0

        return "profile not found"

    @classmethod
    def load(cls):
        for profile in cls.__profiles:
            dbex.Encoder().dump(
                dict(profile),
                f"rasp/res/settings/{profile.filename}.json",
            )

    @classmethod
    def save(cls):
        pass