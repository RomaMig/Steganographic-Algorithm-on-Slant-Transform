import math
from abc import ABC, abstractmethod


class StegoAlgorithm(ABC):

    code_channel = {'0': [0], '1': [1], '2': [2], '3': [0, 1], '4': [0, 2], '5': [1, 2], '6': [0, 1, 2]}
    block_size = [[4, 8], [4, 16], [8, 4], [8, 8], [8, 16], [16, 4], [16, 8], [16, 16]]
    capacity_of_block_size = [11, 19, 10, 15, 23, 10, 22, 31]
    ph, pl = 1, 1900
    limits = [[ph * 3 / 7, pl * 0.5],
              [ph * 2, pl * 0.8],
              [ph * 2 / 7, pl * 0.7],
              [ph, pl],
              [ph * 7 / 3, pl * 1.43],
              [ph * 2.7, pl * 0.99],
              [ph * 6.7, pl * 1.63],
              [ph * 14.26, pl * 2.55]]
    high_freq = [[], [], [], [], [], [], [], []]
    mid_freq = [[], [], [], [], [], [], [], []]
    low_freq = [[], [], [], [], [], [], [], []]
    for n in range(len(block_size)):
        h = block_size[n][0]
        w = block_size[n][1]
        k = h / w * -1
        b = h - 1
        for i in range(h):
            for j in range(w):
                p = k * j + b
                md = math.ceil(p)
                mdd = math.ceil(p - k)
                if i == md or i == mdd or i - 1 == p:
                    mid_freq[n].append([i, j])
                elif i < md:
                    if i + j != 0:
                        low_freq[n].append([i, j])
                else:
                    high_freq[n].append([i, j])
    del n, i, j, k, h, w, b, p, md, mdd

    @classmethod
    @abstractmethod
    def set_code_message(cls, image, byte_text, key, threshold, embedding, trans_forward, trans_inverse, cascading_code_params):
        pass

    @classmethod
    @abstractmethod
    def get_code_message(cls, image, key, extraction, trans_forward, cascading_code_params):
        pass

    @classmethod
    @abstractmethod
    def _check_container(cls, image, binary_text, key):
        # here must be container checker
        pass

    class ContainerOverflow(Exception):
        def __init__(self, info):
            self.info = info
