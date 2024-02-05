from stego_algorithms.fast_algorithm import FastAlgorithm
from utilities.crypto import get_RSA_keys, encrypt_key
from utilities.correcting_code import CascadingCode
from utilities.embedding import embedding_bmej, extraction_bmej
from transformations.slant import Slant
from stego_algorithms.enhanced_algorithm import EnhancedAlgorithm


def init_keys(secret_code):
    public_key, private_key = get_RSA_keys()
    encrypt_key(secret_code, private_key)
    return [public_key, private_key]

def embedding_key(image, params, key):
    embedding_key = EnhancedAlgorithm.Key(0, 0, 0, 0, 0)
    cascading_code = CascadingCode(True, False, True, True, 1, 4, 2, 2)
    session_image = FastAlgorithm.set_code_message(image, key, embedding_key, params.threshold, embedding_bmej,
                                                   Slant.compute_forward, Slant.compute_inverse,
                                                   cascading_code)
    return session_image


def extraction_key(session_image, limit):
    key = EnhancedAlgorithm.Key(0, 0, 0, 0, 0)
    cascading_code = CascadingCode(True, False, True, True, 1, 4, 2, 2)
    session_key = FastAlgorithm.get_code_message(session_image, key, extraction_bmej, Slant.compute_forward,
                                                 cascading_code, limit)
    return session_key
