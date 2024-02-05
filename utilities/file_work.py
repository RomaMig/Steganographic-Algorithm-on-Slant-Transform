import os
from pathlib import Path

import PIL.Image as Image
import PIL.ImageQt as ImageQt
import numpy as np
import pickle
import libjpeg
from PySide6.QtWidgets import QFileDialog

from ui.custom_dialog import CustomDialog
from utilities.image_work import YCbCrtoRGB


# write list to binary file
def write_list(file_name, list):
    # store list in binary file so 'wb' mode
    with open(file_name, 'wb') as fp:
        pickle.dump(list, fp)


# Read list to memory
def read_list(file_name):
    # for reading also binary mode is important
    with open(file_name, 'rb') as fp:
        list = pickle.load(fp)
        return list


def open_image_array(context, source='', mode='r'):
    cwd_dir = str(Path.cwd()) + source
    file_name, _ = QFileDialog.getOpenFileName(context, 'Открыть файл', cwd_dir, 'Images (*.png *.jpg *.jpeg *.bmp)')

    try:
        if file_name:
            extension = file_name.split('.')[1]
            return [open_image(file_name, True if mode == 'r' and (extension == 'jpg' or extension == 'jpeg') else False),
                    file_name, extension]
        else:
            return None
    except ValueError as err:
        dlg = CustomDialog(str(err))
        dlg.exec()
        return None
    except Exception as err:
        dlg = CustomDialog(str(err))
        dlg.exec()
        return None

def open_image(path, isYCbCr):
    image = Image.open(path)  # open an image
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    try:
        if isYCbCr:
            return [ImageQt.ImageQt(image), np.array(libjpeg.decode(path))]
    except Exception as e:
        raise ValueError('Ожидалось изображение jpg формата\n' + str(e))

    array = np.array(image)
    array = array.astype(np.uint8)
    return [ImageQt.ImageQt(image), array]


def saveArrayAsImage(path, array, isYCbCr, quality=100):
    image = Image.fromarray(array.astype(np.uint8), 'YCbCr' if isYCbCr else 'RGB')

    tmp = path.split('/')
    del tmp[-1]
    dir = ''
    for d in tmp:
        dir += d + '/'
    if dir != '' and not os.path.isdir(dir):
        os.mkdir(dir)

    if isYCbCr:
        image.format = 'JPEG'
        image.save(path, quality=quality, subsampling=0)
    else:
        image.save(path)


def getImageFromArray(array, isYCbCr):
    if isYCbCr:
        image = Image.fromarray(array.astype(np.uint8), 'YCbCr')
        image.format = 'JPEG'
        image.save('tmp/thumbnail.jpg', quality=100, subsampling=0)
        image = Image.open('tmp/thumbnail.jpg')
    else:
        image = Image.fromarray(array.astype(np.uint8), 'RGB')
    return ImageQt.ImageQt(image)
