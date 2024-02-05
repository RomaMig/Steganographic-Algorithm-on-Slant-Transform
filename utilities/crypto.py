from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes

header = b"header"


def get_AES_key():
    return get_random_bytes(16)


def encrypt_AES(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    cipher.update(header)

    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    return bytearray(nonce + tag + ciphertext)


def decrypt_AES(ciphertext, key):
    nonce, tag, ciphertext = ciphertext[0:16], ciphertext[16:32], ciphertext[32:]
    decrypt_cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypt_cipher.update(header)

    data = decrypt_cipher.decrypt_and_verify(ciphertext, tag)
    return bytearray(data)


def get_RSA_keys():
    private_key = RSA.generate(2048)
    public_key = private_key.public_key()
    return [public_key, private_key]


def encrypt_RSA(data, public_key):
    if isinstance(public_key, (bytes, bytearray)):
        public_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(bytearray(data))
    return ciphertext


def decrypt_RSA(ciphertext, private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    data = cipher_rsa.decrypt(ciphertext)
    return data


def encrypt_key(secret_code, key):
    encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                                   protection="scryptAndAES128-CBC")  # сейвим ключ сессии

    file_out = open("session/rsa_key.bin", "wb")
    file_out.write(encrypted_key)
    file_out.close()


def decrypt_key(secret_code):
    return RSA.import_key(open("session/rsa_key.bin", "rb").read(), passphrase=secret_code)


def convert_rsa_key_to_string(key):
    if isinstance(key, (bytes, bytearray)):
        key = RSA.import_key(key)
    return key.exportKey(format='PEM')

#
# A
# secret_code = "Unguessable"  # одноразовый пароль для сессии
# private_key = RSA.generate(2048)
# # encrypted_key = private_key.export_key(passphrase=secret_code, pkcs=8,
# #                                        protection="scryptAndAES128-CBC")  # сейвим ключ сессии
#
# public_key = private_key.public_key()
#
# # отправляем публичный ключ
# # B
# # p = public_key.exportKey(format='DER')
# # encrypt_RSA(secret_code, p)
# # q = RSA.import_key(p)
# session_key = get_random_bytes(16)
#
# cipher_rsa = PKCS1_OAEP.new(public_key)
# enc_session_key = cipher_rsa.encrypt(session_key)
#
# # отправляем сессионный ключ
# # A
#
# recipient_key = RSA.import_key(encrypted_key, passphrase=secret_code)
#
# # Encrypt the session key with the public RSA key
# cipher_rsa = PKCS1_OAEP.new(recipient_key)
# enc_session_key2 = cipher_rsa.decrypt(enc_session_key)
#
# pass
