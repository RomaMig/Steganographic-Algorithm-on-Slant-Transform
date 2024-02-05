# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_params.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_KeyParams(object):
    def setupUi(self, KeyParams):
        if not KeyParams.objectName():
            KeyParams.setObjectName(u"KeyParams")
        KeyParams.resize(353, 198)
        self.buttonBox = QDialogButtonBox(KeyParams)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(180, 160, 161, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.sequenceKey = QPlainTextEdit(KeyParams)
        self.sequenceKey.setObjectName(u"sequenceKey")
        self.sequenceKey.setGeometry(QRect(10, 40, 331, 111))
        self.layoutWidget = QWidget(KeyParams)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 331, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.readKey = QPushButton(self.layoutWidget)
        self.readKey.setObjectName(u"readKey")

        self.horizontalLayout.addWidget(self.readKey)

        self.save_key = QPushButton(self.layoutWidget)
        self.save_key.setObjectName(u"save_key")

        self.horizontalLayout.addWidget(self.save_key)

        self.randomSequenceKey = QPushButton(self.layoutWidget)
        self.randomSequenceKey.setObjectName(u"randomSequenceKey")

        self.horizontalLayout.addWidget(self.randomSequenceKey)


        self.retranslateUi(KeyParams)
        self.buttonBox.accepted.connect(KeyParams.accept)
        self.buttonBox.rejected.connect(KeyParams.reject)

        QMetaObject.connectSlotsByName(KeyParams)
    # setupUi

    def retranslateUi(self, KeyParams):
        KeyParams.setWindowTitle(QCoreApplication.translate("KeyParams", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043b\u044e\u0447\u0430", None))
        self.sequenceKey.setPlaceholderText(QCoreApplication.translate("KeyParams", u"\u041a\u043b\u044e\u0447", None))
        self.readKey.setText(QCoreApplication.translate("KeyParams", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u043a\u043b\u044e\u0447", None))
        self.save_key.setText(QCoreApplication.translate("KeyParams", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043b\u044e\u0447", None))
        self.randomSequenceKey.setText(QCoreApplication.translate("KeyParams", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u043b\u044e\u0447", None))
    # retranslateUi

