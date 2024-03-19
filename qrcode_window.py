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
        Form.resize(357, 699)
        Form.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushGenerate = QPushButton(Form)
        self.pushGenerate.setObjectName(u"pushGenerate")
        self.pushGenerate.setGeometry(QRect(80, 80, 181, 24))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pushGenerate.setFont(font)
        self.pushSave = QPushButton(Form)
        self.pushSave.setObjectName(u"pushSave")
        self.pushSave.setGeometry(QRect(270, 10, 75, 24))
        icon = QIcon()
        icon.addFile(u"icons/save as.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushSave.setIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 150, 311, 291))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 331, 22))
        self.pushZoomOut = QPushButton(Form)
        self.pushZoomOut.setObjectName(u"pushZoomOut")
        self.pushZoomOut.setGeometry(QRect(240, 110, 101, 24))
        icon1 = QIcon()
        icon1.addFile(u"icons/-.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushZoomOut.setIcon(icon1)
        self.pushColor = QPushButton(Form)
        self.pushColor.setObjectName(u"pushColor")
        self.pushColor.setGeometry(QRect(120, 110, 111, 24))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.pushColor.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"icons/color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushColor.setIcon(icon2)
        self.pushZoomIn = QPushButton(Form)
        self.pushZoomIn.setObjectName(u"pushZoomIn")
        self.pushZoomIn.setGeometry(QRect(10, 110, 101, 24))
        icon3 = QIcon()
        icon3.addFile(u"icons/+.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushZoomIn.setIcon(icon3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushGenerate.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u0434\u043b\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.pushSave.setText(QCoreApplication.translate("Form", u"Save File", None))
        self.label.setText("")
        self.lineEdit.setText("")
        self.pushZoomOut.setText(QCoreApplication.translate("Form", u"\u0423\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u044c", None))
        self.pushColor.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0446\u0432\u0435\u0442", None))
        self.pushZoomIn.setText(QCoreApplication.translate("Form", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c", None))
    # retranslateUi

