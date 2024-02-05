# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(910, 756)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 911, 721))
        self.tabWidget.setAutoFillBackground(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(380, 150, 521, 521))
        self.transformImage = QGraphicsView(self.groupBox_2)
        self.transformImage.setObjectName(u"transformImage")
        self.transformImage.setGeometry(QRect(10, 70, 501, 441))
        self.transformImage.setMinimumSize(QSize(200, 200))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 501, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.transform = QPushButton(self.layoutWidget)
        self.transform.setObjectName(u"transform")

        self.horizontalLayout.addWidget(self.transform)

        self.checkContainer = QPushButton(self.layoutWidget)
        self.checkContainer.setObjectName(u"checkContainer")

        self.horizontalLayout.addWidget(self.checkContainer)

        self.saveSteganogramm = QPushButton(self.layoutWidget)
        self.saveSteganogramm.setObjectName(u"saveSteganogramm")

        self.horizontalLayout.addWidget(self.saveSteganogramm)

        self.toPlot = QPushButton(self.layoutWidget)
        self.toPlot.setObjectName(u"toPlot")
        self.toPlot.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout.addWidget(self.toPlot)

        self.label_trans_img = QLabel(self.groupBox_2)
        self.label_trans_img.setObjectName(u"label_trans_img")
        self.label_trans_img.setGeometry(QRect(10, 50, 501, 16))
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 381, 671))
        self.sendingMessage = QPlainTextEdit(self.groupBox_3)
        self.sendingMessage.setObjectName(u"sendingMessage")
        self.sendingMessage.setGeometry(QRect(10, 90, 361, 571))
        self.sendingMessage.setMinimumSize(QSize(200, 0))
        self.sendingMessage.setMaximumSize(QSize(400, 16777215))
        self.openMessage = QPushButton(self.groupBox_3)
        self.openMessage.setObjectName(u"openMessage")
        self.openMessage.setGeometry(QRect(10, 20, 111, 24))
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(232, 20, 71, 20))
        self.selectEncode = QComboBox(self.groupBox_3)
        self.selectEncode.addItem(u"cp866")
        self.selectEncode.addItem("")
        self.selectEncode.addItem("")
        self.selectEncode.addItem("")
        self.selectEncode.addItem("")
        self.selectEncode.setObjectName(u"selectEncode")
        self.selectEncode.setGeometry(QRect(300, 20, 71, 22))
        self.file_path_box = QPlainTextEdit(self.groupBox_3)
        self.file_path_box.setObjectName(u"file_path_box")
        self.file_path_box.setEnabled(True)
        self.file_path_box.setGeometry(QRect(10, 50, 361, 31))
        self.file_path_box.setReadOnly(True)
        self.startSession = QPushButton(self.groupBox_3)
        self.startSession.setObjectName(u"startSession")
        self.startSession.setGeometry(QRect(124, 20, 101, 24))
        self.stego_params_w = QLabel(self.tab)
        self.stego_params_w.setObjectName(u"stego_params_w")
        self.stego_params_w.setGeometry(QRect(10, 670, 861, 16))
        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(380, 0, 521, 151))
        self.groupBox_7.setMinimumSize(QSize(0, 100))
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayoutWidget_10 = QWidget(self.groupBox_7)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 20, 508, 121))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_15 = QLabel(self.verticalLayoutWidget_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 140))

        self.verticalLayout.addWidget(self.label_15)

        self.selectEmbadding = QComboBox(self.verticalLayoutWidget_10)
        self.selectEmbadding.addItem("")
        self.selectEmbadding.addItem("")
        self.selectEmbadding.addItem("")
        self.selectEmbadding.setObjectName(u"selectEmbadding")
        self.selectEmbadding.setMaximumSize(QSize(16777215, 130))

        self.verticalLayout.addWidget(self.selectEmbadding)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.verticalLayoutWidget_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(95, 16777215))

        self.verticalLayout_2.addWidget(self.label_14)

        self.selectTransform = QComboBox(self.verticalLayoutWidget_10)
        self.selectTransform.addItem("")
        self.selectTransform.addItem("")
        self.selectTransform.addItem("")
        self.selectTransform.setObjectName(u"selectTransform")
        self.selectTransform.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_2.addWidget(self.selectTransform)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_16 = QLabel(self.verticalLayoutWidget_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout_3.addWidget(self.label_16)

        self.selectAlgorithm = QComboBox(self.verticalLayoutWidget_10)
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.addItem("")
        self.selectAlgorithm.setObjectName(u"selectAlgorithm")
        self.selectAlgorithm.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.selectAlgorithm)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_13 = QLabel(self.verticalLayoutWidget_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_4.addWidget(self.label_13)

        self.setThreshold = QDoubleSpinBox(self.verticalLayoutWidget_10)
        self.setThreshold.setObjectName(u"setThreshold")
        self.setThreshold.setMaximumSize(QSize(60, 16777215))
        self.setThreshold.setMinimum(4.000000000000000)
        self.setThreshold.setValue(18.000000000000000)

        self.verticalLayout_4.addWidget(self.setThreshold)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.verticalLayoutWidget_10)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2)

        self.question = QPushButton(self.verticalLayoutWidget_10)
        self.question.setObjectName(u"question")
        self.question.setMaximumSize(QSize(70, 16777215))

        self.verticalLayout_9.addWidget(self.question)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.checkYCbCr = QCheckBox(self.verticalLayoutWidget_10)
        self.checkYCbCr.setObjectName(u"checkYCbCr")

        self.horizontalLayout_7.addWidget(self.checkYCbCr)

        self.openCascadingCode = QPushButton(self.verticalLayoutWidget_10)
        self.openCascadingCode.setObjectName(u"openCascadingCode")

        self.horizontalLayout_7.addWidget(self.openCascadingCode)

        self.setKeyParams = QPushButton(self.verticalLayoutWidget_10)
        self.setKeyParams.setObjectName(u"setKeyParams")

        self.horizontalLayout_7.addWidget(self.setKeyParams)

        self.openImage = QPushButton(self.verticalLayoutWidget_10)
        self.openImage.setObjectName(u"openImage")

        self.horizontalLayout_7.addWidget(self.openImage)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.image_path_box = QPlainTextEdit(self.verticalLayoutWidget_10)
        self.image_path_box.setObjectName(u"image_path_box")
        self.image_path_box.setEnabled(True)
        self.image_path_box.setMaximumSize(QSize(16777215, 31))
        self.image_path_box.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.image_path_box)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 0, 381, 671))
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(232, 20, 71, 20))
        self.selectEncode_2 = QComboBox(self.groupBox_4)
        self.selectEncode_2.addItem(u"cp866")
        self.selectEncode_2.addItem("")
        self.selectEncode_2.addItem("")
        self.selectEncode_2.addItem("")
        self.selectEncode_2.addItem("")
        self.selectEncode_2.setObjectName(u"selectEncode_2")
        self.selectEncode_2.setGeometry(QRect(300, 20, 71, 22))
        self.receivedMessage = QPlainTextEdit(self.groupBox_4)
        self.receivedMessage.setObjectName(u"receivedMessage")
        self.receivedMessage.setEnabled(True)
        self.receivedMessage.setGeometry(QRect(10, 90, 361, 571))
        self.receivedMessage.setReadOnly(True)
        self.openSteganogramm = QPushButton(self.groupBox_4)
        self.openSteganogramm.setObjectName(u"openSteganogramm")
        self.openSteganogramm.setGeometry(QRect(10, 20, 151, 24))
        self.stego_path_box = QPlainTextEdit(self.groupBox_4)
        self.stego_path_box.setObjectName(u"stego_path_box")
        self.stego_path_box.setEnabled(True)
        self.stego_path_box.setGeometry(QRect(10, 50, 361, 31))
        self.stego_path_box.setReadOnly(True)
        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(380, 70, 501, 601))
        self.stegoImage = QGraphicsView(self.groupBox_5)
        self.stegoImage.setObjectName(u"stegoImage")
        self.stegoImage.setGeometry(QRect(10, 40, 481, 551))
        self.stegoImage.setMinimumSize(QSize(200, 200))
        self.label_stego_img = QLabel(self.groupBox_5)
        self.label_stego_img.setObjectName(u"label_stego_img")
        self.label_stego_img.setGeometry(QRect(10, 20, 481, 16))
        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(380, 0, 501, 71))
        self.groupBox_6.setMinimumSize(QSize(0, 0))
        self.groupBox_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 101, 16))
        self.horizontalLayoutWidget = QWidget(self.groupBox_6)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 481, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.setKeyParams_2 = QPushButton(self.horizontalLayoutWidget)
        self.setKeyParams_2.setObjectName(u"setKeyParams_2")

        self.horizontalLayout_2.addWidget(self.setKeyParams_2)

        self.readStego = QPushButton(self.horizontalLayoutWidget)
        self.readStego.setObjectName(u"readStego")

        self.horizontalLayout_2.addWidget(self.readStego)

        self.stego_params_r = QLabel(self.tab_2)
        self.stego_params_r.setObjectName(u"stego_params_r")
        self.stego_params_r.setGeometry(QRect(10, 670, 871, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(400, 730, 511, 20))
        self.progressBar.setValue(0)
        self.state = QLabel(self.centralwidget)
        self.state.setObjectName(u"state")
        self.state.setGeometry(QRect(10, 730, 381, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Image DCTStego", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0433\u0430\u043d\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.transform.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.checkContainer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440", None))
        self.saveSteganogramm.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0442\u0435\u0433\u043e\u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440", None))
        self.toPlot.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_trans_img.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.sendingMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442", None))
        self.openMessage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.selectEncode.setItemText(1, QCoreApplication.translate("MainWindow", u"cp1251", None))
        self.selectEncode.setItemText(2, QCoreApplication.translate("MainWindow", u"utf-8", None))
        self.selectEncode.setItemText(3, QCoreApplication.translate("MainWindow", u"utf-16", None))
        self.selectEncode.setItemText(4, QCoreApplication.translate("MainWindow", u"ascii", None))

        self.file_path_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.startSession.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0441\u0435\u0441\u0441\u0438\u044e", None))
        self.stego_params_w.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u0442\u0435\u0433\u043e\u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430:", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u0432\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.selectEmbadding.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043d\u0433\u0430\u043c\u0430-\u041c\u0435\u043c\u043e\u043d\u0430 ...", None))
        self.selectEmbadding.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0445\u0430-\u0416\u0430\u043e", None))
        self.selectEmbadding.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.selectTransform.setItemText(0, QCoreApplication.translate("MainWindow", u"Slant", None))
        self.selectTransform.setItemText(1, QCoreApplication.translate("MainWindow", u"DCT 2D", None))
        self.selectTransform.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.selectAlgorithm.setItemText(0, QCoreApplication.translate("MainWindow", u"Fast", None))
        self.selectAlgorithm.setItemText(1, QCoreApplication.translate("MainWindow", u"Enhanced", None))
        self.selectAlgorithm.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433", None))
        self.label_2.setText("")
        self.question.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.checkYCbCr.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u0432 YCbCr", None))
        self.openCascadingCode.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0441\u043a\u0430\u0434\u043d\u044b\u0439 \u043a\u043e\u0434", None))
        self.setKeyParams.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043b\u044e\u0447\u0430", None))
        self.openImage.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.image_path_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.selectEncode_2.setItemText(1, QCoreApplication.translate("MainWindow", u"cp1251", None))
        self.selectEncode_2.setItemText(2, QCoreApplication.translate("MainWindow", u"utf-8", None))
        self.selectEncode_2.setItemText(3, QCoreApplication.translate("MainWindow", u"utf-16", None))
        self.selectEncode_2.setItemText(4, QCoreApplication.translate("MainWindow", u"ascii", None))

        self.receivedMessage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043e \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u043e\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.openSteganogramm.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0442\u0435\u0433\u043e\u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440", None))
        self.stego_path_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0441\u0442\u0435\u0433\u0430\u043d\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u0433\u0430\u043d\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.label_stego_img.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.setKeyParams_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043b\u044e\u0447\u0430", None))
        self.readStego.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.stego_params_r.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u0442\u0435\u0433\u043e\u043a\u043e\u043d\u0442\u0435\u0439\u043d\u0435\u0440\u0430:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0418\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.state.setText("")
    # retranslateUi

