import winshell
import configparser
from setting.create_config_and_find_him_path import path_to_config



def str_to_list(list_as_a_string):
    if list_as_a_string == "[]":
        return []
    
    return [i.strip() for i in list_as_a_string.split(";")]


path = path_to_config()
config = configparser.ConfigParser()
config.read(path, encoding="utf-8")


DESKTOP_PATH = winshell.desktop()
STORAGE_FOLDER = config["parameter"]["STORAGE_FOLDER"]
WALLPAPER_PATH = config["parameter"]["WALLPAPER_PATH"]
ALLOWED_EXTENSIONS = str_to_list(config["parameter"]["ALLOWED_EXTENSIONS"])
EXCLUDED_NAMES = str_to_list(config["parameter"]["EXCLUDED_NAMES"])

TRANSFER_FOLDERS = config["flag"].getboolean("TRANSFER_FOLDERS")
SET_WALLPAPER = config["flag"].getboolean("SET_WALLPAPER")


if __name__ == "__main__":
    list_mame = " ыврапшпыв ю... ЖЖ оашщфщшофкпп;;шопфощшапшо"
    print(str_to_list(list_mame))
