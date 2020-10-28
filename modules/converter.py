from PIL import Image, UnidentifiedImageError
import os

def converter(origin_folder, output_folder, filename, extension):
    try:     
        img = Image.open(f'{origin_folder}/{filename}')
        clean_name = os.path.splitext(filename)[0]

        if not os.path.splitext(filename)[1] == f'.{extension}' and not os.path.isdir(f'{origin_folder}\\{filename}'):
            os.chmod(f'{origin_folder}\\{filename}', 755)
            img.save(f'{output_folder}\\{clean_name}.{extension}')
        return 'Done !!!'
    except UnidentifiedImageError:
        return 'There was an error processing images: cannot identify image file'
    except ValueError:
        return 'Unknown file extension'
    except PermissionError:
        return 'Permission Error'

if __name__ == '__main__':
    converter()