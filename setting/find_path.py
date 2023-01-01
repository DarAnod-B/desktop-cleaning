import sys
import os


def path_to_config():
    config_name = 'config.ini'

    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    elif __file__:
        application_path = os.path.dirname(__file__)

    config_path = os.path.join(application_path, config_name)
    return config_path
  