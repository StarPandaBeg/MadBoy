import logging
import os
import urllib.request

from func import *

ARCHIVE_URL = "https://github.com/StarPandaBeg/MadBoy/archive/master.zip"
VERSION_URL = "https://raw.githubusercontent.com/StarPandaBeg/MadBoy/master/VERSION"
MARKER_URL = "https://chaostech.ru/123.php"

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

    def is_update_required(self):
        local = self.current_version()
        remote = self.remote_version()
        local_v = semantic_to_int(local) if local else -1
        remote_v = semantic_to_int(remote) if remote else -2
        return (local_v < remote_v)

    def auto_update(self):
        pass

    