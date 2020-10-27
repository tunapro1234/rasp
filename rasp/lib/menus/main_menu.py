from rasp.lib.settings import Settings
import rasp.lib.menus.base as base
from rasp.res.glob import *

# print(Settings._Settings__profiles,
#       Settings._Settings__selected_profile_name,
#       Settings._Settings__selected_profile,
#       Settings._Settings__selected_profile.settings,
#       sep="\n")


class MainMenu(base.BaseMenu):
    theme = Settings._Settings__selected_profile.settings.theme
    menu_names = ["tuna", "pro", "1234"]

    @classmethod
    def draw(cls, screen, theme=None, *a, **kw):
        theme = cls.theme if theme is None else theme

        if theme == themes.test:
            base.TestTheme.draw(
                screen,
                cls.menu_names,
            )

        elif theme == themes.megaboi:
            base.MegaboiTheme.draw(screen, cls.menu_names, 12)
