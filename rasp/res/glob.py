import dbex

WIDTH, HEIGHT = 1024, 768
FULLSCREEN = 0
TITLE = "RAP"
FPS = 120


class themes:
    test = -1
    empty = 0
    megaboi = 1
    text_based = 2

default_theme = themes.test

encoder = dbex.Encoder()
decoder = dbex.Decoder()

profiles_path = "rasp/res/profiles.json"
profile_files_path = "rasp/res/settings"