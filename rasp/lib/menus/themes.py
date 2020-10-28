import rasp.lib.menus.base as base
from rasp.res.glob import *

# Theme classları sadece fonksyionları bir arada tutmak için


class TextBasedTheme(base.BaseMenu):
    @staticmethod
    def draw(mode="mm", *a, **kw):
        if mode in ["mm", "main", "main_menu"]:
            TextBasedTheme.draw_mm(*a, **kw)

    @staticmethod
    def draw_mm(screen, menu_names: list, size: int = 16):
        pass

    @staticmethod
    def _print(*values, sep: str = " ", end: str = "\n"):
        for value in values:
            pass


class MegaboiTheme(base.BaseMenu):
    @staticmethod
    def draw(mode="mm", *a, **kw):
        if mode in ["mm", "main", "main_menu"]:
            MegaboiTheme.draw_mm(*a, **kw)

    @staticmethod
    def draw_mm(screen,
                menu_names: list,
                length: int = 8,
                width: int = 2,
                *a,
                **kw):
        menu_height = HEIGHT // length

        for i in range(length):
            pygame.draw.rect(
                screen, colors.red,
                pygame.Rect((width // 2, i * menu_height + width // 2),
                            (WIDTH - width, menu_height - width)), 1)


class TestTheme(base.BaseMenu):
    @staticmethod
    def draw(mode="mm", *a, **kw):
        print()
        if mode in ["mm", "main", "main_menu"]:
            TestTheme.draw_mm(*a, **kw)

    @staticmethod
    def draw_mm(screen,
                menu_names: list,
                length: int = 10,
                offset: int = 1,
                width: int = 3,
                *a,
                **kw):

        # menu_height = (HEIGHT - int(width / 2 + offset)) // length
        menu_height = HEIGHT // length

        for i in range(length):
            pygame.draw.rect(
                screen, colors.white,
                pygame.Rect((offset * 2 + width // 2,
                             i * menu_height + offset + width // 2),
                            (WIDTH - (offset * 4 + width), menu_height -
                             (offset * 2 + width))), width)


theme_classes = {
    themes.test: TestTheme,
    themes.megaboi: MegaboiTheme,
    themes.textbased: TextBasedTheme
}
