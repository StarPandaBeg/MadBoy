from func import *

load_paths()
configure_logger()

from update import Update
Update().auto_update()

from app import App
App().run()