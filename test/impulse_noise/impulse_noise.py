import math
import random
import numpy as np

from stego_algorithms.fast_algorithm import FastAlgorithm
from stego_algorithms.stego_algorithm import StegoAlgorithm
from transformations.slant import Slant
from utilities.correcting_code import CascadingCode
from utilities.embedding import embedding_bmej, extraction_bmej
from utilities.file_work import open_image, saveArrayAsImage, write_list
from utilities.image_work import RGBtoYCbCr

def imnoise(image:np.ndarray, density):
    pixels = [(i, j, k) for k in range(image.shape[2]) for j in range(image.shape[1]) for i in range(image.shape[0])]
    pixels = random.choices(pixels, k=math.ceil(image.size * density))
    for pixel in pixels:
        image[pixel] = 255 if random.random() >= 0.5 else 0
    return image

Slant.init('slant_matrix/')
_, image = open_image('img.png', False)
byte_input = bytearray((open("text.txt", encoding='utf-8', mode='r').read()), encoding='utf-8')
length = len(byte_input)
key = FastAlgorithm.Key(0, 0, 0, 0, 0)
res = []
for ecc in [0, 2, 4, 6]:
    for expansion in [1, 3, 5]:
        for speed in [1, 2, 3]:
            cascading_code = CascadingCode(ecc != 0 or expansion * speed != 1, expansion != 1, ecc != 0, speed != 1,
                                           expansion, 4, ecc, speed)
            for threshold in range(4, 35, 2):
                try:
                    stego = FastAlgorithm.set_code_message(np.copy(image), byte_input.copy(), key, threshold,
                                                           embedding_bmej,
                                                           Slant.compute_forward,
                                                           Slant.compute_inverse,
                                                           cascading_code)
                except StegoAlgorithm.ContainerOverflow:
                    pass
                else:
                    for q in [0.001]:
                        s = imnoise(np.copy(stego), q)
                        saveArrayAsImage('imgs/tmp{0}_{1}_{2}_{3}_{4}.png'.format(q, threshold, speed, expansion, ecc), s, False)
                        byte_output = FastAlgorithm.get_code_message(s, key, extraction_bmej,
                                                                     Slant.compute_forward,
                                                                     cascading_code, limit=length)
                        err = 0
                        for b in range(min(len(byte_input), len(byte_output))):
                            err += (byte_input[b] ^ byte_output[b]).bit_count()
                        res.append(
                            [threshold, expansion, speed, ecc, q, len(byte_input) * speed * expansion * (1 + ecc / 4),
                             'Да' if byte_input == byte_output else 'Нет', (err / length / 8)])

write_list('data', res)
f = open('data.txt', 'w')
f.write('Порог|Расширение|Скорость кода|Длинна кор. блока|Плотность шума|Длинна|Пригодно|MSE\n')
for d in res:
    f.write('{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}\n'.format(d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7]))
