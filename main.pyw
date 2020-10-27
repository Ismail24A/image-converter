import PySimpleGUI as sg
from PIL import Image, UnidentifiedImageError
import os

sg.theme('dark grey 10')
layout = [
    [sg.Text("Path of the images to convert : "), sg.Input(key='-IPATH-',)],
    [sg.Text("Path where to store output :     "), sg.Input(key='-OPATH-')],
    [sg.Text("Output extension :                   "), sg.Input(key='-EXT-')],
    [sg.Text(size =(100, 1) ,key='-MSG-',text_color='red')],
    [sg.Button('Submit'), sg.Button('Exit')]
]

size = (600, 270)
title = 'Image converter'
icon='./icon.ico'

window = sg.Window(title, layout, icon= icon, resizable=True, size= size, element_padding=(9, 15))


def converter(origin_folder, output_folder, extension):
    try:     
        img = Image.open(f'{origin_folder}/{filename}')
        clean_name = os.path.splitext(filename)[0]

        if not os.path.splitext(filename)[1] == f'.{extension}' and not os.path.isdir(f'{origin_folder}\\{filename}'):
            os.chmod(f'{origin_folder}\\{filename}', 755)
            img.save(f'{output_folder}\\{clean_name}.{extension}')
        sg.Print('Done !!!')
    except UnidentifiedImageError:
        sg.Print('There was an error processing images: cannot identify image file')
    except ValueError:
        sg.Print('Unknown file extension')
    except PermissionError:
        sg.Print('Permission Error')

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
        for filename in os.listdir(origin):
           converter(origin, output, ext)

    except FileNotFoundError:
        window['-MSG-'].update('Directory not found !')
        

window.close()
    

