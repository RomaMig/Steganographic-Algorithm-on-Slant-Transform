from numpy.linalg import inv
from utilities.file_work import read_list, write_list
import numpy as np
import math
import os


class Slant:
    forward = []
    inverse = []
    ones = [None]

    for n in range(1, 4):
        u = 2 ** n
        ones.append(np.zeros([u, u], dtype=float))
        for i in range(u):
            ones[n][i, i] = 1

    @classmethod
    def init(cls, source=''):
        forward_path = source + '/' + 'forward'
        inverse_path = source + '/' + 'inverse'
        if os.path.exists(forward_path) and os.path.exists(inverse_path):
            Slant.forward = read_list(forward_path)
            Slant.inverse = read_list(inverse_path)
        else:
            n4 = (4 / 2) ** 2
            n8 = (8 / 2) ** 2
            n16 = (16 / 2) ** 2

            num4 = np.arange(-n4, n4 + 1, 2)
            num8 = np.arange(-n8, n8 + 1, 2)
            num16 = np.arange(-n16, n16 + 1, 2)

            for i4 in num4:
                for i8 in num8:
                    for i16 in num16:
                        Slant.__init([i4, i8, i16])

            if not os.path.isdir(source):
                os.mkdir(source)
            write_list(forward_path, Slant.forward)
            write_list(inverse_path, Slant.inverse)

    @classmethod
    def init2(cls, source=''):
        dir = source
        forward_path = dir + 'forward'
        inverse_path = dir + 'inverse'
        if os.path.exists(forward_path) and os.path.exists(inverse_path):
            Slant.forward = read_list(forward_path)
            Slant.inverse = read_list(inverse_path)
        else:
            n4 = (4 / 2) ** 2
            n8 = (8 / 2) ** 2
            n16 = (16 / 2) ** 2

            num4 = np.arange(-n4, n4 - 2, 1)
            num8 = np.arange(-n8, n8 - 2, 4)
            num16 = np.arange(-n16, n16 - 2, 16)

            for i4 in num4:
                for i8 in num8:
                    for i16 in num16:
                        Slant.__init([i4, i8, i16])
                        delta = 3
                        step = 1.1
                        for i in range(9):
                            Slant.__init([i4 + delta, i8 + delta, i16 + delta])
                            delta = 3 / step
                            step += 0.1

            write_list(forward_path, Slant.forward)
            write_list(inverse_path, Slant.inverse)

    @classmethod
    def __init(cls, beta):
        slant = []
        islant = []
        slant.append(np.array([[1, 1], [1, -1]], dtype=float) / math.sqrt(2))

        a1 = np.array([[1, 0], [0, 0]], dtype=float)
        a2 = np.array([[0, 1], [0, 0]], dtype=float)
        a3 = np.array([[0, 0], [1, 0]], dtype=float)
        a4 = np.array([[0, 0], [0, 1]], dtype=float)

        for n in range(1, 4):
            u = 2 ** n
            u2 = u * u
            a = math.sqrt((3 * u2) / (4 * u2 - beta[n - 1]))
            b = math.sqrt((u2 - beta[n - 1]) / (4 * u2 - beta[n - 1]))
            o1 = Slant.ones[n].copy()
            o2 = Slant.ones[n].copy()
            o3 = Slant.ones[n].copy()
            o4 = Slant.ones[n].copy() * -1
            o1[0, 0] = 1
            o1[0, 1] = 0
            o1[1, 0] = a
            o1[1, 1] = b
            o2[0, 0] = 1
            o2[0, 1] = 0
            o2[1, 0] = -a
            o2[1, 1] = b
            o3[0, 0] = 0
            o3[0, 1] = 1
            o3[1, 0] = -b
            o3[1, 1] = a
            o4[0, 0] = 0
            o4[0, 1] = -1
            o4[1, 0] = b
            o4[1, 1] = a
            a0 = np.kron(a1, o1) + np.kron(a2, o2) + np.kron(a3, o3) + np.kron(a4, o4)
            slant.append((a0 @ np.kron(Slant.ones[1], slant[n - 1])) / math.sqrt(2))

        del slant[0]
        for i in range(len(slant)):
            islant.append(inv(slant[i]))

        Slant.forward.append(slant.copy())
        Slant.inverse.append(islant.copy())
        # del ones, o1, o2, o3, o4, a0, a1, a2, a3, a4, a, b, i, n, u, u2

    @classmethod
    def compute_forward(cls, block, params):
        # Assuming a square image
        n1 = block.shape[0]
        n2 = block.shape[1]
        final2DSlant = Slant.forward[params][int(math.log2(n1) - 2)] @ block @ Slant.inverse[params][int(math.log2(n2) - 2)]
        return final2DSlant

    @classmethod
    def compute_inverse(cls, block, params):
        # Assuming a square image
        n1 = block.shape[0]
        n2 = block.shape[1]
        finalInverse2DSlant = Slant.inverse[params][int(math.log2(n1) - 2)] @ block @ Slant.forward[params][int(math.log2(n2) - 2)]
        return finalInverse2DSlant
