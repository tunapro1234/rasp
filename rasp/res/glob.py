import dbex

WIDTH, HEIGHT = 1024, 768
FULLSCREEN = 0
TITLE = "RAP"
FPS = 120

encoder = dbex.Encoder()
decoder = dbex.Decoder()

profiles_path = "rasp/res/profiles.json"
profile_files_path = "rasp/res/settings"