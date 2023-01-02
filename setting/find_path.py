import sys
import os
import ctypes.wintypes
import shutil


def path_to_documents():
    CSIDL_PERSONAL = 5       # My Documents
    SHGFP_TYPE_CURRENT = 0   # Get current, not default value

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(
        0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf)

    return buf.value


def create_config(config_path):
    def_config_name = 'default_config.ini'

    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    elif __file__:
        application_path = os.path.dirname(__file__)

    def_config_path = os.path.join(application_path, def_config_name)
    shutil.copy(def_config_path, config_path)


def path_to_config():
    config_foulder_name = 'desktop_cleaning'
    config_name = 'config.ini'

    config_foulder_path = os.path.join(
        path_to_documents(), config_foulder_name)
    os.makedirs(config_foulder_path, exist_ok=True)
    config_path = os.path.join(config_foulder_path, config_name)

    if not os.path.exists(config_path):
        create_config(config_path)
    return config_path
