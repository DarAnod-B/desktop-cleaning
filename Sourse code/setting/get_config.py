import winshell
import re

import configparser
from setting.find_path import path_to_config


def list_processing(list_as_a_string):
    return re.sub("[^A-Za-zА-Яа-я0-9_ ]", "", list_as_a_string).split(" ")


path = path_to_config()
config = configparser.ConfigParser()
config.read(path, encoding="utf-8")


DESKTOP_PATH = winshell.desktop()
STORAGE_FOLDER = config["parameter"]["STORAGE_FOLDER"]
WALLPAPER_PATH = config["parameter"]["WALLPAPER_PATH"]
ALLOWED_EXTENSIONS = list_processing(config["parameter"]["ALLOWED_EXTENSIONS"])
EXCLUDED_NAMES = list_processing(config["parameter"]["EXCLUDED_NAMES"])

TRANSFER_FOLDERS = bool(config["flag"]["TRANSFER_FOLDERS"])
SET_WALLPAPER = bool(config["flag"]["SET_WALLPAPER"])
