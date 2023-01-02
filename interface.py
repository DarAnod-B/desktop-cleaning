import PySimpleGUI as sg
import re
from setting.set_config import change_STORAGE_FOLDER, change_ALLOWED_EXTENSIONS, change_TRANSFER_FOLDERS
from setting.get_config import STORAGE_FOLDER, ALLOWED_EXTENSIONS


def validation_check(values):
    if values['-STORAGE_FOLDER-'].replace(' ', '') == '':
        return False
    elif values['-ALLOWED_EXTENSIONS-'].replace(' ', '') == '':
        return False
    return True


def extension_list_create(extension_str):
    extension_str = re.sub(" +", " ", extension_str.strip())
    return extension_str.split(' ')


def launch_interface():
    sg.theme('Black')

    layout = [
        [sg.Text('Название папки в которую сохраняют данные:')],
        [sg.Input(key='-STORAGE_FOLDER-', enable_events=True,
                  default_text=STORAGE_FOLDER)],
        [sg.Text('Сохраняемые расширения:')],
        [sg.Input(key='-ALLOWED_EXTENSIONS-', enable_events=True,
                  default_text=' '.join(ALLOWED_EXTENSIONS))],
        [sg.Checkbox('Сохранять папки', key='-TRANSFER_FOLDERS-', enable_events=True,
                     default=True,  size=(12, 1))],
        [sg.Button('Ok', button_color='green'), sg.Button('Cancel')],
    ]

    window = sg.Window('Desktop cleaning', layout)

    while True:
        event, values = window.read()
        # Настройка закрытия окна.
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        # Валидация введеных данных
        if validation_check(values):
            window['Ok'].update(button_color='green')
        else:
            window['Ok'].update(button_color='black')
            continue

        # Обработка нажатия кнопок
        if event == 'Ok':
            change_STORAGE_FOLDER(
                values['-STORAGE_FOLDER-'].replace(' ', ''))
            change_ALLOWED_EXTENSIONS(
                extension_list_create(values['-ALLOWED_EXTENSIONS-']))
            change_TRANSFER_FOLDERS(values['-TRANSFER_FOLDERS-'])
            break

    window.close()


if __name__ == '__main__':
    launch_interface()
