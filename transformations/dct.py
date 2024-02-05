from scipy.fftpack import dct, idct
import numpy as np
import math


class DCT:

    @classmethod
    def __computeSinglePoint1DCT(cls, signal, u, N):

        result = 0

        for x in range(N):
            result += signal[x] * math.cos(((2 * x + 1) * u * math.pi) / (2 * N))

        if u == 0:
            result = result / math.sqrt(N)
        else:
            result = result * math.sqrt(2.0 / N)

        return result

    @classmethod
    def __computeSinglePointInverse1DCT(cls, signal, x, N):

        result = 0

        for u in range(N):
            if u == 0:
                tau = 1.0 / math.sqrt(N)
            else:
                tau = math.sqrt(2.0 / N)

            result += tau * signal[u] * math.cos(((2 * x + 1) * u * math.pi) / (2 * N))
        return result

    @classmethod
    def __computeSinglePoint2DCT(cls, image, u, v, N):

        result = 0

        for x in range(N):
            for y in range(N):
                result += image[x, y] * math.cos(((2 * x + 1) * u * math.pi) / (2 * N)) * math.cos(
                    ((2 * y + 1) * v * math.pi) / (2 * N))

        # Add the tau value to the result
        if (u == 0) and (v == 0):
            result = result / N
        elif (u == 0) or (v == 0):
            result = (math.sqrt(2.0) * result) / N
        else:
            result = (2.0 * result) / N

        return result

    @classmethod
    def __computeSinglePointInverse2DCT(cls, image, x, y, N):

        result = 0

        for u in range(N):
            for v in range(N):
                if (u == 0) and (v == 0):
                    tau = 1.0 / N
                elif (u == 0) or (v == 0):
                    tau = math.sqrt(2.0) / N
                else:
                    tau = 2.0 / N
                result += tau * image[u, v] * math.cos(((2 * x + 1) * u * math.pi) / (2 * N)) * math.cos(
                    ((2 * y + 1) * v * math.pi) / (2 * N))

        return result

    @classmethod
    def computeForward2DCT(cls, block):
        # Assuming a square image
        N = block.shape[0]
        final2DDCT = np.zeros([N, N], dtype=float)
        for u in range(N):
            for v in range(N):
                # Compute the DCT value for each cells/points in the resulting transformed image.
                final2DDCT[u, v] = DCT.__computeSinglePoint2DCT(block, u, v, N)
        return final2DDCT

    @classmethod
    def computeInverse2DCT(cls, block):
        # Assuming a square image
        N = block.shape[0]
        finalInverse2DDCT = np.zeros([N, N], dtype=float)
        for x in range(N):
            for y in range(N):
                # Compute the DCT value for each cells/points in the resulting transformed image.
                finalInverse2DDCT[x, y] = DCT.__computeSinglePointInverse2DCT(block, x, y, N)
        return finalInverse2DDCT

    @classmethod
    def computeForward1DCT(cls, block):
        N = block.shape[0]
        M = block.shape[1]
        size = N * M
        signal = block.reshape(size)
        final1DDCT = np.zeros([N, M], dtype=float)
        for u in range(N):
            for v in range(M):
                final1DDCT[u, v] = DCT.__computeSinglePoint1DCT(signal, u * M + v, size)
        return final1DDCT

    @classmethod
    def computeInverse1DCT(cls, block):
        N = block.shape[0]
        M = block.shape[1]
        size = N * M
        signal = block.reshape(size)
        finalInverse1DDCT = np.zeros([N, M], dtype=float)
        for x in range(N):
            for y in range(M):
                finalInverse1DDCT[x, y] = DCT.__computeSinglePointInverse1DCT(signal, x * M + y, size)
        return finalInverse1DDCT

    @classmethod
    def scipyForward2DCT(cls, block):
        for i in range(block.ndim):
            block = dct(block, axis=i, norm='ortho')
        return block

    @classmethod
    def scipyInverse2DCT(cls, block):
        for i in range(block.ndim):
            block = idct(block, axis=i, norm='ortho')
        return block
