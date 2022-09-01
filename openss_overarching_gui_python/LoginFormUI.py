# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(625, 565)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | MainWindow.windowFlags())
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 550, 500))
        self.widget.setMinimumSize(QSize(0, 0))
        self.bgImg = QLabel(self.widget)
        self.bgImg.setObjectName(u"bgImg")
        self.bgImg.setGeometry(QRect(10, 30, 200, 430))
        self.bgImg.setStyleSheet(u"border-image: url(:/images/menuside2.webp);\n"
"border-top-left-radius: 60px;")
        self.bgImg.setScaledContents(False)
        self.fadeSolid = QLabel(self.widget)
        self.fadeSolid.setObjectName(u"fadeSolid")
        self.fadeSolid.setGeometry(QRect(10, 30, 530, 430))
        self.fadeSolid.setStyleSheet(u"background-color: rgba(200,200,200,255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 80), stop:0.38 rgba(230, 230, 230, 255));\n"
"border-bottom-right-radius: 60px;\n"
"border-top-left-radius: 60px;")
        self.Title = QLabel(self.widget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(300, 70, 181, 35))
        font = QFont()
        font.setFamilies([u"STHeiti"])
        font.setPointSize(30)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"color: rgb(0, 50, 100)")
        self.KeyInput = QLineEdit(self.widget)
        self.KeyInput.setObjectName(u"KeyInput")
        self.KeyInput.setGeometry(QRect(290, 180, 200, 35))
        font1 = QFont()
        font1.setFamilies([u"Gurmukhi Sangam MN"])
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.KeyInput.setFont(font1)
        self.KeyInput.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(100, 100, 100, 100);\n"
"color: rgba(0,0,0,200);\n"
"padding-bottom: 7px;")
        self.SecretInput = QLineEdit(self.widget)
        self.SecretInput.setObjectName(u"SecretInput")
        self.SecretInput.setGeometry(QRect(290, 260, 200, 35))
        self.SecretInput.setFont(font1)
        self.SecretInput.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(100, 100, 100, 100);\n"
"color: rgba(0,0,0,200);\n"
"padding-bottom: 7px;")
        self.inpButton = QPushButton(self.widget)
        self.inpButton.setObjectName(u"inpButton")
        self.inpButton.setGeometry(QRect(310, 350, 155, 50))
        font2 = QFont()
        font2.setFamilies([u"PT Sans"])
        font2.setPointSize(20)
        self.inpButton.setFont(font2)
        self.inpButton.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(180, 100, 0, 255), stop:1 rgba(150, 0, 0, 255));\n"
"	border-radius: 10px;\n"
"	color: rgba(255,255,255,255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(180, 150, 50, 255), stop:1 rgba(150, 50, 50, 255));\n"
"}")
        self.logoBar = QLabel(self.widget)
        self.logoBar.setObjectName(u"logoBar")
        self.logoBar.setGeometry(QRect(10, 95, 241, 71))
        self.logoBar.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.65 rgba(0, 0, 0, 40), stop:0.90 rgba(230, 230, 230, 255))")
        self.logoImg = QLabel(self.widget)
        self.logoImg.setObjectName(u"logoImg")
        self.logoImg.setGeometry(QRect(20, 105, 161, 51))
        self.logoImg.setStyleSheet(u"border-image: url(:/images/logo.webp)")
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(20, 430, 20, 20))
        font3 = QFont()
        font3.setPointSize(12)
        self.exitButton.setFont(font3)
        self.exitButton.setStyleSheet(u"QPushButton{\n"
        "	background-color: rgb(197, 0, 0);\n"
        "	border-radius: 8px;\n"
        "	border-style: solid;\n"
        "	border-width: 1px;\n"
        "	border-color: rgba(80, 80, 80, 200);\n"
        "	color: rgba(255,255,255,200);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "	background-color: rgba(220, 50, 50, 200)\n"
        "}")

        self.errMsg = QLabel(self.widget)
        self.errMsg.setObjectName(u"label")
        self.errMsg.setGeometry(QRect(278, 410, 220, 20))
        font4 = QFont()
        font4.setPointSize(15)
        self.errMsg.setFont(font4)
        self.errMsg.setStyleSheet(u"color: rgba(255, 0, 0,200)")
        self.errMsg.setAlignment(Qt.AlignCenter)

        self.bgImg.raise_()
        self.logoBar.raise_()
        self.fadeSolid.raise_()
        self.Title.raise_()
        self.KeyInput.raise_()
        self.SecretInput.raise_()
        self.inpButton.raise_()
        self.logoImg.raise_()
        self.exitButton.raise_()
        self.errMsg.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.exitButton.clicked.connect(lambda: MainWindow.close())
        self.inpButton.clicked.connect(lambda: self.changeValidateText(MainWindow.verifyKeys(
            key_id=self.KeyInput.text(),
            key_secret=self.SecretInput.text()
        )))

    def changeValidateText(self, validity):
        if validity is None:
            self.errMsg.setText("Invalid Key or Secret.")
        else:
            self.errMsg.setText("Log in success!")



    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bgImg.setText("")
        self.fadeSolid.setText("")
        self.Title.setText(QCoreApplication.translate("MainWindow", u"LOGIN KEYS", None))
        self.KeyInput.setText("")
        self.KeyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"API Key ID...", None))
        self.SecretInput.setText("")
        self.SecretInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"API Key Secret...", None))
        self.inpButton.setText(QCoreApplication.translate("MainWindow", u"Validate Keys", None))
        self.logoBar.setText("")
        self.logoImg.setText("")
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

