# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 750, 530))
        self.sideBG = QLabel(self.widget)
        self.sideBG.setObjectName(u"sideBG")
        self.sideBG.setGeometry(QRect(182, 38, 490, 433))
        self.sideBG.setStyleSheet(u"background-color: rgba(80, 100, 130, 255);\n"
"border-bottom-right-radius: 35px;\n"
"border-top: 10px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(100, 120, 150, 255), stop:1 rgba(80, 100, 130, 255));\n"
"border-bottom:  10px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(100, 120, 150, 255), stop:0 rgba(80, 100, 130, 255));\n"
"border-right: 10px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(100, 120, 150, 255), stop:0 rgba(80, 100, 130, 255));")
        self.BG = QLabel(self.widget)
        self.BG.setObjectName(u"BG")
        self.BG.setGeometry(QRect(30, 30, 651, 450))
        self.BG.setStyleSheet(u"background-color: rgba(100, 120, 150, 255);\n"
"border-top-left-radius: 40px;\n"
"border-bottom-right-radius: 50px;\n"
"border: 1px solid rgb(0, 0, 76);")
        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(40, 75, 130, 40))
        self.logo.setStyleSheet(u"border-image: url(:/images/logo.webp);")
        self.logoBG = QLabel(self.widget)
        self.logoBG.setObjectName(u"logoBG")
        self.logoBG.setGeometry(QRect(30, 60, 150, 70))
        self.logoBG.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.20197 rgba(255,255,255, 40), stop:0.8 rgba(255, 255, 255, 40), stop:1 rgba(0, 0, 0, 0))")
        self.linebar = QLabel(self.widget)
        self.linebar.setObjectName(u"linebar")
        self.linebar.setGeometry(QRect(180, 30, 2, 450))
        self.linebar.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.alignButton = QPushButton(self.widget)
        self.alignButton.setObjectName(u"alignButton")
        self.alignButton.setGeometry(QRect(30, 150, 150, 51))
        font = QFont()
        font.setFamilies([u".Lucida Grande UI"])
        self.alignButton.setFont(font)
        self.alignButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(100, 120, 150, 255);\n"
"border: none;\n"
"border-left: 1px solid rgba(0,0,0,200)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(100, 120, 150, 255));\n"
"border-left: 3px solid rgba(0,0,0,200)\n"
"}")
        self.detectButton = QPushButton(self.widget)
        self.detectButton.setObjectName(u"detectButton")
        self.detectButton.setGeometry(QRect(30, 200, 150, 51))
        self.detectButton.setFont(font)
        self.detectButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(100, 120, 150, 255);\n"
"border: none;\n"
"border-left: 1px solid rgba(0,0,0,200)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(100, 120, 150, 255));\n"
"border-left: 3px solid rgba(0,0,0,200)\n"
"}")
        self.compareButton = QPushButton(self.widget)
        self.compareButton.setObjectName(u"compareButton")
        self.compareButton.setGeometry(QRect(30, 250, 150, 51))
        self.compareButton.setFont(font)
        self.compareButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(100, 120, 150, 255);\n"
"border: none;\n"
"border-left: 1px solid rgba(0,0,0,200)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(100, 120, 150, 255));\n"
"border-left: 3px solid rgba(0,0,0,200)\n"
"}")
        self.ocrButton = QPushButton(self.widget)
        self.ocrButton.setObjectName(u"ocrButton")
        self.ocrButton.setGeometry(QRect(30, 300, 150, 51))
        self.ocrButton.setFont(font)
        self.ocrButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(100, 120, 150, 255);\n"
"border: none;\n"
"border-left: 1px solid rgba(0,0,0,200)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(100, 120, 150, 255));\n"
"border-left: 3px solid rgba(0,0,0,200)\n"
"}")
        self.poseButton = QPushButton(self.widget)
        self.poseButton.setObjectName(u"poseButton")
        self.poseButton.setGeometry(QRect(30, 350, 150, 51))
        self.poseButton.setFont(font)
        self.poseButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(100, 120, 150, 255);\n"
"border: none;\n"
"border-left: 1px solid rgba(0,0,0,200)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 40), stop:1 rgba(100, 120, 150, 255));\n"
"border-left: 3px solid rgba(0,0,0,200)\n"
"}")
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(40, 450, 20, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.exitButton.setFont(font1)
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
        self.BG.raise_()
        self.logoBG.raise_()
        self.logo.raise_()
        self.linebar.raise_()
        self.alignButton.raise_()
        self.detectButton.raise_()
        self.compareButton.raise_()
        self.ocrButton.raise_()
        self.poseButton.raise_()
        self.sideBG.raise_()
        self.exitButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.exitButton.clicked.connect(lambda: MainWindow.loadLoginMenu())
        self.alignButton.clicked.connect(lambda: MainWindow.loadAPIDemo(demo_type="alignment"))
        self.detectButton.clicked.connect(lambda: MainWindow.loadAPIDemo(demo_type="detect"))
        self.compareButton.clicked.connect(lambda: MainWindow.loadAPIDemo(demo_type="compare"))
        self.poseButton.clicked.connect(lambda: MainWindow.loadAPIDemo(demo_type="pose"))

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sideBG.setText("")
        self.BG.setText("")
        self.logo.setText("")
        self.logoBG.setText("")
        self.linebar.setText("")
        self.alignButton.setText(QCoreApplication.translate("MainWindow", u"Facial Alignment\n"
"Demonstration", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Facial Detection\n"
" Demonstration", None))
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"Face Comparing\n"
"Demonstration", None))
        self.ocrButton.setText(QCoreApplication.translate("MainWindow", u"Text Recognition\n"
" Demonstration", None))
        self.poseButton.setText(QCoreApplication.translate("MainWindow", u"Pose Recognition\n"
" Demonstration", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi

