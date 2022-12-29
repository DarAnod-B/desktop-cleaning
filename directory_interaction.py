import os
from setting.get_config import STORAGE_FOLDER, DESKTOP_PATH


def path_from_desktop(*path):
    return os.path.join(DESKTOP_PATH, *path)


def moving_files_and_folders(all_name):
    for name in all_name:
        os.replace(path_from_desktop(name),
                   path_from_desktop(STORAGE_FOLDER, name))
