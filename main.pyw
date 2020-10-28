import PySimpleGUI as sg
from modules.converter import converter
import os

sg.theme('dark grey 10')
layout = [
    [sg.Text("Path of the images to convert  :"), sg.Input(key='-IPATH-',)],
    [sg.Text("Path where to store output      :"), sg.Input(key='-OPATH-')],
    [sg.Text("Output extension                    :"), sg.Input(key='-EXT-')],
    [sg.Multiline('', key='-MSG-', size=(70, 9), disabled=True)],
    [sg.Button('Convert', size=(10, 1)), sg.Button('Exit', size=(10, 1))]
]

size = (600, 400)
title = 'Image converter'
icon='./assets/icon.ico'

window = sg.Window(title, layout, icon= icon, resizable=True, size= size, element_padding=(9, 15))
sg.cprint_set_output_destination(window, '-MSG-')

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    origin = values['-IPATH-']
    output = values['-OPATH-']
    ext = values['-EXT-']
    
    if not os.path.exists(output):
        os.mkdir(output)

    try:
        os.startfile(output)
        for filename in os.listdir(origin):
            return_msg, color = converter(origin, output, filename, ext)
            sg.cprint(return_msg, text_color=color)


    except FileNotFoundError:
        sg.cprint("Directory not found !", text_color='red')

        

window.close()
    

