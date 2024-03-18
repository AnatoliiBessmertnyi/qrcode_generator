# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qrcode_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(332, 425)
        self.pushGenerate = QPushButton(Form)
        self.pushGenerate.setObjectName(u"pushGenerate")
        self.pushGenerate.setGeometry(QRect(10, 290, 281, 24))
        self.pushSave = QPushButton(Form)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setGeometry(QRect(10, 10, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 261, 201))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(12, 260, 281, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushGenerate.setText(QCoreApplication.translate("Form", u"Generate QR Code", None))
        self.pushSave.setText(QCoreApplication.translate("Form", u"Save QR", None))
        self.label.setText("")
    # retranslateUi

