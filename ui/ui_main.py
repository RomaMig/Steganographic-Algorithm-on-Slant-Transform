# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGraphicsView, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 835)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 791, 801))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.originalImage = QGraphicsView(self.verticalLayoutWidget)
        self.originalImage.setObjectName(u"originalImage")
        self.originalImage.setMinimumSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.originalImage)

        self.transformImage = QGraphicsView(self.verticalLayoutWidget)
        self.transformImage.setObjectName(u"transformImage")
        self.transformImage.setMinimumSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.transformImage)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.openImage = QPushButton(self.verticalLayoutWidget)
        self.openImage.setObjectName(u"openImage")

        self.horizontalLayout_3.addWidget(self.openImage)

        self.saveTransformedImage = QPushButton(self.verticalLayoutWidget)
        self.saveTransformedImage.setObjectName(u"saveTransformedImage")

        self.horizontalLayout_3.addWidget(self.saveTransformedImage)

        self.openTransformedImage = QPushButton(self.verticalLayoutWidget)
        self.openTransformedImage.setObjectName(u"openTransformedImage")

        self.horizontalLayout_3.addWidget(self.openTransformedImage)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.selectEncode = QComboBox(self.groupBox)
        self.selectEncode.addItem(u"cp866")
        self.selectEncode.addItem("")
        self.selectEncode.addItem("")
        self.selectEncode.addItem("")
        self.selectEncode.addItem("")
        self.selectEncode.setObjectName(u"selectEncode")
        self.selectEncode.setGeometry(QRect(88, 30, 71, 22))
        self.checkYCbCr = QCheckBox(self.groupBox)
        self.checkYCbCr.setObjectName(u"checkYCbCr")
        self.checkYCbCr.setGeometry(QRect(390, 60, 161, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 71, 20))
        self.selectSizeBlock = QComboBox(self.groupBox)
        self.selectSizeBlock.addItem("")
        self.selectSizeBlock.addItem("")
        self.selectSizeBlock.setObjectName(u"selectSizeBlock")
        self.selectSizeBlock.setGeometry(QRect(100, 60, 61, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 81, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 60, 121, 20))
        self.setThreshold = QDoubleSpinBox(self.groupBox)
        self.setThreshold.setObjectName(u"setThreshold")
        self.setThreshold.setGeometry(QRect(311, 60, 71, 22))
        self.setThreshold.setValue(5.000000000000000)
        self.transform = QPushButton(self.groupBox)
        self.transform.setObjectName(u"transform")
        self.transform.setGeometry(QRect(590, 60, 191, 24))
        self.toPlot = QPushButton(self.groupBox)
        self.toPlot.setObjectName(u"toPlot")
        self.toPlot.setGeometry(QRect(590, 30, 191, 24))
        self.setKeyParams = QPushButton(self.groupBox)
        self.setKeyParams.setObjectName(u"setKeyParams")
        self.setKeyParams.setGeometry(QRect(390, 30, 191, 24))
        self.selectTransform = QComboBox(self.groupBox)
        self.selectTransform.addItem("")
        self.selectTransform.addItem("")
        self.selectTransform.addItem("")
        self.selectTransform.addItem("")
        self.selectTransform.setObjectName(u"selectTransform")
        self.selectTransform.setGeometry(QRect(310, 30, 71, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 30, 141, 16))

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.sendingMessage = QPlainTextEdit(self.verticalLayoutWidget)
        self.sendingMessage.setObjectName(u"sendingMessage")

        self.horizontalLayout_5.addWidget(self.sendingMessage)

        self.receivedMessage = QPlainTextEdit(self.verticalLayoutWidget)
        self.receivedMessage.setObjectName(u"receivedMessage")
        self.receivedMessage.setEnabled(True)
        self.receivedMessage.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.receivedMessage)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u043a\u0440\u044b\u0442\u043e\u0433\u043e \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.openImage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.saveTransformedImage.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0442\u0435\u0433\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
        self.openTransformedImage.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0435\u0433\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.selectEncode.setItemText(1, QCoreApplication.translate("MainWindow", u"cp1251", None))
        self.selectEncode.setItemText(2, QCoreApplication.translate("MainWindow", u"utf-8", None))
        self.selectEncode.setItemText(3, QCoreApplication.translate("MainWindow", u"utf-16", None))
        self.selectEncode.setItemText(4, QCoreApplication.translate("MainWindow", u"ascii", None))

        self.checkYCbCr.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u0432 YCbCr", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.selectSizeBlock.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.selectSizeBlock.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0431\u043b\u043e\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433 \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f", None))
        self.transform.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.toPlot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.setKeyParams.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043b\u044e\u0447\u0430", None))
        self.selectTransform.setItemText(0, QCoreApplication.translate("MainWindow", u"2D py DCT", None))
        self.selectTransform.setItemText(1, QCoreApplication.translate("MainWindow", u"1D py DCT", None))
        self.selectTransform.setItemText(2, QCoreApplication.translate("MainWindow", u"2D DCT", None))
        self.selectTransform.setItemText(3, QCoreApplication.translate("MainWindow", u"1D DCT", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.sendingMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442", None))
        self.receivedMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043e \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
    # retranslateUi

