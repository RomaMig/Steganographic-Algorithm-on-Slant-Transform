from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel


class CustomDialog(QDialog):
    def __init__(self, msg):
        super().__init__()

        self.setWindowTitle("Внимание")

        self.layout = QVBoxLayout()
        message = QLabel(msg)
        self.layout.addWidget(message)
        self.setLayout(self.layout)
