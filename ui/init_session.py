# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'init_session.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QHBoxLayout,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_initSession(object):
    def setupUi(self, initSession):
        if not initSession.objectName():
            initSession.setObjectName(u"initSession")
        initSession.resize(489, 407)
        self.horizontalLayoutWidget = QWidget(initSession)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 471, 401))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget_3 = QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-1, 20, 241, 381))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 140))
        self.verticalLayoutWidget = QWidget(self.groupBox_3)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 211, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.openImageRSA = QPushButton(self.verticalLayoutWidget)
        self.openImageRSA.setObjectName(u"openImageRSA")

        self.verticalLayout.addWidget(self.openImageRSA)

        self.editPassword = QLineEdit(self.verticalLayoutWidget)
        self.editPassword.setObjectName(u"editPassword")
        self.editPassword.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.editPassword.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.editPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.editPassword)

        self.embeddingRSA = QPushButton(self.verticalLayoutWidget)
        self.embeddingRSA.setObjectName(u"embeddingRSA")

        self.verticalLayout.addWidget(self.embeddingRSA)

        self.saveRSA = QPushButton(self.verticalLayoutWidget)
        self.saveRSA.setObjectName(u"saveRSA")

        self.verticalLayout.addWidget(self.saveRSA)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 211, 161))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.openStegoSessionKey = QPushButton(self.verticalLayoutWidget_6)
        self.openStegoSessionKey.setObjectName(u"openStegoSessionKey")

        self.verticalLayout_9.addWidget(self.openStegoSessionKey)

        self.editPassword_2 = QLineEdit(self.verticalLayoutWidget_6)
        self.editPassword_2.setObjectName(u"editPassword_2")
        self.editPassword_2.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.editPassword_2.setInputMethodHints(Qt.ImhLatinOnly|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.editPassword_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.verticalLayout_9.addWidget(self.editPassword_2)

        self.extractionSessionKey = QPushButton(self.verticalLayoutWidget_6)
        self.extractionSessionKey.setObjectName(u"extractionSessionKey")

        self.verticalLayout_9.addWidget(self.extractionSessionKey)

        self.sessionKey = QPlainTextEdit(self.verticalLayoutWidget_6)
        self.sessionKey.setObjectName(u"sessionKey")
        self.sessionKey.setMaximumSize(QSize(16777215, 16777))
        self.sessionKey.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.sessionKey)


        self.verticalLayout_3.addWidget(self.groupBox_4)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 20, 241, 381))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 140))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_5)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 211, 151))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.openStegoRSA = QPushButton(self.verticalLayoutWidget_2)
        self.openStegoRSA.setObjectName(u"openStegoRSA")

        self.verticalLayout_2.addWidget(self.openStegoRSA)

        self.extractionRSA = QPushButton(self.verticalLayoutWidget_2)
        self.extractionRSA.setObjectName(u"extractionRSA")

        self.verticalLayout_2.addWidget(self.extractionRSA)

        self.publicKey = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.publicKey.setObjectName(u"publicKey")
        self.publicKey.setMaximumSize(QSize(16777215, 16777))
        self.publicKey.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.publicKey)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.verticalLayoutWidget_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 20, 211, 91))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.openImageSessionKey = QPushButton(self.verticalLayoutWidget_5)
        self.openImageSessionKey.setObjectName(u"openImageSessionKey")

        self.verticalLayout_7.addWidget(self.openImageSessionKey)

        self.embeddingSessionKey = QPushButton(self.verticalLayoutWidget_5)
        self.embeddingSessionKey.setObjectName(u"embeddingSessionKey")

        self.verticalLayout_7.addWidget(self.embeddingSessionKey)

        self.saveSessionKey = QPushButton(self.verticalLayoutWidget_5)
        self.saveSessionKey.setObjectName(u"saveSessionKey")

        self.verticalLayout_7.addWidget(self.saveSessionKey)


        self.verticalLayout_4.addWidget(self.groupBox_6)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(initSession)

        QMetaObject.connectSlotsByName(initSession)
    # setupUi

    def retranslateUi(self, initSession):
        initSession.setWindowTitle(QCoreApplication.translate("initSession", u"\u0418\u043d\u0438\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u0435\u0441\u0441\u0438\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("initSession", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("initSession", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u0448\u0430\u0433", None))
        self.openImageRSA.setText(QCoreApplication.translate("initSession", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.editPassword.setPlaceholderText(QCoreApplication.translate("initSession", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0441\u0435\u0441\u0441\u0438\u0438", None))
        self.embeddingRSA.setText(QCoreApplication.translate("initSession", u"\u0412\u0441\u0442\u0440\u043e\u0438\u0442\u044c RSA-\u043a\u043b\u044e\u0447", None))
        self.saveRSA.setText(QCoreApplication.translate("initSession", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("initSession", u"\u0412\u0442\u043e\u0440\u043e\u0439 \u0448\u0430\u0433", None))
        self.openStegoSessionKey.setText(QCoreApplication.translate("initSession", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0442\u0435\u0433\u0430\u043d\u043e\u0433\u0440\u0430\u043c\u043c\u0443", None))
        self.editPassword_2.setPlaceholderText(QCoreApplication.translate("initSession", u"\u041f\u0430\u0440\u043e\u043b\u044c \u0441\u0435\u0441\u0441\u0438\u0438", None))
        self.extractionSessionKey.setText(QCoreApplication.translate("initSession", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c \u0441\u0435\u0441\u0441\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("initSession", u"\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("initSession", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u0448\u0430\u0433", None))
        self.openStegoRSA.setText(QCoreApplication.translate("initSession", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u0442\u0435\u0433\u0430\u043d\u043e\u0433\u0440\u0430\u043c\u043c\u0443 RSA", None))
        self.extractionRSA.setText(QCoreApplication.translate("initSession", u"\u0418\u0437\u0432\u043b\u0435\u0447\u044c RSA-\u043a\u043b\u044e\u0447", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("initSession", u"\u0412\u0442\u043e\u0440\u043e\u0439 \u0448\u0430\u0433", None))
        self.openImageSessionKey.setText(QCoreApplication.translate("initSession", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.embeddingSessionKey.setText(QCoreApplication.translate("initSession", u"\u0412\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0441\u0435\u0441\u0441\u0438\u043e\u043d\u043d\u044b\u0439 \u043a\u043b\u044e\u0447", None))
        self.saveSessionKey.setText(QCoreApplication.translate("initSession", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

