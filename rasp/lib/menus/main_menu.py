from rasp.lib.menus.base_menu import BaseMenu
from rasp.lib.settings import Settings
from rasp.res.glob import themes
import pygame

print(Settings._Settings__profiles,
      Settings._Settings__selected_profile_name,
      Settings._Settings__selected_profile,
      Settings._Settings__selected_profile.settings,
      sep="\n")


class MainMenu(BaseMenu):
    theme = Settings._Settings__selected_profile.settings.theme

    @classmethod
    def draw(cls, theme=None, *a, **kw):
        theme = cls.theme if theme is None else theme

        if theme == themes.test:
            # print("MainMenu.draw")
            pass
