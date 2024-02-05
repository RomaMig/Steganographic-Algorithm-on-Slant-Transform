import numpy as np
import numpy.random as rnd

from stego_algorithms.enhanced_algorithm import EnhancedAlgorithm
from stego_algorithms.stego_algorithm import StegoAlgorithm
from utilities.block_constructor import cut_image_on_blocks, merge_blocks_to_image
from utilities.crypto import encrypt_AES, decrypt_AES
from utilities.image_work import get_image_channel, build_image_from_channels, normalize_channel
from utilities.correcting_code import cascading_encode, cascading_decode
from transformations.slant import Slant
from abc import abstractmethod


class FastAlgorithm(EnhancedAlgorithm):

    @classmethod
    @abstractmethod
    def set_code_message(cls, image, byte_text, key, threshold, embedding, trans_forward, trans_inverse,
                         cascading_code_params, aes_key=None):
        block_widths, block_heights, num_blocks, image_channels, distribution_size, rng, rnp_distribution, rng_transform_params, rnp_transformants = EnhancedAlgorithm._init(
            image, key)

        if aes_key is not None:
            byte_text = encrypt_AES(byte_text, aes_key)
        byte_text.append(3)
        binary_array = cascading_encode(byte_text, rng, cascading_code_params)

        if not EnhancedAlgorithm._check_container(image, binary_array, num_blocks):
            raise StegoAlgorithm.ContainerOverflow('Контейнер слишком мал для входного сообщения')

        indexes = EnhancedAlgorithm._indexing(block_widths, block_heights)
        distribution = [i for i in range(distribution_size)]
        rnp_distribution.shuffle(distribution)

        bit_index = 0
        done = False

        while not done:
            if len(distribution) == 0:
                raise StegoAlgorithm.ContainerOverflow('Контейнер слишком мал для входного сообщения')
            block, transformants, transform_params, num_channel, chunk = FastAlgorithm._step(distribution, indexes,
                                                                                             block_widths,
                                                                                             block_heights,
                                                                                             image_channels,
                                                                                             rng_transform_params,
                                                                                             trans_forward,
                                                                                             rnp_transformants)

            while embedding(block, binary_array[bit_index] == 1, transformants, threshold):
                bit_index += 1
                if bit_index >= len(binary_array):
                    done = True
                    break

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
        block_widths, block_heights, num_blocks, image_channels, distribution_size, rng, rnp_distribution, rng_transform_params, rnp_transformants = EnhancedAlgorithm._init(
            image, key)

        indexes = EnhancedAlgorithm._indexing(block_widths, block_heights)
        distribution = [i for i in range(distribution_size)]
        rnp_distribution.shuffle(distribution)

        binary_array = []
        byte_text = bytearray()

        while True:
            if len(distribution) == 0:
                return byte_text
            block, transformants, transform_params, num_channel, chunk = FastAlgorithm._step(distribution, indexes,
                                                                                             block_widths,
                                                                                             block_heights,
                                                                                             image_channels,
                                                                                             rng_transform_params,
                                                                                             trans_forward,
                                                                                             rnp_transformants)

            while True:
                bit = extraction(block, transformants)
                if isinstance(bit, type(False)):
                    break

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
    def _step(cls, distribution, indexes, block_widths, block_heights, image_channels, rng_transform_params,
              trans_forward, rnp_transformants):
        block_size = {'48': 0, '416': 1, '84': 2, '88': 3, '816': 4, '164': 5, '168': 6, '1616': 7}
        block_number = distribution.pop()
        blockX, blockY = indexes[block_number // len(image_channels)]
        num_channel = int(block_number % len(image_channels))
        chunk = [blockX, blockY, 1]
        transform_params = int(rng_transform_params.random() * len(Slant.forward))
        block = cut_image_on_blocks(image_channels[num_channel], block_widths, block_heights, chunk)
        block = trans_forward(block, transform_params)

        block_codes = block_size.get(str(block_widths[blockX]) + str(block_heights[blockX][blockY]))
        transformants = StegoAlgorithm.mid_freq[block_codes].copy()
        rnp_transformants.shuffle(transformants)
        return [block, transformants, transform_params, num_channel, chunk]
