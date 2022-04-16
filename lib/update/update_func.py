from distutils.dir_util import copy_tree
import os
import shutil
import stat

import urllib.request
import zipfile

from func import rm_if_exists

ARCHIVE_URL = "https://github.com/StarPandaBeg/MadBoy/archive/master.zip"
VERSION_URL = "https://raw.githubusercontent.com/StarPandaBeg/MadBoy/master/VERSION"

def change_perms(d):
    for root, dirs, files in os.walk(d):  
        for dir in dirs:
            os.chmod(os.path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(os.path.join(root, file), stat.S_IRWXU)

def download_remote(dest):
    if os.path.exists(dest):
        change_perms(dest)
        rm_if_exists(dest, True)
    path, _ = urllib.request.urlretrieve(ARCHIVE_URL, "TMP")
    z = zipfile.ZipFile(path)
    z.extractall(path=dest)

    copy_tree(dest+"/MadBoy-master", dest)
    rm_if_exists(dest+"/MadBoy-master", True)
    return True

def copy_current(dest):
    if (os.path.exists(dest)):
        change_perms(dest)
        rm_if_exists(dest, True)
    shutil.copytree(os.getcwd(), dest, ignore=shutil.ignore_patterns('.git*', '*.db', '__pycache__*', 'newver*', 'UPDATE_IN_PROGRESS', 'TMP'))

def clear_dir(dest, except_ = []):
    for i in os.listdir(dest):
        if i in except_:
            continue
        rm_if_exists(i, os.path.isdir(i))