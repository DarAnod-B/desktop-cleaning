import configparser
from setting.find_path import path_to_config


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
def change_ALLOWED_EXTENSIONS(list_of_extensions, config):
    config["parameter"]["ALLOWED_EXTENSIONS"] = f"{list_of_extensions}"
    return config


@save_settings
def change_EXCLUDED_NAMES(list_of_names, config):
    config["parameter"]["EXCLUDED_NAMES"] = f"{list_of_names}"
    return config


@save_settings
def change_TRANSFER_FOLDERS(value, config):
    config["flag"]["TRANSFER_FOLDERS"] = f"{value}"
    return config


@save_settings
def change_SET_WALLPAPER(value, config):
    config["flag"]["SET_WALLPAPER"] = f"{value}"
    return config
