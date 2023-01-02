import PySimpleGUI as sg
import re
import os


def launch_interface():
    sg.theme('Black')

    layout = [
        [sg.Checkbox('Сохранять папки', key='-TRANSFER_FOLDERS-', enable_events=True,
                     default=True,  size=(12, 1))],
        [sg.Input(key="-IN2-",  size=(36, 1), visible=False),
         sg.FileBrowse(key="-IN-", visible=False)],

    ]

    window = sg.Window('DesktopCleaning', layout)

    while True:
        event, values = window.read()

        if values['-TRANSFER_FOLDERS-'] == True:
            print('123')
            window['-IN2-'].update(visible=True)
            window['-IN-'].update(visible=True)
        else:
            window['-IN2-'].update(visible=False)
            window['-IN-'].update(visible=False)

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()


if __name__ == '__main__':
    launch_interface()
