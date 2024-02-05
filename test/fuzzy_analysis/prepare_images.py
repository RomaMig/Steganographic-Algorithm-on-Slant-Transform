import base64
import math
import random

import numpy as np
from os import listdir
from os.path import isfile, join

from key_params import KeyParams
from stego_algorithms.fast_algorithm import FastAlgorithm
from transformations.slant import Slant
from utilities.correcting_code import CascadingCode
from utilities.embedding import embedding_bmej
from utilities.file_work import open_image, saveArrayAsImage

__bit_keys = [1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 4, 5, 128, 128, 128, 128, 128, 128]
__key_offsets = [0, 4, 12, 17, 18]
key_size = sum(__bit_keys)


def random_sequence_key():
    num_bit = key_size
    bits = random.getrandbits(num_bit - sum(__bit_keys[__key_offsets[0]:__key_offsets[2]]))
    offset = __key_offsets[0]

    for i in range(__key_offsets[2]):
        offset += __bit_keys[i]
        bits |= 0 << (num_bit - offset)

    bytes = bits.to_bytes(int(math.ceil(num_bit / 8)), byteorder='big')
    string = base64.b64encode(bytes).decode()
    return set_key(string)


def set_key(string_key):
    if string_key is None or len(string_key) == 0:
        raise ModuleNotFoundError('Отсутствует ключ')

    try:
        binary_key = ''.join(format(i, '0%xb' % 8) for i in
                             bytearray(base64.b64decode(string_key.encode('utf-8'))))
    except Exception:
        raise ValueError('Ключ не соответствует требованиям')

    return set_key_from_string(binary_key)


def set_key_from_string(string):
    offset = [0]
    for i in range(len(__bit_keys)):
        offset.append(offset[i] + __bit_keys[i])

    key_embedding = [int(string[offset[i]:offset[i + 1]], 2) for i in range(__key_offsets[0], __key_offsets[1])]
    key_cascading_code = [int(string[offset[i]:offset[i + 1]], 2) for i in range(__key_offsets[1], __key_offsets[2])]
    algorithm_args = [int(string[offset[i]:offset[i + 1]], 2) for i in range(__key_offsets[2], __key_offsets[3])]
    aes_key = [int(string[offset[i]:offset[i + 1]], 2) for i in range(__key_offsets[3], __key_offsets[4])]

    return [key_embedding, key_cascading_code,
            FastAlgorithm.Key(algorithm_args[0], algorithm_args[1], algorithm_args[2], algorithm_args[3],
                              algorithm_args[4]), aes_key[0]]


empty = 'empty'
full = 'full'

Slant.init('slant_matrix/')
key = random_sequence_key()
cascading_code = CascadingCode(True, False, False, False, 1, 4, 0, 1)
text = open("text.txt", encoding='utf-8', mode='r').read()
byte_input = bytearray((text), encoding='utf-8')
files = [f for f in listdir(empty) if isfile(join(empty, f))]

for i in range(4128, 4128 + int(len(files) / 10)):
    _, image = open_image(f'{empty}/{files[i]}', True)
    stego = FastAlgorithm.set_code_message(image, byte_input.copy(), key[2], 6, embedding_bmej, Slant.compute_forward,
                                           Slant.compute_inverse, cascading_code)
    saveArrayAsImage(f'{full}/!!{files[i]}', stego, True, quality=98)
