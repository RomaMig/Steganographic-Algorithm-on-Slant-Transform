import math

import numpy as np
from transformations.slant import Slant
from utilities.embedding import embedding_bmej, extraction_bmej
from utilities.file_work import open_image
from utilities.image_work import get_image_channel


rng = np.random.default_rng()

block = []
msgs = []
_, image = open_image('angle_research/test2.png', False)
image = get_image_channel(image, 2)
for i in range(10):
    b = image[::, i * 16:(i + 1) * 16]
    block.append(b)
    t = rng.integers(size=(10), low=0, high=2)
    msgs.append(t)

angles = np.linspace(math.pi / 4, math.pi / 2, 5)
f = open('angle_research/data.txt', 'w')
f.write('Порог|Mean|Disp|Угол 1|Шаг 1|Угол 2|Шаг 2|Угол 3|Шаг 3|MSE\n')

for t in [0.1, 0.5, 0.75, 1, 2, 5]:
    step1 = 1.0e-4
    for n1 in range(3):
        for a1 in range(len(angles)):
            step2 = 1.0e-4
            for n2 in range(3):
                for a2 in range(len(angles)):
                    step3 = 1.0e-4
                    for n3 in range(3):
                        for a3 in range(len(angles)):
                            MSE = 0
                            mean = 0
                            disp = 0
                            for m in range(len(msgs)):
                                Slant.init_with_angle([angles[a1], angles[a2], angles[a3]], [angles[a1] + step1, angles[a2] + step2, angles[a3] + step3])

                                d = Slant.compute_forward(block[m], 0)
                                dmod = setCodeMessage(d, msgs[m], t, embedding_bmej)
                                b = Slant.compute_inverse(dmod, 0)

                                d2 = Slant.compute_forward(b, 1)
                                res = getCodeMessage(d2, extraction_bmej)
                                MSE += mse(msgs[m], res) * len(res)
                                meantmp = getMean(d2)
                                mean += meantmp
                                disp += getDispersion(d2, meantmp)

                                Slant.forward = []
                                Slant.inverse = []

                            MSE /= 100
                            mean /= 100
                            disp /= 100
                            f.write('{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}\n'.format(t, mean, disp, angles[a1], step1,
                                                                                                angles[a2], step2,
                                                                                                angles[a3], step3,
                                                                                                MSE))
                        step3 *= 10
                step2 *= 10
        step1 *= 10
f.close()
