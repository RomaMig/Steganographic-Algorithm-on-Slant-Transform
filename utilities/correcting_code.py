import numpy as np
from viterbi import Viterbi
from reedsolo import RSCodec, ReedSolomonError
from utilities.binary_operations import get_byte_from_bits, access_bit


def cascading_encode(byte_text, rng, cascading_code_params):
    block_size = 8
    if not cascading_code_params.is_cascading_code:
        return [access_bit(byte_text, i) for i in range(len(byte_text) * 8)]

    if cascading_code_params.is_reedsolo:
        while len(byte_text) % cascading_code_params.code_size != 0: byte_text.append(0)
        byte_text = reedsolo_encode(byte_text, cascading_code_params.code_size, cascading_code_params.ecc_size)
        block_size *= (cascading_code_params.code_size + cascading_code_params.ecc_size)

    binary_array = [access_bit(byte_text, i) for i in range(len(byte_text) * 8)]

    if cascading_code_params.is_conv_code:
        bits = []
        for i in range(len(binary_array) // block_size):
            bits += conv_encode(binary_array[i * block_size:(i + 1) * block_size], cascading_code_params.speed_conv_code)
        binary_array = bits

    if cascading_code_params.is_spectrum_expansion:
        binary_array = spectrum_expansion(binary_array, rng, cascading_code_params.expansion)

    return binary_array


def cascading_decode(binary_array, rng, cascading_code_params):
    if not cascading_code_params.is_cascading_code:
        return get_byte_from_bits(binary_array)
    if cascading_code_params.is_spectrum_expansion:
        binary_array = spectrum_narrowing(binary_array, rng, cascading_code_params.expansion)
    if cascading_code_params.is_conv_code:
        binary_array = viterbi_decode(binary_array, cascading_code_params.speed_conv_code)
    byte_array = get_byte_from_bits(binary_array)
    if cascading_code_params.is_reedsolo:
        byte_array = reedsolo_decode(byte_array, cascading_code_params.code_size, cascading_code_params.ecc_size)
    return byte_array


def conv_encode(binary_array, speed):
    if speed == 3:
        codec = Viterbi(8, [0b11110111, 0b11011001, 0b10010101])
    elif speed == 2:
        codec = Viterbi(8, [0b11110111, 0b11011001])
    else:
        raise ValueError('Неверная скорость свёрточного кода')
    return codec.encode(np.array(binary_array))


def viterbi_decode(binary_array, speed):
    if speed == 3:
        codec = Viterbi(8, [0b11110111, 0b11011001, 0b10010101])
    elif speed == 2:
        codec = Viterbi(8, [0b11110111, 0b11011001])
    else:
        raise ValueError('Неверная скорость свёрточного кода')
    return codec.decode(binary_array)


def reedsolo_encode(byte_text, code_size, ecc_size):
    rsc = RSCodec(ecc_size)
    byte_array = bytearray()

    for i in range(len(byte_text) // code_size):
        byte_array += rsc.encode(byte_text[i * code_size:(i + 1) * code_size])

    return byte_array


def reedsolo_decode(byte_array, code_size, ecc_size):
    rsc = RSCodec(ecc_size)
    try:
        decode_bytes = rsc.decode(byte_array)
        return decode_bytes[0]
    except ReedSolomonError as err:
        print(err)
        return byte_array[0:code_size]


def spectrum_expansion(signal, rng, size):
    if size < 3:
        return signal
    output = []
    for bit in signal:
        for i in range(size):
            output.append(round(rng.random()) ^ bit)
    return output


def spectrum_narrowing(signal, rng, size):
    if size < 3:
        return signal
    output = []
    threshold = size / 2
    i = 0
    count = 0
    for bit in signal:
        if round(rng.random()) != bit:
            count += 1
        i += 1
        if i % size == 0:
            if count > threshold:
                output.append(1)
            else:
                output.append(0)
            count = 0
    return output


class CascadingCode:
    def __init__(self, is_cascading_code, is_spectrum_expansion, is_reedsolo, is_conv_code, expansion, code_size,
                 ecc_size, speed_conv_code):
        self.expansion = expansion
        self.code_size = code_size
        self.ecc_size = ecc_size
        self.speed_conv_code = speed_conv_code
        self.is_spectrum_expansion = is_spectrum_expansion
        self.is_conv_code = is_conv_code
        self.is_reedsolo = is_reedsolo
        self.is_cascading_code = is_cascading_code

    def get_block_size(self):
        if not self.is_cascading_code:
            return 1
        size = 1
        if self.is_conv_code:
            size *= self.speed_conv_code
        if self.is_reedsolo:
            size *= (self.code_size + self.ecc_size)
        if self.is_spectrum_expansion:
            size *= self.expansion
        return size
