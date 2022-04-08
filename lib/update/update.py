import logging
import os
import urllib.request

from func import *

ARCHIVE_URL = "https://github.com/StarPandaBeg/MadBoyX/archive/master.zip"
VERSION_URL = "https://raw.githubusercontent.com/StarPandaBeg/MadBoyX/master/VERSION"
# MARKER_URL = "https://chaostech.ru/123.php"

class Update:

    def current_version(self):
        if (os.path.exists("VERSION")):
            with open("VERSION", 'r') as f:
                return f.read()
        else:
            return None

    def remote_version(self):
        try:
            path, _ = urllib.request.urlretrieve(VERSION_URL, "TMP")
            if not os.path.exists(path):
                return None
            with open("TMP") as f:
                v = f.read()
            os.remove("TMP")
            return v
        except:
            return None

    def is_update_required(self, local, remote):
        local_v = semantic_to_int(local) if local else -1
        remote_v = semantic_to_int(remote) if remote else -2
        return (local_v < remote_v)

    def update(self):
        pass

    def auto_update(self):
        local = self.current_version()
        remote = self.remote_version()

        logging.info(f"Current version: {local}")
        logging.info(f"Remote version: {remote}")

        if self.is_update_required(local, remote):
            logging.info("Starting update...")

            with open("UPDATE_IN_PROGRESS", 'w') as f:
                pass
            self.update()
            os.remove("UPDATE_IN_PROGRESS")
            
            logging.info(f"Restarting script...")
            os.system(f"run.bat")
            exit()

    