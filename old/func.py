import logging
import os
import random
import shutil
import sys
import string

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = ROOT_DIR + r"\lib"
MODULES_DIR = ROOT_DIR + r"\modules"
TASKS_DIR = ROOT_DIR + r"\background"

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

def load_paths():
    for f in os.walk(LIB_DIR):
        x = f[0]
        if x.find("__pycache__") is not -1:
            continue
        sys.path.append(x)

def configure_logger():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO, datefmt=LOG_DATE_FORMAT)

def generate_client_id():
    return f"pyxploit-{random.randint(100000, 999999)}"

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def get_drives():
    return ['%s' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

def semantic_to_int(version):
    l = [int(x, 10) for x in version.split('.')]
    l.reverse()
    version = sum(x * (100 ** i) for i, x in enumerate(l))
    return version

def rm_if_exists(path, tree=False):
    if os.path.exists(path):
        if tree:
            shutil.rmtree(path)
        else:
            os.remove(path)