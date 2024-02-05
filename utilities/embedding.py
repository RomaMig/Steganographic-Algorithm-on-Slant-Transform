import numpy as np
import random as rnd


def embedding_bmej(block, bit, transformants, threshold):
    if len(transformants) < 3:
        return False
    embedding_bmej_by_key(block, bit, [transformants.pop(), transformants.pop(), transformants.pop()], threshold)
    return True


def embedding_bmej_by_key(block, bit, key, threshold):
    hardline = rnd.random() * threshold / 2

    w1 = abs(block[key[0][0], key[0][1]])
    w2 = abs(block[key[1][0], key[1][1]])
    w3 = abs(block[key[2][0], key[2][1]])

    s1 = np.sign(block[key[0][0], key[0][1]])
    s2 = np.sign(block[key[1][0], key[1][1]])
    s3 = np.sign(block[key[2][0], key[2][1]])

    s1 = s1 if s1 != 0 else 1
    s2 = s2 if s2 != 0 else 1
    s3 = s3 if s3 != 0 else 1

    if not bit and max(w1, w2) + threshold > w3:
        w3 = max(w1, w2) + threshold + hardline
    elif bit and min(w1, w2) < w3 + threshold:
        if w1 < w3 + threshold + hardline:
            w1 = w3 + threshold + hardline
        if w2 < w3 + threshold + hardline:
            w2 = w3 + threshold + hardline

    block[key[0][0], key[0][1]] = s1 * w1
    block[key[1][0], key[1][1]] = s2 * w2
    block[key[2][0], key[2][1]] = s3 * w3


def extraction_bmej(block, transformants):
    if len(transformants) < 3:
        return False
    return extraction_bmej_by_key(block, [transformants.pop(), transformants.pop(), transformants.pop()])


def extraction_bmej_by_key(block, key):
    w1 = abs(block[key[0][0], key[0][1]])
    w2 = abs(block[key[1][0], key[1][1]])
    w3 = abs(block[key[2][0], key[2][1]])

    if w3 > max(w1, w2):
        return 0
    elif w3 < min(w1, w2):
        return 1
    else:
        return -1


def embedding_kj(block, bit, transformants, threshold):
    if len(transformants) < 2:
        return False
    embedding_kj_by_key(block, bit, [transformants.pop(), transformants.pop()], threshold)
    return True


def embedding_kj_by_key(block, bit, key, threshold):
    hardline = rnd.random() * threshold / 2

    w1 = abs(block[key[0][0], key[0][1]])
    w2 = abs(block[key[1][0], key[1][1]])

    s1 = np.sign(block[key[0][0], key[0][1]])
    s2 = np.sign(block[key[1][0], key[1][1]])

    s1 = s1 if s1 != 0 else 1
    s2 = s2 if s2 != 0 else 1

    if not bit and w1 - w2 <= threshold:
        w1 = w2 + threshold + hardline
    elif bit and w1 - w2 >= -threshold:
        w2 = w1 + threshold + hardline

    block[key[0][0], key[0][1]] = s1 * w1
    block[key[1][0], key[1][1]] = s2 * w2


def extraction_kj(block, transformants):
    if len(transformants) < 2:
        return False
    return extraction_kj_by_key(block, [transformants.pop(), transformants.pop()])


def extraction_kj_by_key(block, key):
    w1 = abs(block[key[0][0], key[0][1]])
    w2 = abs(block[key[1][0], key[1][1]])

    if w1 > w2:
        return 0
    elif w1 < w2:
        return 1
    else:
        return -1
