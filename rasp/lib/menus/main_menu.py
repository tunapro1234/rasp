from rasp.lib.menus.themes import theme_classes
from rasp.lib.settings import Settings
import rasp.lib.menus.base as base
from rasp.res.glob import *


class MainMenu(base.BaseMenu):
    menu_names = [__name__, "tuna", "pro", "1234", "test", *range(10)]

    @classmethod
    def draw(cls, screen, theme=None, *a, **kw):
        theme = Settings._Settings__selected_profile.settings.theme if (
            theme is None) else theme

        theme_classes[theme].draw(screen, cls.menu_names)
