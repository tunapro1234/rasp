from rasp.res.glob import *


class Screen(pygame.Surface):
    def __init__(self, surface: pygame.Surface, *a, **kw):
        self = surface