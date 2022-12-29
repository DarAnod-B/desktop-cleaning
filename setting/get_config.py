import winshell
import configparser


config = configparser.ConfigParser()
config.read("setting\config.ini", encoding="utf-8")


DESKTOP_PATH = winshell.desktop()
STORAGE_FOLDER = config["parameter"]["STORAGE_FOLDER"]
ALLOWED_EXTENSIONS = config["parameter"]["ALLOWED_EXTENSIONS"]
TRANSFER_FOLDERS = config["flag"]["TRANSFER_FOLDERS"]

