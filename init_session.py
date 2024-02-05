import base64
import os
from pathlib import Path
from PySide6.QtWidgets import QDialog, QFileDialog
from stego_algorithms.key_exchange import init_keys, embedding_key, extraction_key
from ui.init_session import Ui_initSession
from ui.custom_dialog import CustomDialog
from utilities.file_work import saveArrayAsImage, open_image_array
from utilities.crypto import convert_rsa_key_to_string, encrypt_RSA, decrypt_RSA, decrypt_key


class InitSession(QDialog):

    def __init__(self):
        super(InitSession, self).__init__()
        self.image_session_key = None
        self.public_key = None
        self.session_key = None
        self.stego_session_key = None
        self.stego_rsa = None
        self.extension = None
        self.image_rsa = None
        self.params = None
        self.load_key_params = None
        self.ui = Ui_initSession()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.ui.openImageRSA.pressed.connect(self.open_image_rsa)
        self.ui.embeddingRSA.pressed.connect(self.embedding_rsa)
        self.ui.saveRSA.pressed.connect(self.save_rsa)
        self.ui.openStegoRSA.pressed.connect(self.open_stego_rsa)
        self.ui.extractionRSA.pressed.connect(self.extraction_rsa)
        self.ui.openStegoSessionKey.pressed.connect(self.open_stego_session_key)
        self.ui.extractionSessionKey.pressed.connect(self.extraction_session_key)
        self.ui.openImageSessionKey.pressed.connect(self.open_image_session_key)
        self.ui.embeddingSessionKey.pressed.connect(self.embedding_session_key)
        self.ui.saveSessionKey.pressed.connect(self.save_session_key)

    def open_image_rsa(self):
        inf = open_image_array(self, '/imgs/')
        if inf is None:
            return
        self.image_rsa, _, self.extension = inf
        self.image_rsa = self.image_rsa[1]
        return self.image_rsa

    def embedding_rsa(self):
        if self.image_rsa is None and self.open_image_rsa() is None:
            dlg = CustomDialog('Отсутствует изображение')
            dlg.exec()
            return
        secret_code = self.ui.editPassword.text()
        if secret_code is None or len(secret_code) == 0:
            dlg = CustomDialog('Введите одноразовый пароль сессии')
            dlg.exec()
            return
        public_key, private_key = init_keys(secret_code)
        self.public_key = bytearray(public_key.exportKey(format='DER'))
        self.stego_rsa = embedding_key(self.image_rsa, self.params, self.public_key)

    def save_rsa(self):
        if not hasattr(self, 'stego_rsa') or self.stego_rsa is None:
            dlg = CustomDialog("Отсутствует стегоконтейнер")
            dlg.exec()
            return

        cwd_dir = str(Path.cwd()) + '/session/'
        dir = QFileDialog.getExistingDirectory(self, 'Выберите папку', cwd_dir)

        if dir:
            if not os.path.isdir(dir):
                os.mkdir(dir)
            saveArrayAsImage(dir + '/stego_rsa.' + self.extension, self.stego_rsa,
                             True if self.extension == 'jpg' or self.extension == 'jpeg' else False)

    def open_stego_rsa(self):
        inf = open_image_array(self, '/session/')
        if inf is None:
            return
        self.stego_rsa, _, self.extension = inf
        self.stego_rsa = self.stego_rsa[1]
        return self.stego_rsa

    def extraction_rsa(self):
        if self.stego_rsa is None and self.open_stego_rsa() is None:
            dlg = CustomDialog('Отсутствует стеганоконтейнер с открытым ключом RSA')
            dlg.exec()
            return
        self.public_key = extraction_key(self.stego_rsa, 294)
        self.ui.publicKey.setPlainText(str(convert_rsa_key_to_string(self.public_key)))

    def open_stego_session_key(self):
        inf = open_image_array(self, '/session/')
        if inf is None:
            return
        self.stego_session_key, _, self.extension = inf
        self.stego_session_key = self.stego_session_key[1]
        return self.stego_session_key

    def extraction_session_key(self):
        if self.stego_session_key is None and self.open_stego_session_key() is None:
            dlg = CustomDialog('Отсутствует стеганоконтейнер с сессионным ключом')
            dlg.exec()
            return
        secret_code = self.ui.editPassword_2.text()
        if secret_code is None or len(secret_code) == 0:
            dlg = CustomDialog('Введите одноразовый пароль сессии')
            dlg.exec()
            return
        self.session_key = extraction_key(self.stego_session_key, 256)
        self.session_key = bytearray(decrypt_RSA(self.session_key, decrypt_key(secret_code)))
        self.ui.sessionKey.setPlainText(base64.b64encode(self.session_key).decode())

    def open_image_session_key(self):
        inf = open_image_array(self, '/imgs/')
        if inf is None:
            return
        self.image_session_key, _, self.extension = inf
        self.image_session_key = self.image_session_key[1]
        return self.image_session_key

    def embedding_session_key(self):
        if self.public_key is None:
            dlg = CustomDialog('Отсутствует открытый ключ RSA')
            dlg.exec()
            return
        if self.image_session_key is None and self.open_image_session_key() is None:
            dlg = CustomDialog('Отсутствует изображение')
            dlg.exec()
            return
        key_params = self.load_key_params()
        if key_params.byte_key is None:
            dlg = CustomDialog('Отсутствует ключ')
            dlg.exec()
            return
        self.session_key = bytearray(key_params.byte_key)
        encrypt_session_key = bytearray(encrypt_RSA(self.session_key, self.public_key))
        self.stego_session_key = embedding_key(self.image_session_key, self.params, encrypt_session_key)

    def save_session_key(self):
        if not hasattr(self, 'stego_session_key') or self.stego_session_key is None:
            dlg = CustomDialog("Отсутствует стегоконтейнер")
            dlg.exec()
            return

        cwd_dir = str(Path.cwd()) + '/session/'
        dir = QFileDialog.getExistingDirectory(self, 'Выберите папку', cwd_dir)

        if dir:
            if not os.path.isdir(dir):
                os.mkdir(dir)
            saveArrayAsImage(dir + '/stego_session_key.' + self.extension, self.stego_session_key,
                             True if self.extension == 'jpg' or self.extension == 'jpeg' else False)

