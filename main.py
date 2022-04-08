from func import *

load_paths()
configure_logger()

from update import Update
v = Update().is_update_required()
print(v)
exit()

from app import App
App().run()