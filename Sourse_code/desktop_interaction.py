import os
from setting.get_config import STORAGE_FOLDER, DESKTOP_PATH, WALLPAPER_PATH
import win32api
import win32con
import win32gui
import shutil


def path_from_desktop(*path):
    return os.path.join(DESKTOP_PATH, *path)


def moving_files_and_folders(all_name):
    for name in all_name:
        shutil.move(path_from_desktop(name),
                    path_from_desktop(STORAGE_FOLDER, name))


def setWallpaper():
        key = win32api.RegOpenKeyEx(
            win32con.HKEY_CURRENT_USER, os.path.join("Control Panel", "Desktop"), 0, win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(
            win32con.SPI_SETDESKWALLPAPER, WALLPAPER_PATH, 1+2)
