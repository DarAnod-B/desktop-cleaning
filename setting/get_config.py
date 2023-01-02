import winshell
import re

import configparser
from setting.find_path import path_to_config


path = path_to_config()
config = configparser.ConfigParser()
config.read(path, encoding="utf-8")


DESKTOP_PATH = winshell.desktop()
STORAGE_FOLDER = str(config["parameter"]["STORAGE_FOLDER"])
ALLOWED_EXTENSIONS = re.sub(
    "[^A-Za-zА-Яа-я ]", "", config["parameter"]["ALLOWED_EXTENSIONS"]).split(' ')
TRANSFER_FOLDERS = bool(config["flag"]["TRANSFER_FOLDERS"])
