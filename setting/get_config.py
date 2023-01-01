import winshell
import configparser
from setting.find_path import path_to_config


path = path_to_config()
config = configparser.ConfigParser()
config.read(path, encoding="utf-8")


DESKTOP_PATH = winshell.desktop()
STORAGE_FOLDER = config["parameter"]["STORAGE_FOLDER"]
ALLOWED_EXTENSIONS = config["parameter"]["ALLOWED_EXTENSIONS"]
TRANSFER_FOLDERS = config["flag"]["TRANSFER_FOLDERS"]
