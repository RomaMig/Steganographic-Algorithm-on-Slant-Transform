import base64
import math
import os
import random

from pathlib import Path
from PySide6.QtCore import QRunnable, Slot
from PySide6.QtWidgets import QDialog, QFileDialog
from ui.key_params import Ui_KeyParams
from ui.custom_dialog import CustomDialog
from stego_algorithms.enhanced_algorithm import EnhancedAlgorithm
from utilities.binary_operations import bitstring_to_bytes


class KeyParams(QDialog):
    def __init__(self):
        super(KeyParams, self).__init__()
        self.ui = Ui_KeyParams()
        self.ui.setupUi(self)
        self.initUI()
        self.__bit_keys = [1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 4, 5, 128, 128, 128, 128, 128, 128]
        self.__key_offsets = [0, 4, 12, 17, 18]
        self.key_size = sum(self.__bit_keys)
        self.keycode = None
        self.byte_key = None

    def initUI(self):
        self.ui.randomSequenceKey.pressed.connect(self.random_sequence_key)
        self.ui.readKey.pressed.connect(self.read_key_from_file)
        self.ui.save_key.pressed.connect(self.save_key)

    def read_key_from_file(self):
        cwd_dir = str(Path.cwd()) + '/stego_imgs/'
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', cwd_dir, 'Text (*.txt)')

        if file_name:
            try:
                with open(file_name, encoding='utf-8', mode='r') as key:
                    self.set_key(key.read())
            except Exception as err:
                dlg = CustomDialog(str(err))
                dlg.exec()
                return

    def save_key(self):
        if self.ui.sequenceKey.toPlainText() == '':
            dlg = CustomDialog("Отсутствует ключ для сохранения")
            dlg.exec()
            return

        cwd_dir = str(Path.cwd())
        dir = QFileDialog.getExistingDirectory(self, 'Выберите папку', cwd_dir)

        if dir:
            if not os.path.isdir(dir):
                os.mkdir(dir)
            with open(dir + '/key.txt', 'w') as key_file:
                key_file.write(self.ui.sequenceKey.toPlainText())

    def random_sequence_key(self):
        num_bit = self.key_size
        bits = random.getrandbits(num_bit - sum(self.__bit_keys[self.__key_offsets[0]:self.__key_offsets[2]]))
        offset = self.__key_offsets[0]

        for i in range(self.__key_offsets[2]):
            offset += self.__bit_keys[i]
            bits |= self.keycode[i] << (num_bit - offset)

        bytes = bits.to_bytes(int(math.ceil(num_bit / 8)), byteorder='big')
        string = base64.b64encode(bytes).decode()
        self.ui.sequenceKey.setPlainText(string)
        self.set_key(string)

    def set_key(self, string_key):
        if string_key is None or len(string_key) == 0:
            raise ModuleNotFoundError('Отсутствует ключ')

        try:
            binary_key = ''.join(format(i, '0%xb' % 8) for i in
                                 bytearray(base64.b64decode(string_key.encode('utf-8'))))
        except Exception:
            raise ValueError('Ключ не соответствует требованиям')

        self.ui.sequenceKey.setPlainText(string_key)
        self.byte_key = bitstring_to_bytes(binary_key)
        self.set_key_from_string(binary_key)

    def set_key_from_string(self, string):
        offset = [0]
        for i in range(len(self.__bit_keys)):
            offset.append(offset[i] + self.__bit_keys[i])

        key_embedding = [int(string[offset[i]:offset[i + 1]], 2) for i in range(self.__key_offsets[0], self.__key_offsets[1])]
        key_cascading_code = [int(string[offset[i]:offset[i + 1]], 2) for i in range(self.__key_offsets[1], self.__key_offsets[2])]
        algorithm_args = [int(string[offset[i]:offset[i + 1]], 2) for i in range(self.__key_offsets[2], self.__key_offsets[3])]
        aes_key = [int(string[offset[i]:offset[i + 1]], 2) for i in range(self.__key_offsets[3], self.__key_offsets[4])]

        self.key = [key_embedding,
                    key_cascading_code,
                    EnhancedAlgorithm.Key(algorithm_args[0], algorithm_args[1], algorithm_args[2], algorithm_args[3],
                                          algorithm_args[4]),
                    aes_key[0]]

    def accept(self):
        self.set_key(self.ui.sequenceKey.toPlainText())
        super().accept()


class Worker(QRunnable):

    def __init__(self, func):
        super().__init__()
        self.func = func

    @Slot()  # QtCore.Slot
    def run(self):
        self.func()
