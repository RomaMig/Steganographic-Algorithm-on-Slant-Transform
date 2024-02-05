from scipy.fftpack import dct, idct


class scipyDCT:

    @classmethod
    def compute_forward(cls, block, params=None):
        for i in range(block.ndim):
            block = dct(block, axis=i, norm='ortho')
        return block

    @classmethod
    def compute_inverse(cls, block, params=None):
        for i in range(block.ndim):
            block = idct(block, axis=i, norm='ortho')
        return block
