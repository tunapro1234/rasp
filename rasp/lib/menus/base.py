from rasp.lib.settings import Settings
from rasp.res.glob import *


class MetaMenu(type):
    def __new__(cls, name, bases, body):
        # print(cls, name, bases, body, sep="\n")

        attributes = ["draw"]

        if name != "BaseMenu":
            for attr in attributes:
                if attr not in body:
                    raise TypeError(f"Required attribute not found: {attr}")

        return super().__new__(cls, name, bases, body)


class BaseMenu(metaclass=MetaMenu):
    pass  # gelicem


class MegaboiTheme(BaseMenu):
    @staticmethod
    def draw(screen, menu_names, length, width=2):
        menu_height = HEIGHT // length

        for i in range(length):
            pygame.draw.rect(
                screen, colors.red,
                pygame.Rect((width // 2, i * menu_height + width // 2),
                            (WIDTH - width, menu_height - width)), 1)


class TestTheme(BaseMenu):
    @staticmethod
    def draw(screen, menu_names, length=10, offset=1, width=3):
        # menu_height = (HEIGHT - int(width / 2 + offset)) // length
        menu_height = HEIGHT // length

        # 480 // 10 - 2
        # 46
        # [0-45] [46-]

        for i in range(length):
            pygame.draw.rect(
                screen,
                colors.white,
                # yapf: disable
                pygame.Rect((offset * 2 + width // 2,
                             i * menu_height + offset + width // 2),
                            (WIDTH - (offset * 4 + width), menu_height -
                             (offset * 2 + width))),

                # yapf: enable
                width)
