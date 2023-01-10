import PySimpleGUI as sg
import re
import os
from setting.set_config import change_STORAGE_FOLDER, change_ALLOWED_EXTENSIONS, change_EXCLUDED_NAMES, change_WALLPAPER_PATH, change_SET_WALLPAPER, change_TRANSFER_FOLDERS
from setting.find_path import path_to_application
from setting.get_config import STORAGE_FOLDER, WALLPAPER_PATH, ALLOWED_EXTENSIONS, EXCLUDED_NAMES


def validation_check(values):
    if values['-STORAGE_FOLDER-'].replace(' ', '') == '':
        return False
    elif values['-ALLOWED_EXTENSIONS-'].replace(' ', '') == '':
        return False
    return True


def button_activation(values):
    if validation_check(values):
        window['Ok'].update(button_color='green', disabled=False)
    else:
        window['Ok'].update(button_color='black', disabled=True)


def visible_change(values):
    for key in ['-SELECTION_1-', '-WALLPAPER_PATH-', '-Browse-', '-SELECTION_2-']:
        window[key].update(visible=values['-SET_WALLPAPER-'])


def interface_update(values):
    button_activation(values)
    visible_change(values)


def list_create(extension_str):
    return re.sub(" +", " ", extension_str.strip())


def saving_config_changes(values):
    change_STORAGE_FOLDER(
        values['-STORAGE_FOLDER-'].replace(' ', ''))
    change_ALLOWED_EXTENSIONS(
        list_create(values['-ALLOWED_EXTENSIONS-']))
    change_EXCLUDED_NAMES(
        list_create(values['-EXCLUDED_NAMES-']))
    change_SET_WALLPAPER(values['-SET_WALLPAPER-'])
    change_WALLPAPER_PATH(values['-WALLPAPER_PATH-'])
    change_TRANSFER_FOLDERS(values['-TRANSFER_FOLDERS-'])




def launch_interface():
    sg.theme('Black')

    layout = [
        [sg.Text('Название папки в которую сохраняют данные:')],
        [sg.Input(key='-STORAGE_FOLDER-', enable_events=True,
                  default_text=STORAGE_FOLDER)],

        [sg.Text('Непереносимые расширения\n(перечисление через пробел):')],
        [sg.Input(key='-ALLOWED_EXTENSIONS-', enable_events=True,
                  default_text=ALLOWED_EXTENSIONS)],

        [sg.Text(
            'Объекты исключенные из переноса \n(в названиях не должно быть пробелов или расширения,\n перечисление через пробел):')],
        [sg.Input(key='-EXCLUDED_NAMES-', enable_events=True,
                  default_text=EXCLUDED_NAMES)],

        [sg.Checkbox('Переносить папки', key='-TRANSFER_FOLDERS-', enable_events=True,
                     default=True,  size=(13, 1))],
        [sg.Checkbox('Смена обоев', key='-SET_WALLPAPER-', enable_events=True,
                     default=False,  size=(12, 1))],

        [sg.Text('_' * 45, key="-SELECTION_1-", visible=False, size=(40, 1))],
        [sg.Input(key="-WALLPAPER_PATH-", default_text=WALLPAPER_PATH, change_submits=True, visible=False,  size=(36, 1)),
         sg.FileBrowse(key="-Browse-", visible=False)],
        [sg.Text('_' * 45, key="-SELECTION_2-", visible=False, size=(40, 1))],

        [sg.Button('Ok', button_color='green'), sg.Button('Cancel')],

    ]

    path_to_icon = os.path.join(path_to_application(), 'setting', 'data', 'icon.ico')
    global window
    window = sg.Window('DesktopCleaning', layout, icon=path_to_icon)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        interface_update(values)

        if event == 'Ok':
            saving_config_changes(values)
            break

    window.close()


if __name__ == '__main__':
    launch_interface()
