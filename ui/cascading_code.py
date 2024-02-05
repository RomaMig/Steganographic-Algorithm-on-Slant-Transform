# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cascading_code.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CascadingCode(object):
    def setupUi(self, CascadingCode):
        if not CascadingCode.objectName():
            CascadingCode.setObjectName(u"CascadingCode")
        CascadingCode.resize(431, 188)
        self.buttonBox = QDialogButtonBox(CascadingCode)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 150, 421, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox_4 = QGroupBox(CascadingCode)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, -20, 431, 161))
        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(270, 20, 161, 141))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 21, 141, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkReedsolo = QCheckBox(self.verticalLayoutWidget)
        self.checkReedsolo.setObjectName(u"checkReedsolo")
        self.checkReedsolo.setChecked(True)

        self.verticalLayout.addWidget(self.checkReedsolo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_2.addWidget(self.label_17)

        self.setBlockSize = QDoubleSpinBox(self.verticalLayoutWidget)
        self.setBlockSize.setObjectName(u"setBlockSize")
        self.setBlockSize.setMaximumSize(QSize(50, 16777215))
        self.setBlockSize.setDecimals(0)
        self.setBlockSize.setMinimum(1.000000000000000)
        self.setBlockSize.setMaximum(16.000000000000000)
        self.setBlockSize.setValue(4.000000000000000)

        self.horizontalLayout_2.addWidget(self.setBlockSize)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_24 = QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_3.addWidget(self.label_24)

        self.setEccSize = QDoubleSpinBox(self.verticalLayoutWidget)
        self.setEccSize.setObjectName(u"setEccSize")
        self.setEccSize.setMaximumSize(QSize(50, 16777215))
        self.setEccSize.setDecimals(0)
        self.setEccSize.setMinimum(1.000000000000000)
        self.setEccSize.setMaximum(64.000000000000000)
        self.setEccSize.setValue(2.000000000000000)

        self.horizontalLayout_3.addWidget(self.setEccSize)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(130, 20, 141, 111))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 18, 121, 81))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.checkConvCode = QCheckBox(self.layoutWidget)
        self.checkConvCode.setObjectName(u"checkConvCode")
        self.checkConvCode.setChecked(True)

        self.verticalLayout_7.addWidget(self.checkConvCode)

        self.label_25 = QLabel(self.layoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_7.addWidget(self.label_25)

        self.selectConvSpeed = QComboBox(self.layoutWidget)
        self.selectConvSpeed.addItem("")
        self.selectConvSpeed.addItem("")
        self.selectConvSpeed.setObjectName(u"selectConvSpeed")

        self.verticalLayout_7.addWidget(self.selectConvSpeed)

        self.groupBox_3 = QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 20, 131, 111))
        self.layoutWidget1 = QWidget(self.groupBox_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 17, 111, 88))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.checkSpectrumExpansion = QCheckBox(self.layoutWidget1)
        self.checkSpectrumExpansion.setObjectName(u"checkSpectrumExpansion")
        self.checkSpectrumExpansion.setChecked(True)

        self.verticalLayout_8.addWidget(self.checkSpectrumExpansion)

        self.label_26 = QLabel(self.layoutWidget1)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_8.addWidget(self.label_26)

        self.setSpectrumExtension = QDoubleSpinBox(self.layoutWidget1)
        self.setSpectrumExtension.setObjectName(u"setSpectrumExtension")
        self.setSpectrumExtension.setDecimals(0)
        self.setSpectrumExtension.setMinimum(2.000000000000000)
        self.setSpectrumExtension.setMaximum(18.000000000000000)
        self.setSpectrumExtension.setValue(3.000000000000000)

        self.verticalLayout_8.addWidget(self.setSpectrumExtension)

        self.checkCascadingCode = QCheckBox(self.groupBox_4)
        self.checkCascadingCode.setObjectName(u"checkCascadingCode")
        self.checkCascadingCode.setGeometry(QRect(20, 130, 261, 31))
        self.checkCascadingCode.setChecked(True)

        self.retranslateUi(CascadingCode)
        self.buttonBox.accepted.connect(CascadingCode.accept)
        self.buttonBox.rejected.connect(CascadingCode.reject)

        QMetaObject.connectSlotsByName(CascadingCode)
    # setupUi

    def retranslateUi(self, CascadingCode):
        CascadingCode.setWindowTitle(QCoreApplication.translate("CascadingCode", u"\u041a\u0430\u0441\u043a\u0430\u0434\u043d\u044b\u0439 \u043a\u043e\u0434", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("CascadingCode", u"GroupBox", None))
        self.groupBox.setTitle(QCoreApplication.translate("CascadingCode", u"\u041a\u043e\u0434 \u0420\u0438\u0434\u0430-\u0421\u043e\u043b\u043e\u043c\u043e\u043d\u0430", None))
        self.checkReedsolo.setText(QCoreApplication.translate("CascadingCode", u"\u041a\u043e\u0434 \u0420\u0438\u0434\u0430-\u0421\u043e\u043b\u043e\u043c\u043e\u043d\u0430", None))
        self.label_17.setText(QCoreApplication.translate("CascadingCode", u"\u0414\u043b\u0438\u043d\u043d\u0430 \u0431\u043b\u043e\u043a\u0430", None))
        self.label_24.setText(QCoreApplication.translate("CascadingCode", u"\u0414\u043b\u0438\u043d\u043d\u0430 \u0431\u043b\u043e\u043a\u0430\n"
"\u043a\u043e\u0440\u0440\u0435\u043a\u0446\u0438\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CascadingCode", u"\u0421\u0432\u0451\u0440\u0442\u043e\u0447\u043d\u044b\u0439 \u043a\u043e\u0434", None))
        self.checkConvCode.setText(QCoreApplication.translate("CascadingCode", u"\u0421\u0432\u0451\u0440\u0442\u043e\u0447\u043d\u044b\u0439 \u043a\u043e\u0434", None))
        self.label_25.setText(QCoreApplication.translate("CascadingCode", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043a\u043e\u0434\u0430", None))
        self.selectConvSpeed.setItemText(0, QCoreApplication.translate("CascadingCode", u"1/2", None))
        self.selectConvSpeed.setItemText(1, QCoreApplication.translate("CascadingCode", u"1/3", None))

        self.selectConvSpeed.setCurrentText(QCoreApplication.translate("CascadingCode", u"1/2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("CascadingCode", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435 \u0441\u043f\u0435\u043a\u0442\u0440\u0430", None))
        self.checkSpectrumExpansion.setText(QCoreApplication.translate("CascadingCode", u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u0438\u0435\n"
"\u0441\u043f\u0435\u043a\u0442\u0440\u0430", None))
        self.label_26.setText(QCoreApplication.translate("CascadingCode", u"\u041f\u043e\u0440\u044f\u0434\u043e\u043a", None))
        self.checkCascadingCode.setText(QCoreApplication.translate("CascadingCode", u"\u041a\u0430\u0441\u043a\u0430\u0434\u043d\u044b\u0439 \u043a\u043e\u0434", None))
    # retranslateUi

