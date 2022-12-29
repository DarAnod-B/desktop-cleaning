import configparser
import os


def save_settings(func):
    def wrapper(*args, **kwargs):
        path_to_settings = os.path.join("setting", "config.ini")
        config = configparser.ConfigParser()
        config.read(path_to_settings, encoding='utf-8')

        config = func(*args, **kwargs, config=config)

        with open(path_to_settings, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
    return wrapper


@save_settings
def change_STORAGE_FOLDER(name, config):
    config["parameter"]["STORAGE_FOLDER"] = f"{name}"
    return config


@save_settings
def change_ALLOWED_EXTENSIONS(value, config):
    config["parameter"]["ALLOWED_EXTENSIONS"] = f"{value}"
    return config

@save_settings
def change_TRANSFER_FOLDERS(value, config):
    config["flag"]["TRANSFER_FOLDERS"] = f"{value}"
    return config
