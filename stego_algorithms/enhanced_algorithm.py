import numpy as np
import numpy.random as rnd

from stego_algorithms.stego_algorithm import StegoAlgorithm
from utilities.block_constructor import cut_image_on_blocks, merge_blocks_to_image
from utilities.crypto import encrypt_AES, decrypt_AES
from utilities.image_work import get_image_channel, build_image_from_channels, normalize_channel
from utilities.correcting_code import cascading_encode, cascading_decode
from transformations.slant import Slant
from abc import abstractmethod


class EnhancedAlgorithm(StegoAlgorithm):

    @classmethod
    @abstractmethod
    def set_code_message(cls, image, byte_text, key, threshold, embedding, trans_forward, trans_inverse,
                         cascading_code_params, aes_key=None):
        block_widths, block_heights, num_blocks, image_channels, distribution_size, rng, rng_distribution, rng_transform_params, rnp_transformants = EnhancedAlgorithm._init(
            image, key)

        if aes_key is not None:
            byte_text = encrypt_AES(byte_text, aes_key)
        byte_text.append(3)
        binary_array = cascading_encode(byte_text, rng, cascading_code_params)

        if not EnhancedAlgorithm._check_container(image, binary_array, num_blocks):
            raise StegoAlgorithm.ContainerOverflow('Контейнер слишком мал для входного сообщения')

        indexes, distribution, transformants = EnhancedAlgorithm.__prepare_data(block_widths, block_heights,
                                                                                distribution_size, rnp_transformants)
        bit_index = 0
        transform_image = dict()

        while True:
            if bit_index >= len(binary_array):
                break
            if len(distribution) == 0:
                raise StegoAlgorithm.ContainerOverflow('Контейнер слишком мал для входного сообщения')
            block_number = rng_distribution.choice(distribution)
            if block_number not in transform_image:
                transform_image[block_number] = EnhancedAlgorithm._step(block_number, indexes, block_widths,
                                                                        block_heights, image_channels,
                                                                        rng_transform_params, trans_forward)

            if embedding(transform_image[block_number][0], binary_array[bit_index] == 1, transformants[block_number],
                         threshold):
                bit_index += 1
            else:
                distribution.remove(block_number)

        for block_number in transform_image:
            block, transform_params, num_channel, chunk = transform_image[block_number]
            block = trans_inverse(block, transform_params)
            block = np.round(block)
            block = normalize_channel(block)
            image_channels[num_channel] = merge_blocks_to_image(image_channels[num_channel], [block],
                                                                block_widths, block_heights,
                                                                chunk=chunk)

        result_image = build_image_from_channels(image_channels)
        return result_image

    @classmethod
    @abstractmethod
    def get_code_message(cls, image, key, extraction, trans_forward, cascading_code_params, limit=None, aes_key=None):
        block_widths, block_heights, num_blocks, image_channels, distribution_size, rng, rng_distribution, rng_transform_params, rnp_transformants = EnhancedAlgorithm._init(
            image, key)
        indexes, distribution, transformants = EnhancedAlgorithm.__prepare_data(block_widths, block_heights,
                                                                                distribution_size, rnp_transformants)

        binary_array = []
        byte_text = bytearray()
        transform_image = dict()

        while True:
            if len(distribution) == 0:
                return byte_text
            block_number = rng_distribution.choice(distribution)
            if block_number not in transform_image:
                transform_image[block_number] = EnhancedAlgorithm._step(block_number, indexes, block_widths,
                                                                        block_heights, image_channels,
                                                                        rng_transform_params, trans_forward)

            bit = extraction(transform_image[block_number][0], transformants[block_number])
            if isinstance(bit, type(False)):
                distribution.remove(block_number)
                continue

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

    @classmethod
    def _init(cls, image, key):
        block_widths, block_heights = EnhancedAlgorithm._get_bound_of_blocks(image, key)
        num_blocks = sum([len(height) for height in block_heights])
        num_channels = image.shape[2]
        distribution_size = num_blocks * num_channels

        rng = rnd.Generator(rnd.PCG64DXSM(0))
        rng_distribution = rnd.Generator(rnd.PCG64DXSM(key.distribution))
        rng_transform_params = rnd.Generator(rnd.PCG64DXSM(key.transform_params))
        rnp_transformants = rnd.Generator(rnd.PCG64DXSM(key.transformants))

        image_channels = [get_image_channel(image, i) for i in range(num_channels)]
        return [block_widths, block_heights, num_blocks, image_channels, distribution_size, rng, rng_distribution,
                rng_transform_params, rnp_transformants]

    @classmethod
    def _step(cls, block_number, indexes, block_widths, block_heights, image_channels, rng_transform_params,
              trans_forward):
        blockX, blockY = indexes[block_number // len(image_channels)]
        num_channel = int(block_number % len(image_channels))
        chunk = [blockX, blockY, 1]
        transform_params = int(rng_transform_params.random() * len(Slant.forward))
        block = cut_image_on_blocks(image_channels[num_channel], block_widths, block_heights, chunk)
        block = trans_forward(block, transform_params)
        return [block, transform_params, num_channel, chunk]

    @classmethod
    def __prepare_data(cls, block_widths, block_heights, distribution_size, rnp_transformants):
        block_size = {'48': 0, '416': 1, '84': 2, '88': 3, '816': 4, '164': 5, '168': 6, '1616': 7}
        indexes = EnhancedAlgorithm._indexing(block_widths, block_heights)
        num_channel = distribution_size // len(indexes)
        distribution = [i for i in range(distribution_size)]
        block_codes = [
            block_size.get(str(block_widths[indexes[i][0]]) + str(block_heights[indexes[i][0]][indexes[i][1]])) for i in
            range(0, len(indexes))]
        transformants = [StegoAlgorithm.mid_freq[block_codes[i // num_channel]].copy() for i in
                         range(0, distribution_size)]
        for block_number in range(distribution_size):
            rnp_transformants.shuffle(transformants[block_number])
        return [indexes, distribution, transformants]

    @classmethod
    def _get_bound_of_blocks(cls, image, key):
        rng_width = rnd.Generator(rnd.PCG64DXSM(key.block_size_width))
        rng_height = rnd.Generator(rnd.PCG64DXSM(key.block_size_height))

        block_widths = EnhancedAlgorithm._get_blocks_by_side([4, 8, 16], image.shape[0], rng_width)
        block_height = []

        for i in range(len(block_widths)):
            block_height.append(
                EnhancedAlgorithm._get_blocks_by_side([8, 16] if block_widths[i] == 4 else [4, 8, 16], image.shape[1],
                                                      rng_height))

        return [block_widths, block_height]

    @classmethod
    def _get_blocks_by_side(cls, enum, side, rng):
        length = 0
        block_by_side = []

        while length < side:
            value = rng.choice(enum)
            block_by_side.append(value)
            length += value

        if length > side:
            del block_by_side[-1]
        return block_by_side

    @classmethod
    def _indexing(cls, block_widths, block_heights):
        indexes = []
        num_blocks_w = len(block_widths)
        num_blocks_h = [len(h) for h in block_heights]
        for i in range(num_blocks_w):
            for j in range(num_blocks_h[i]):
                indexes.append([i, j])
        return indexes

    @classmethod
    @abstractmethod
    def _check_container(cls, image, binary_array, num_blocks):
        return num_blocks * (len(StegoAlgorithm.mid_freq[7]) // 2) >= len(binary_array)

    class Key:
        def __init__(self, distribution, block_size_width, block_size_height, transformants, transform_params):
            self.distribution = distribution
            self.block_size_width = block_size_width
            self.block_size_height = block_size_height
            self.transformants = transformants
            self.transform_params = transform_params
