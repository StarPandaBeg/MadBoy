# Backport to 1.0
if (__name__ != "__main__"):
    def main():
        import os
        if (os.path.exists("update.py")):
            os.remove("update.py")
            with open("run.bat", 'r', encoding="utf-8") as f:
                content = f.read()
            with open("run.bat", 'w', encoding="utf-8") as f:
                f.write(content.replace("update.py", "main.py"))
            os.system(f"run.bat")
            exit()

from func import *

load_paths()
configure_logger()

from update import Update
Update().auto_update()

from app import App
App().run()