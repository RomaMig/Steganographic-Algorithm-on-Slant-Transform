import random
import sys
import time
import os
import matplotlib
import matplotlib.pyplot as plt

from transformations.scipy_dct import scipyDCT

matplotlib.use('QtAgg')

from init_session import InitSession
from transformations.slant import Slant
from stego_algorithms.fast_algorithm import FastAlgorithm
from stego_algorithms.stego_algorithm import StegoAlgorithm
from stego_algorithms.enhanced_algorithm import EnhancedAlgorithm
from utilities.image_work import RGBtoYCbCr
from utilities.file_work import *
from utilities.embedding import embedding_kj, embedding_bmej, extraction_kj, extraction_bmej
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog
from ui.main import Ui_MainWindow
from ui.custom_dialog import CustomDialog
from key_params import KeyParams
from cascading_code_params import CascadingCodeParams


class ExpenseTracker(QMainWindow):

    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.key_params = KeyParams()
        self.cascading_code = CascadingCodeParams()
        self.init_session = InitSession()
        self.extension = None
        self.scr = 1
        self.scw = 1
        Slant.init('slant_matrix/')
        self.initUI()

    def initUI(self):
        self.ui.openImage.pressed.connect(self.open_image_from_file)
        self.ui.openSteganogramm.pressed.connect(self.open_steganogramm_from_file)
        self.ui.openMessage.pressed.connect(self.open_text_file)
        self.ui.readStego.pressed.connect(self.read_steganogramm)
        self.ui.saveSteganogramm.pressed.connect(self.save_steganogramm_to_file)
        self.ui.transform.pressed.connect(self.transform)
        self.ui.toPlot.pressed.connect(self.open_to_plot)
        self.ui.setKeyParams.pressed.connect(self.set_key_params)
        self.ui.question.pressed.connect(self.get_answer)
        self.ui.setKeyParams_2.pressed.connect(self.set_key_params)
        self.ui.openCascadingCode.pressed.connect(self.open_cascading_code)
        self.ui.startSession.pressed.connect(self.start_session)
        self.ui.checkContainer.pressed.connect(self.check_container)

    def transform(self):
        start = time.time()
        try:
            params, byte_text = self.prepare_to_transform()
            key, params = self.prepare_key(params, mode='w')

            self.ui.progressBar.setValue(17)
            if params.isYCbCr:
                ready_image = RGBtoYCbCr(self.originalImage[1])
            else:
                ready_image = self.originalImage[1]

            self.ui.state.setText('Встраивание...')
            self.ui.progressBar.setValue(20)
            transformImage = params.algorithm.set_code_message(ready_image.copy(), byte_text, key[2], params.threshold,
                                                               params.embedding, params.transform.compute_forward,
                                                               params.transform.compute_inverse,
                                                               self.cascading_code.cascading_code_params)#, aes_key=key[3].to_bytes(16, byteorder='big'))

            self.ui.progressBar.setValue(78)
        except StegoAlgorithm.ContainerOverflow as co:
            self.ui.state.setText(co.info)
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog(co.info)
            dlg.exec()
            return

        except UnicodeEncodeError as uee:
            self.ui.state.setText('Проверьте корректность кодировки')
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog('Проверьте корректность кодировки\n' + str(uee))
            dlg.exec()
            return

        except Exception as err:
            self.ui.state.setText(str(err))
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog(str(err))
            dlg.exec()
        else:
            self.ui.progressBar.setValue(98)
            self.transformImage = [getImageFromArray(transformImage, params.isYCbCr), transformImage]
            self.scw = self.__set_picture(self.ui.transformImage, self.transformImage[0], self.scw)
            self.ui.label_trans_img.setText('Изображение-стегоконтейнер:')
            self.ui.state.setText('Встраивание произведено успешно!')
            dlg = CustomDialog("Встраивание сообщения проведено!")
            dlg.exec()
            self.ui.progressBar.setValue(100)
        end = time.time()
        print("The time of embedding is:", (end - start) * 10 ** 3, "ms")

    def get_text_from_image(self, image, params=None):
        try:
            self.ui.progressBar.setValue(5)
            self.ui.state.setText('Подготовка')
            if params is None:
                params = self.get_params(mode='r')
                if params is None:
                    self.ui.state.setText('Не удалось считать параметры')
                    self.ui.progressBar.setValue(0)
                    return

            key, params = self.prepare_key(params, mode='r')

            self.ui.state.setText('Извлечение...')
            self.ui.progressBar.setValue(17)

            byte_text = params.algorithm.get_code_message(image, key[2], params.extraction, params.transform.compute_forward,
                                                          self.cascading_code.cascading_code_params)#, aes_key=key[3].to_bytes(16, byteorder='big'))
            text = ''.join(byte_text.decode(params.encoding))
            self.ui.progressBar.setValue(80)
        except Exception as err:
            self.ui.state.setText('Ошибка чтения стеганограммы')
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog('Ошибка чтения стеганограммы\n' + str(err))
            dlg.exec()
            return

        self.ui.progressBar.setValue(90)
        self.ui.state.setText('Вывод сообщения')
        self.ui.receivedMessage.setPlainText(text)
        self.ui.state.setText('Извлечение произведено успешно!')
        dlg = CustomDialog("Извлечение сообщения проведено!")
        dlg.exec()
        self.ui.progressBar.setValue(100)

    def check_container(self):
        try:
            params, byte_input = self.prepare_to_transform()
            key, params = self.prepare_key(params, mode='w')
            length = len(byte_input)

            self.ui.progressBar.setValue(17)
            if params.isYCbCr:
                ready_image = RGBtoYCbCr(self.originalImage[1])
            else:
                dlg = CustomDialog('Данная функция проверяет стойкость к сжатию jpg и jpeg контейнеров.\n'
                                   'Предложенные параметры встраивания не позволят сохранить контейнер в формате jpg или jpeg')
                dlg.exec()
                self.ui.progressBar.setValue(0)
                self.ui.state.setText('')
                return

            self.ui.state.setText('Встраивание...')
            self.ui.progressBar.setValue(20)
            stego = params.algorithm.set_code_message(ready_image.copy(), byte_input, key[2], params.threshold,
                                                               params.embedding, params.transform.compute_forward,
                                                               params.transform.compute_inverse,
                                                               self.cascading_code.cascading_code_params)
            self.ui.progressBar.setValue(68)
            saveArrayAsImage('tmp/tmp_check.jpg', stego, True, quality=98)
            _, s = open_image('tmp/tmp_check.jpg', True)

            self.ui.state.setText('Извлечение...')
            byte_output = params.algorithm.get_code_message(s, key[2], params.extraction,
                                                          params.transform.compute_forward,
                                                          self.cascading_code.cascading_code_params, limit=length)
            self.ui.progressBar.setValue(95)
        except StegoAlgorithm.ContainerOverflow as co:
            self.ui.state.setText(co.info)
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog(co.info)
            dlg.exec()
            return

        except UnicodeEncodeError as uee:
            self.ui.state.setText('Проверьте корректность кодировки')
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog('Проверьте корректность кодировки\n' + str(uee))
            dlg.exec()
            return

        except Exception as err:
            self.ui.state.setText(str(err))
            self.ui.progressBar.setValue(0)
            dlg = CustomDialog(str(err))
            dlg.exec()
        else:
            err = 0
            for b in range(min(len(byte_input), len(byte_output))):
                err += (byte_input[b] ^ byte_output[b]).bit_count()

            if err == 0:
                info = 'Контейнер пригоден'
            else:
                info = f'Контейнер непригоден. Процент ошибочно принятых битов: {(err / length / 8):.2%}'
            self.ui.progressBar.setValue(100)
            self.ui.state.setText(info)
            dlg = CustomDialog(info)
            dlg.exec()

    '''
    Управление параметрами
    '''

    class Params:
        def __init__(self, algorithm, isYCbCr, threshold, embedding, extraction, transform,
                     encoding):
            self.algorithm = algorithm
            self.isYCbCr = isYCbCr
            self.threshold = threshold
            self.embedding = embedding
            self.extraction = extraction
            self.transform = transform
            self.encoding = encoding

    def get_params(self, mode='w'):
        transforms = {'DCT 2D': scipyDCT,
                      'Slant': Slant,
                      'Авто': None}
        algorithms = {'Fast': FastAlgorithm,
                      'Enhanced': EnhancedAlgorithm,
                      'Авто': None}
        embeddings = {'Коха-Жао': [embedding_kj, extraction_kj],
                      'Бенгама-Мемона ...': [embedding_bmej, extraction_bmej],
                      'Авто': [None, None]}

        if mode == 'r':
            encoding = self.ui.selectEncode_2.currentText()
            transform = None
            isYCbCr = None
            embedding = [None, None]
            algorithm = None
        else:
            encoding = self.ui.selectEncode.currentText()
            isYCbCr = self.ui.checkYCbCr.isChecked()
            transform = transforms.get(self.ui.selectTransform.currentText())
            embedding = embeddings.get(self.ui.selectEmbadding.currentText())
            algorithm = algorithms.get(self.ui.selectAlgorithm.currentText())
        threshold = self.ui.setThreshold.text()
        threshold = float(threshold.replace(',', '.'))

        return self.Params(algorithm, isYCbCr, threshold, embedding[0], embedding[1], transform,
                           encoding)

    '''
    Функции, управляющие поведением интерфейса
    '''

    def open_to_plot(self):
        if not (hasattr(self, 'originalImage') and hasattr(self, 'transformImage')):
            dlg = CustomDialog("Отсутствуют изображения")
            dlg.exec()
            return

        fig, (ax1, ax2) = plt.subplots(1, 2)

        ax1.imshow(self.originalImage[1].astype(np.uint8))
        ax1.set_title('Изображение-контейнер')

        ax2.imshow(self.transformImage[1].astype(np.uint8))
        ax2.set_title('Изображение-стегоконтейнер')

        plt.show()

    def open_image_from_file(self):
        inf = open_image_array(self, '/imgs/', 'w')
        if inf is None:
            return
        self.originalImage, file_name, self.extension = inf
        self.ui.image_path_box.setPlainText(file_name)
        self.scw = self.__set_picture(self.ui.transformImage, self.originalImage[0], self.scw)
        self.ui.label_trans_img.setText('Изображение-контейнер:')

    def open_steganogramm_from_file(self):
        cwd_dir = str(Path.cwd()) + '/stego_imgs/'
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть стегоконтейнер', cwd_dir,
                                                   'Images (*.png *.jpg *.jpeg *.bmp)')

        try:
            if file_name:
                tmp = file_name.split('/')
                del tmp[-1]
                dir = ''
                for d in tmp:
                    dir += d + '/'
                with open(dir + 'key.txt', 'r') as key_file:
                    self.key_params.set_key(key_file.read())
                self.ui.stego_path_box.setPlainText(file_name)
                self.stegoImage = open_image(file_name, self.key_params.key[0][0] == 1)
                self.scr = self.__set_picture(self.ui.stegoImage, self.stegoImage[0], self.scr)
                self.ui.label_stego_img.setText('Изображение-стегоконтейнер:')
        except (ModuleNotFoundError, ValueError) as err:
            dlg = CustomDialog(str(err))
            dlg.exec()
            self.key_params.exec()
        except Exception as err:
            dlg = CustomDialog(str(err))
            dlg.exec()

    def open_text_file(self):
        cwd_dir = str(Path.cwd()) + "/msg/"
        file_name, _ = QFileDialog.getOpenFileName(self, 'Открыть файл ключа', cwd_dir, 'Text (*.txt)')

        if file_name:
            self.ui.file_path_box.setPlainText(file_name)
            with open(file_name, encoding='utf-8', mode='r') as text_file:
                self.ui.sendingMessage.setPlainText(text_file.read())

    def save_steganogramm_to_file(self):
        if not hasattr(self, 'transformImage'):
            dlg = CustomDialog("Отсутствует стегоконтейнер")
            dlg.exec()
            return

        cwd_dir = str(Path.cwd()) + '/stego_imgs/'
        dir = QFileDialog.getExistingDirectory(self, 'Выберите папку', cwd_dir)

        if dir:
            if not os.path.isdir(dir):
                os.mkdir(dir)
            dir += '/' + str(int(random.random() * 1.e7))
            done = False
            while not done:
                try:
                    os.mkdir(dir)
                    done = True
                except FileExistsError:
                    dir += '/' + str(int(random.random() * 1.e7))
                except FileNotFoundError:
                    dlg = CustomDialog("Папка не найдена\nСохранение не удалось")
                    dlg.exec()
                    return

            if self.key_params.ui.sequenceKey.toPlainText() == '':
                dlg = CustomDialog("Отсутствует ключ для сохранения\nБудет сохранен только стегоконтейнер")
                dlg.exec()
                saveArrayAsImage(dir + '/img.' + self.extension, self.transformImage[1],
                                 True if self.extension == 'jpg' or self.extension == 'jpeg' else False)
            else:
                with open(dir + '/key.txt', 'w') as key_file:
                    key_file.write(self.key_params.ui.sequenceKey.toPlainText())
                saveArrayAsImage(dir + '/img.' + ('jpg' if self.key_params.key[0][0] == 1 else self.extension),
                                 self.transformImage[1], self.key_params.key[0][0] == 1)

    def set_key_params(self):
        params = self.get_params('w')
        self.key_params.keycode = self.get_key_embedding(params) + self.cascading_code.get_keycode()
        self.key_params.exec()
        if hasattr(self.key_params, 'key'):
            params = self.update_params_from_keycode(params, self.key_params.key[0], self.key_params.key[1])
            self.update_params_interface(params)
        return self.key_params

    def open_cascading_code(self):
        self.cascading_code.exec()

    def start_session(self):
        self.init_session.params = self.get_params(mode='w')
        self.init_session.load_key_params = self.set_key_params
        self.init_session.exec()

    def read_steganogramm(self):
        if not hasattr(self, 'stegoImage'):
            dlg = CustomDialog("Отсутствует стегоконтейнер")
            dlg.exec()
            return

        self.get_text_from_image(self.stegoImage[1])

    '''
    Утилитарные функции
    '''

    @staticmethod
    def __set_picture(graphicsView, picture, bsc):
        pixmap = QtGui.QPixmap.fromImage(picture)

        scene = QGraphicsScene()
        scene.addPixmap(pixmap)

        graphicsView.scale(1 / bsc, 1 / bsc)
        scw, sch = (graphicsView.width() - 2) / scene.width(), (graphicsView.height() - 2) / scene.height()
        if scw <= 1 or sch <= 1:
            sc = scw if scw < sch else sch
        else:
            sc = scw if scw > sch else sch
        graphicsView.scale(sc, sc)
        graphicsView.setScene(scene)
        return sc

    def prepare_to_transform(self):
        self.ui.progressBar.setValue(5)
        self.ui.state.setText('Подготовка')
        params = self.get_params(mode='w')
        if params is None:
            raise Exception('Не удалось считать параметры')

        if not hasattr(self, 'originalImage'):
            raise Exception('Отсутствует исходное изображение')

        self.ui.progressBar.setValue(10)
        self.ui.state.setText('Подготовка текста')
        text = self.ui.sendingMessage.toPlainText()
        byte_text = bytearray(text, encoding=params.encoding)
        self.ui.progressBar.setValue(12)

        return [params, byte_text]

    def prepare_key(self, params, mode='w'):
        self.ui.progressBar.setValue(15)
        if not hasattr(self.key_params, 'key'):
            if mode == 'w':
                self.ui.state.setText('Генерация ключа')
                self.key_params.keycode = self.get_key_embedding(params) + self.cascading_code.get_keycode()
                self.key_params.random_sequence_key()
            elif mode == 'r':
                raise Exception('Отсутствует ключ')
        key = self.key_params.key
        params = self.update_params_from_keycode(params, key[0], key[1])
        state = None
        if mode == 'w':
            self.update_params_interface(params)
            state = self.ui.stego_params_w
        elif mode == 'r':
            state = self.ui.stego_params_r

        state.setText(
            'Параметры стегоконтейнера: Алгоритм - {}, Преобразование - {}, Встраивание - {}, Цветовое пространство - {}'.format(
                'Enhanced' if key[0][2] == 1 else 'Fast',
                'DCT 2D' if key[0][3] == 1 else 'Slant',
                'Коха-Жао' if key[0][1] == 1 else 'Бенгама-Мемона-Эо-Юнг',
                'YCbCr' if key[0][0] == 1 else 'RGB'))
        return [key, params]

    def get_key_embedding(self, params):
        return [1 if params.isYCbCr else 0,
                1 if params.embedding is not None and params.embedding is embedding_kj else 0,
                1 if params.algorithm is EnhancedAlgorithm else 0,
                1 if params.transform is scipyDCT else 0]

    def update_params_from_keycode(self, params, key_embedding, key_cascading_code):
        params.isYCbCr = key_embedding[0] == 1
        params.embedding, params.extraction = \
            [embedding_kj, extraction_kj] if key_embedding[1] == 1 else [embedding_bmej, extraction_bmej]
        params.algorithm = EnhancedAlgorithm if key_embedding[2] == 1 else FastAlgorithm
        params.transform = scipyDCT if key_embedding[3] == 1 else Slant
        self.cascading_code.update_params(key_cascading_code)
        return params

    def update_params_interface(self, params):
        self.ui.selectAlgorithm.setCurrentIndex(1 if params.algorithm is EnhancedAlgorithm else 0)
        self.ui.selectEmbadding.setCurrentIndex(1 if params.embedding is embedding_kj else 0)
        self.ui.selectTransform.setCurrentIndex(1 if params.transform is scipyDCT else 0)
        self.ui.checkYCbCr.setChecked(params.isYCbCr)

    @staticmethod
    def get_answer():
        try:
            with open('info/embedding_help.txt', encoding='utf-8', mode='r') as info:
                dlg = CustomDialog(info.read())
                dlg.exec()
        except FileNotFoundError as err:
            dlg = CustomDialog('Отсутствует файл справки\n' + str(err))
            dlg.exec()


app = QApplication(sys.argv)
window = ExpenseTracker()
window.show()

sys.exit(app.exec())
