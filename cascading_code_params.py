from PySide6.QtWidgets import QDialog
from ui.cascading_code import Ui_CascadingCode
from utilities.correcting_code import CascadingCode


class CascadingCodeParams(QDialog):

    def __init__(self):
        super(CascadingCodeParams, self).__init__()
        self.ui = Ui_CascadingCode()
        self.ui.setupUi(self)
        self.initUI()
        self.cascading_code_params = CascadingCode(True, True, True, True, 3, 4, 2, 2)

    def initUI(self):
        self.ui.checkCascadingCode.stateChanged.connect(self.check_cascading_code)
        self.ui.checkReedsolo.stateChanged.connect(self.check_reedsolo)
        self.ui.checkConvCode.stateChanged.connect(self.check_conv_code)
        self.ui.checkSpectrumExpansion.stateChanged.connect(self.check_spectrum_expansion)
        self.ui.selectConvSpeed.currentTextChanged.connect(self.select_conv_speed)
        self.ui.setSpectrumExtension.valueChanged.connect(self.set_spectrum_expansion)
        self.ui.setBlockSize.valueChanged.connect(self.set_block_size)
        self.ui.setEccSize.valueChanged.connect(self.set_ecc_size)

    def check_cascading_code(self):
        self.cascading_code_params.is_cascading_code = self.ui.checkCascadingCode.isChecked()

    def check_spectrum_expansion(self):
        self.cascading_code_params.is_spectrum_expansion = self.ui.checkSpectrumExpansion.isChecked()

    def check_conv_code(self):
        self.cascading_code_params.is_conv_code = self.ui.checkConvCode.isChecked()

    def check_reedsolo(self):
        self.cascading_code_params.is_reedsolo = self.ui.checkReedsolo.isChecked()

    def select_conv_speed(self):
        conv_speed = {'1/2': 2,
                      '1/3': 3}
        self.cascading_code_params.speed_conv_code = conv_speed.get(self.ui.selectConvSpeed.currentText())

    def set_spectrum_expansion(self):
        self.cascading_code_params.expansion = int(self.ui.setSpectrumExtension.value())

    def set_block_size(self):
        self.cascading_code_params.code_size = int(self.ui.setBlockSize.value())

    def set_ecc_size(self):
        self.cascading_code_params.ecc_size = int(self.ui.setEccSize.value())

    def update_interface(self):
        self.ui.checkCascadingCode.setChecked(self.cascading_code_params.is_cascading_code)
        self.ui.checkReedsolo.setChecked(self.cascading_code_params.is_reedsolo)
        self.ui.checkConvCode.setChecked(self.cascading_code_params.is_conv_code)
        self.ui.checkSpectrumExpansion.setChecked(self.cascading_code_params.is_spectrum_expansion)
        self.ui.selectConvSpeed.setCurrentIndex(self.cascading_code_params.speed_conv_code - 2)
        self.ui.setEccSize.setValue(self.cascading_code_params.ecc_size)
        self.ui.setBlockSize.setValue(self.cascading_code_params.code_size)
        self.ui.setSpectrumExtension.setValue(self.cascading_code_params.expansion)

    def update_params(self, key_code):
        self.cascading_code_params.is_cascading_code = key_code[0] == 1
        self.cascading_code_params.is_conv_code = key_code[1] == 1
        self.cascading_code_params.is_reedsolo = key_code[2] == 1
        self.cascading_code_params.is_spectrum_expansion = key_code[3] == 1
        self.cascading_code_params.speed_conv_code = key_code[4] + 2
        self.cascading_code_params.ecc_size = key_code[5] + 1
        self.cascading_code_params.code_size = key_code[6] + 1
        self.cascading_code_params.expansion = key_code[7] + 2
        self.update_interface()

    def get_keycode(self):
        return [1 if self.cascading_code_params.is_cascading_code else 0,
                1 if self.cascading_code_params.is_conv_code else 0,
                1 if self.cascading_code_params.is_reedsolo else 0,
                1 if self.cascading_code_params.is_spectrum_expansion else 0,
                self.cascading_code_params.speed_conv_code - 2,
                self.cascading_code_params.ecc_size - 1,
                self.cascading_code_params.code_size - 1,
                self.cascading_code_params.expansion - 2]
