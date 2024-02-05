import math
import numpy.random as rnd
import numpy as np
from Cryptodome.Random import get_random_bytes

from stego_algorithms.enhanced_algorithm import EnhancedAlgorithm
from transformations.slant import Slant
from stego_algorithms.stego_algorithm import StegoAlgorithm
from utilities.block_constructor import cut_image_on_blocks, merge_blocks_to_image
from utilities.correcting_code import cascading_encode, cascading_decode, CascadingCode
from utilities.crypto import encrypt_AES, decrypt_AES
from utilities.embedding import embedding_bmej, extraction_bmej
from utilities.file_work import open_image, write_list, read_list
from utilities.image_work import get_image_channel, normalize_channel, build_image_from_channels


def mse(actual, predict):
    return np.square(np.subtract(actual, predict)).mean()


def mape(actual, predict):
    return np.abs(np.divide(np.subtract(actual, predict), actual)).mean()


def getMean(block):
    sum = 0
    transformants = StegoAlgorithm.mid_freq[7].copy()
    for i in range(0, len(transformants)):
        sum += block[transformants[i][0], transformants[i][1]]
    return sum


def getDispersion(block, mean):
    sum = 0
    transformants = StegoAlgorithm.mid_freq[7].copy()
    for i in range(0, len(transformants)):
        sum += (block[transformants[i][0], transformants[i][1]] - mean) ** 2
    return sum


def set_code_message(param, image, byte_text, key, threshold, embedding, trans_forward, trans_inverse,
                     cascading_code_params, aes_key=None):
    block_size = {'48': 0, '416': 1, '84': 2, '88': 3, '816': 4, '164': 5, '168': 6, '1616': 7}
    span = [[0, 255], [0, 255], [0, 255]]
    block_widths, block_heights = __get_bound_of_blocks(image, key)
    num_blocks = sum([len(height) for height in block_heights])
    rng = rnd.Generator(rnd.PCG64DXSM(0))

    byte_text.append(3)
    if aes_key is not None:
        byte_text = encrypt_AES(byte_text, aes_key)
    binary_array = cascading_encode(byte_text, rng, cascading_code_params)

    if not _check_container(image, binary_array, num_blocks):
        raise StegoAlgorithm.ContainerOverflow('Контейнер слишком мал для входного сообщения')

    rnp_distribution = rnd.Generator(rnd.PCG64DXSM(key.distribution))
    rnp_transformants = rnd.Generator(rnd.PCG64DXSM(key.transformants))

    distribution = [i for i in range(0, num_blocks * image.shape[2])]
    rnp_distribution.shuffle(distribution)

    image_channels = [get_image_channel(image, i) for i in range(image.shape[2])]
    indexes = __indexing(block_widths, block_heights)
    bit_index = 0
    block_index = 0
    done = False

    while not done:
        if block_index >= len(distribution):
            raise StegoAlgorithm.ContainerOverflow('Контейнер слишком мал для входного сообщения')
        blockX, blockY = indexes[int(distribution[block_index] // image.shape[2])]
        num_channel = int(distribution[block_index] % image.shape[2])
        chunk = [blockX, blockY, 1]
        transform_params = param
        block = cut_image_on_blocks(image_channels[num_channel], block_widths, block_heights, chunk)
        block = trans_forward(block, transform_params)

        transformants = StegoAlgorithm.mid_freq[
            block_size.get(str(block_widths[blockX]) + str(block_heights[blockX][blockY]))].copy()
        rnp_transformants.shuffle(transformants)
        block_index += 1
        for i in range(0, len(transformants) - 2, 3):
            k = [transformants[i], transformants[i + 1], transformants[i + 2]]
            if bit_index >= len(binary_array):
                done = True
                break
            embedding(block, binary_array[bit_index] == 1, k, threshold)
            bit_index += 1

        block = trans_inverse(block, transform_params)
        block = np.round(block)
        block = normalize_channel(block, span[num_channel])

        image_channels[num_channel] = merge_blocks_to_image(image_channels[num_channel], [block],
                                                            block_widths, block_heights,
                                                            chunk=chunk)
    result_image = build_image_from_channels(image_channels)
    return result_image


def get_code_message(param, image, key, extraction, trans_forward, cascading_code_params, limit=None, aes_key=None):
    block_size = {'48': 0, '416': 1, '84': 2, '88': 3, '816': 4, '164': 5, '168': 6, '1616': 7}
    block_widths, block_heights = __get_bound_of_blocks(image, key)
    num_blocks = sum([len(height) for height in block_heights])
    binary_array = []

    rng = rnd.Generator(rnd.PCG64DXSM(0))
    rnp_distribution = rnd.Generator(rnd.PCG64DXSM(key.distribution))
    rng_transform_params = rnd.Generator(rnd.PCG64DXSM(key.transform_params))
    rnp_transformants = rnd.Generator(rnd.PCG64DXSM(key.transformants))

    distribution = [i for i in range(0, num_blocks * image.shape[2])]
    rnp_distribution.shuffle(distribution)

    image_channels = [get_image_channel(image, i) for i in range(image.shape[2])]
    indexes = __indexing(block_widths, block_heights)
    block_index = 0
    byte_text = bytearray()

    while True:
        if block_index >= len(distribution):
            return byte_text
        blockX, blockY = indexes[int(distribution[block_index] // image.shape[2])]
        num_channel = int(distribution[block_index] % image.shape[2])
        chunk = [blockX, blockY, 1]
        transform_params = param
        block = cut_image_on_blocks(image_channels[num_channel], block_widths, block_heights, chunk)
        block = trans_forward(block, transform_params)

        transformants = StegoAlgorithm.mid_freq[
            block_size.get(str(block_widths[blockX]) + str(block_heights[blockX][blockY]))].copy()
        rnp_transformants.shuffle(transformants)
        block_index += 1

        for i in range(0, len(transformants) - 2, 3):
            k = [transformants[i], transformants[i + 1], transformants[i + 2]]
            bit = extraction(block, k)
            if bit != -1:
                binary_array.append(bit)
                if len(binary_array) % (8 * cascading_code_params.get_block_size()) == 0:
                    decode_bytes = cascading_decode(binary_array, rng, cascading_code_params)
                    binary_array = []

                    if limit is not None:
                        byte_text += decode_bytes
                        if len(byte_text) >= limit:
                            return byte_text[:limit]
                    else:
                        end = decode_bytes.find(3)
                        if end == -1:
                            byte_text += decode_bytes
                        else:
                            byte_text += decode_bytes[:end]
                            if aes_key is None:
                                return byte_text
                            else:
                                try:
                                    byte_text = decrypt_AES(byte_text, aes_key)
                                    return byte_text
                                except Exception:
                                    byte_text += decode_bytes[end:]


def __get_bound_of_blocks(image, key):
    rng_width = rnd.Generator(rnd.PCG64DXSM(key.block_size_width))
    rng_height = rnd.Generator(rnd.PCG64DXSM(key.block_size_height))

    block_widths = __get_blocks_by_side([4, 8, 16], image.shape[0], rng_width)
    block_height = []

    for i in range(len(block_widths)):
        block_height.append(
            __get_blocks_by_side([8, 16] if block_widths[i] == 4 else [4, 8, 16], image.shape[1],
                                 rng_height))

    return [block_widths, block_height]


def __get_blocks_by_side(enum, side, rng):
    max_num_blocks = int(side / 4)

    block_by_side = rng.choice(enum, size=max_num_blocks).tolist()
    num_blocks = 1
    sum_by_side = sum(block_by_side[0:num_blocks])
    while sum_by_side < side:
        num_blocks += 1
        sum_by_side = sum(block_by_side[0:num_blocks])
        if sum_by_side > side:
            del block_by_side[num_blocks - 1]
            num_blocks = num_blocks - 1
            sum_by_side = sum(block_by_side[0:num_blocks])
            if sum_by_side - side < 4:
                break
    return block_by_side[0:num_blocks]


def __indexing(block_widths, block_heights):
    indexes = []
    num_blocks_w = len(block_widths)
    num_blocks_h = [len(h) for h in block_heights]
    for i in range(num_blocks_w):
        for j in range(num_blocks_h[i]):
            indexes.append([i, j])
    return indexes


def _check_container(image, binary_array, key):
    return key * (len(StegoAlgorithm.mid_freq[7]) / 3) >= len(binary_array)


def init():
    _, image = open_image('img.png', False)
    byte_input = bytearray((open("text.txt", encoding='utf-8', mode='r').read()), encoding='utf-8')
    key = EnhancedAlgorithm.Key(0, 0, 0, 0, 0)
    cascading_code = CascadingCode(False, False, False, False, 1, 4, 2, 2)

    n4 = (4 / 2) ** 2
    n8 = (8 / 2) ** 2
    n16 = (16 / 2) ** 2

    num4 = np.arange(-n4, n4 - 2, 1)
    num8 = np.arange(-n8, n8 - 2, 4)
    num16 = np.arange(-n16, n16 - 2, 16)

    size = len(byte_input)
    for threshold in range(30, 35, 2):
        res = []
        param = 0
        for i4 in num4:
            for i8 in num8:
                for i16 in num16:
                    try:
                        delta = 3
                        step = 1.1
                        stego = set_code_message(param, np.copy(image), byte_input.copy(), key, threshold, embedding_bmej,
                                                 Slant.compute_forward, Slant.compute_inverse,
                                                 cascading_code)
                        for i in range(9):
                            byte_output = get_code_message(param + i + 1, stego, key, extraction_bmej,
                                                           Slant.compute_forward,
                                                           cascading_code, limit=size)
                            err = 0
                            for b in range(size):
                                err += (byte_input[b] ^ byte_output[b]).bit_count()
                            res.append([threshold, i4, i8, i16, delta, (err / size / 8)])
                            delta = 3 / step
                            step += 0.1
                            if err == 0:
                                break
                    except Exception:
                        pass
                    finally:
                        param += 10
        write_list(f'data{threshold}', res)
    pass

Slant.init2()
init()

for threshold in range(30, 35, 2):
    data = read_list(f'data{threshold}')
    f = open(f'data{threshold}.txt', 'w')
    f.write('Порог|Угол 1|Угол 2|Угол 3|Шаг|MSE\n')
    for d in data:
        f.write('{0}|{1}|{2}|{3}|{4}|{5}\n'.format(d[0], d[1], d[2], d[3], d[4], d[5]))


# def setCodeMessage(block, binaryText, threshold, embedding):
#     l = 0
#     transformants = StegoAlgorithm.mid_freq[7].copy()
#     for i in range(0, len(transformants) - 2, 3):
#         k = [transformants[i], transformants[i + 1], transformants[i + 2]]
#         embedding(block, binaryText[l] == 1, k, threshold)
#         l += 1
#
#     return block
#
# def getCodeMessage(block, extraction):
#     binaryText = np.empty([10], dtype=int)
#
#     l = 0
#     transformants = StegoAlgorithm.mid_freq[7].copy()
#     for i in range(0, len(transformants) - 2, 3):
#         k = [transformants[i], transformants[i + 1], transformants[i + 2]]
#         bit = extraction(block, k)
#         if bit != -1:
#             binaryText[l] = bit
#             l += 1
#
#     return binaryText
