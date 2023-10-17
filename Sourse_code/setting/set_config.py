import configparser
from setting.create_config_and_find_him_path import path_to_config
import re

def removing_spaces_in_a_str(extension_str):
    return re.sub(" +", " ", extension_str.strip())


def list_processing(list_as_a_string):
    clean_list_as_a_string = re.sub("[^A-Za-zА-Яа-я0-9_; ]", "", list_as_a_string)
    if clean_list_as_a_string == "":
        return []
    return clean_list_as_a_string

def save_settings(func):
    def wrapper(*args, **kwargs):
        path = path_to_config()
        config = configparser.ConfigParser()
        config.read(path, encoding='utf-8')

        config = func(*args, **kwargs, config=config)

        with open(path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    return wrapper


@save_settings
def change_STORAGE_FOLDER(name, config):
    config["parameter"]["STORAGE_FOLDER"] = f"{name}"
    return config


@save_settings
def change_WALLPAPER_PATH(value, config):
    config["parameter"]["WALLPAPER_PATH"] = f"{value}"
    return config


@save_settings
def change_ALLOWED_EXTENSIONS(str_of_extensions, config):
    str_of_extensions = removing_spaces_in_a_str(str_of_extensions)
    str_of_extensions =  list_processing(str_of_extensions)
    config["parameter"]["ALLOWED_EXTENSIONS"] = f"{str_of_extensions}"
    return config


@save_settings
def change_EXCLUDED_NAMES(str_of_names, config):
    str_of_names = removing_spaces_in_a_str(str_of_names)
    str_of_names =  list_processing(str_of_names)
    
    if str_of_names != "[]":
        config["parameter"]["EXCLUDED_NAMES"] = f"{str_of_names}"
    else:
        config["parameter"]["EXCLUDED_NAMES"] = ""
    return config


@save_settings
def change_TRANSFER_FOLDERS(value, config):
    config["flag"]["TRANSFER_FOLDERS"] = f"{value}"
    return config


@save_settings
def change_SET_WALLPAPER(value, config):
    config["flag"]["SET_WALLPAPER"] = f"{value}"
    return config
