import os
import sys
import win32com.client


def creating_a_shortcut(path_to_shortcut):
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path_to_shortcut)
    shortcut.arguments = '--no_interface'
    shortcut.Targetpath = sys.argv[0]
    shortcut.save()


def autorun_activation():
    user_folder_path = os.path.expanduser('~')
    path_to_startup = f"{user_folder_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"

    thisfile_path = sys.argv[0]
    thisfile_name = os.path.basename(thisfile_path).rsplit('.', 1)[0]

    path_to_shortcut = os.path.join(
        path_to_startup, f'{thisfile_name}.lnk')

    if not os.path.exists(path_to_shortcut):
        creating_a_shortcut(path_to_shortcut)
