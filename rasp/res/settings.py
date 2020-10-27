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


default_profile = SettingProfile(
    name="master",
    author="TUNAPRO1234",
    filename="default_settings",
    settings=default_settings,
)


class Settings:
    default_profile_name = "master"
    profiles = [default_profile]

    @classmethod
    def create_profile(cls, profile: SettingProfile):
        # Eğer aynı isimde bir profil bulunursa
        if cls.find_profile("name", profile.name) is not None:
            return 1

        # Eğer profil kaydedilecekse ve aynı dosya isiminde bir profil bulunursa
        if profile.filename is not None and cls.find_profile(
                "filename", profile.filename) is not None:
            return 2

        cls.profiles.append(profile)
        return 0

    @classmethod
    def find_profile(cls, attr_to_search: str, attr_value: str):
        for index, profile in enumerate(cls.profiles):
            if getattr(profile, attr_to_search) == attr_value:
                return index

        return None
