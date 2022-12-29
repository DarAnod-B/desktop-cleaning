import PySimpleGUI as sg
import re
from setting.set_config import change_STORAGE_FOLDER, change_ALLOWED_EXTENSIONS, change_TRANSFER_FOLDERS

sg.theme('DarkTeal2')

layout = [
    [sg.Text('Название папки в которую сохраняют данные:')],
    [sg.Input(key='-STORAGE_FOLDER-', enable_events=True, default_text='Прочее')],
    [sg.Text('Сохраняемые расширения:')],
    [sg.Input(key='-extensions-', enable_events=True, default_text='Ink ini')],
    [sg.Checkbox('Сохранять папки', key='-folder-', size=(12, 1))],
    [sg.Button('Ok', button_color='green'), sg.Button('Cancel')],
]


window = sg.Window('Desktop cleaning', layout)


def validation_check():
    if values['-STORAGE_FOLDER-'].replace(' ', '') == '':
        return False
    elif values['-extensions-'].replace(' ', '') == '':
        return False
    return True


def folder_name_processing(folder_name):
    return folder_name.replace(' ', '')


def extension_list_create(extension_str):
    extension_str = re.sub(" +", " ", extension_str.strip())
    return extension_str.split(' ')


while True:
    event, values = window.read()

    # Настройка закрытия окна.
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # Валидация введеных данных
    if validation_check():
        window['Ok'].update(button_color='green')
    else:
        window['Ok'].update(button_color='black')
        continue

    # Обработка нажатия кнопок
    if event == 'Ok':
        change_STORAGE_FOLDER(
            folder_name_processing(values['-STORAGE_FOLDER-']))
        change_ALLOWED_EXTENSIONS(
            extension_list_create(values['-extensions-']))
        change_TRANSFER_FOLDERS(values['-folder-'])


window.close()
