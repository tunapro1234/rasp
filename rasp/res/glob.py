import pygame
import dbex

# WIDTH, HEIGHT = 1024, 768
WIDTH, HEIGHT = 640, 480
FULLSCREEN = 0
TITLE = "RAP"
FPS = 120


class themes:
    test = -1
    empty = 0
    megaboi = 1
    textbased = 2


class colors:
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    lime = (0, 255, 0)
    maroon = (50, 0, 0)
    turq = (64, 224, 208)
    orange = (255, 69, 0)
    green = (34, 139, 34)
    gray = (128, 128, 128)
    white = (255, 255, 255)


default_theme = themes.test

encoder = dbex.Encoder()
decoder = dbex.Decoder()

profiles_path = "rasp/res/profiles.json"
profile_files_path = "rasp/res/settings"