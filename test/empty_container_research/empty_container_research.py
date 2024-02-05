import numpy as np

from stego_algorithms.enhanced_algorithm import EnhancedAlgorithm
from stego_algorithms.fast_algorithm import FastAlgorithm
from stego_algorithms.stego_algorithm import StegoAlgorithm
from transformations.slant import Slant
from utilities.correcting_code import CascadingCode
from utilities.embedding import embedding_bmej
from utilities.file_work import open_image, write_list

Slant.init('slant_matrix/')
_, image = open_image('img.png', False)
byte_input = bytearray((open("text.txt", encoding='utf-8', mode='r').read()), encoding='utf-8')
key = EnhancedAlgorithm.Key(0, 0, 0, 0, 0)
cascading_code = CascadingCode(True, False, True, False, 3, 4, 2, 3)

for threshold in range(6, 25, 2):
    res = []
    try:
        fast_stego = FastAlgorithm.set_code_message(np.copy(image), byte_input.copy(), key, threshold, embedding_bmej,
                                                    Slant.compute_forward, Slant.compute_inverse,
                                                    cascading_code)

        enhanced_stego = EnhancedAlgorithm.set_code_message(np.copy(image), byte_input.copy(), key, threshold, embedding_bmej,
                                                            Slant.compute_forward, Slant.compute_inverse,
                                                            cascading_code)
    except StegoAlgorithm.ContainerOverflow:
        pass
    else:
        for blockX in range(0, image.shape[0] // 8):
            for blockY in range(0, image.shape[1] // 8):
                left = blockX * 8
                upper = blockY * 8
                grid = np.ix_(range(left, left + 8),
                              range(upper, upper + 8))
                std_image = np.std(image[grid])
                std_fast_stego = np.std(fast_stego[grid])
                std_enhanced_stego = np.std(enhanced_stego[grid])
                res.append([std_image, std_fast_stego, std_enhanced_stego])

        write_list('25data{}'.format(threshold), res)
        f = open('25data{}.txt'.format(threshold), 'w')
        f.write('СКО ориг.|СКО fast|СКО enhanced\n')
        for d in res:
            f.write('{0}|{1}|{2}\n'.format(d[0], d[1], d[2]))
