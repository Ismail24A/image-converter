from PIL import Image, UnidentifiedImageError
import os

def converter(origin_folder: str, output_folder: str, filename: str, extension: str):
    try:     
        img = Image.open(f'{origin_folder}/{filename}')
        clean_name = os.path.splitext(filename)[0]

        if not os.path.splitext(filename)[1] == f'.{extension}' and not os.path.isdir(f'{origin_folder}\\{filename}'):
            os.chmod(f'{origin_folder}\\{filename}', 755)
            img.save(f'{output_folder}\\{clean_name}.{extension}')
        return ['Done !!!', 'white']

    except UnidentifiedImageError:
        return ['There was an error processing images: cannot identify image file', 'red']

    except ValueError:
        return ['Unknown file extension', 'red']

    except PermissionError:
        return ['Permission Error', 'red']

if __name__ == '__main__':
    converter()