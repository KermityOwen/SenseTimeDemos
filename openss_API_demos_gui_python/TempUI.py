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
    QSizePolicy, QStackedWidget, QWidget)
import res_rc

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
        self.logo.setStyleSheet(u"border-image: url(:/images/images/logo.webp)")
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
"border-left: 1px solid rgba(0,0,0,200);\n"
"color: white;\n"
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
"border-left: 1px solid rgba(0,0,0,200);\n"
"color: white;\n"
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
"border-left: 1px solid rgba(0,0,0,200);\n"
"color: white\n"
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
"border-left: 1px solid rgba(0,0,0,200);\n"
"color: white\n"
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
"border-left: 1px solid rgba(0,0,0,200);\n"
"color: white\n"
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
        self.mainPages = QStackedWidget(self.widget)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setGeometry(QRect(185, 38, 490, 431))
        font2 = QFont()
        font2.setKerning(True)
        self.mainPages.setFont(font2)
        self.mainPages.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.alignPage = QWidget()
        self.alignPage.setObjectName(u"alignPage")
        self.align_desc = QLabel(self.alignPage)
        self.align_desc.setObjectName(u"align_desc")
        self.align_desc.setGeometry(QRect(25, 60, 451, 80))
        font3 = QFont()
        font3.setFamilies([u"Helvetica Neue"])
        font3.setPointSize(15)
        self.align_desc.setFont(font3)
        self.align_desc.setStyleSheet(u"color: rgb(200, 255, 240);")
        self.align_desc.setTextFormat(Qt.RichText)
        self.align_desc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.align_desc.setWordWrap(True)
        self.alignPost = QLabel(self.alignPage)
        self.alignPost.setObjectName(u"alignPost")
        self.alignPost.setGeometry(QRect(265, 130, 175, 220))
        self.alignPost.setStyleSheet(u"border-radius: 40px;\n"
"border-image: url(:/images/images/source_image_align.webp);")
        self.alignPre = QLabel(self.alignPage)
        self.alignPre.setObjectName(u"alignPre")
        self.alignPre.setGeometry(QRect(35, 130, 175, 220))
        self.alignPre.setStyleSheet(u"border-radius: 40px;\n"
"border-image: url(:/images/images/source_image.webp);")
        self.alignTitle = QLabel(self.alignPage)
        self.alignTitle.setObjectName(u"alignTitle")
        self.alignTitle.setGeometry(QRect(85, 10, 341, 40))
        font4 = QFont()
        font4.setFamilies([u"Helvetica Neue"])
        font4.setPointSize(23)
        self.alignTitle.setFont(font4)
        self.alignTitle.setStyleSheet(u"color: white\n"
"")
        self.alignTitle.setAlignment(Qt.AlignCenter)
        self.alignDemo = QPushButton(self.alignPage)
        self.alignDemo.setObjectName(u"alignDemo")
        self.alignDemo.setGeometry(QRect(180, 370, 120, 40))
        self.alignDemo.setStyleSheet(u"QPushButton{\n"
"border-radius: 12px;\n"
"border: 2px solid white;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(167, 0, 0, 255), stop:1 rgba(252, 159, 0, 255));\n"
"color: rgba(255, 255, 255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 20, 20, 255), stop:1 rgba(255, 179, 20, 255));\n"
"}")
        self.label = QLabel(self.alignPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(218, 240, 60, 16))
        font5 = QFont()
        font5.setBold(True)
        self.label.setFont(font5)
        self.mainPages.addWidget(self.alignPage)
        self.detectPage = QWidget()
        self.detectPage.setObjectName(u"detectPage")
        self.detectTitle = QLabel(self.detectPage)
        self.detectTitle.setObjectName(u"detectTitle")
        self.detectTitle.setGeometry(QRect(85, 10, 341, 40))
        self.detectTitle.setFont(font4)
        self.detectTitle.setStyleSheet(u"color: white\n"
"")
        self.detectTitle.setAlignment(Qt.AlignCenter)
        self.detectPre = QLabel(self.detectPage)
        self.detectPre.setObjectName(u"detectPre")
        self.detectPre.setGeometry(QRect(5, 160, 231, 171))
        self.detectPre.setStyleSheet(u"border-radius: 40px;\n"
"border-image: url(:/images/images/source_group.webp);")
        self.detectDesc = QLabel(self.detectPage)
        self.detectDesc.setObjectName(u"detectDesc")
        self.detectDesc.setGeometry(QRect(25, 60, 451, 80))
        self.detectDesc.setFont(font3)
        self.detectDesc.setStyleSheet(u"color: rgb(200, 255, 240);")
        self.detectDesc.setTextFormat(Qt.RichText)
        self.detectDesc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.detectDesc.setWordWrap(True)
        self.detectDemo = QPushButton(self.detectPage)
        self.detectDemo.setObjectName(u"detectDemo")
        self.detectDemo.setGeometry(QRect(180, 370, 120, 40))
        self.detectDemo.setStyleSheet(u"QPushButton{\n"
"border-radius: 12px;\n"
"border: 2px solid white;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(167, 0, 0, 255), stop:1 rgba(252, 159, 0, 255));\n"
"color: rgba(255, 255, 255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 20, 20, 255), stop:1 rgba(255, 179, 20, 255));\n"
"}")
        self.detectPost = QLabel(self.detectPage)
        self.detectPost.setObjectName(u"detectPost")
        self.detectPost.setGeometry(QRect(245, 160, 231, 171))
        self.detectPost.setStyleSheet(u"border-radius: 40px;\n"
"border-image: url(:/images/images/source_group_detect.webp)")
        self.mainPages.addWidget(self.detectPage)
        self.comparePage = QWidget()
        self.comparePage.setObjectName(u"comparePage")
        self.compareDemo = QPushButton(self.comparePage)
        self.compareDemo.setObjectName(u"compareDemo")
        self.compareDemo.setGeometry(QRect(180, 370, 120, 40))
        self.compareDemo.setStyleSheet(u"QPushButton{\n"
"border-radius: 12px;\n"
"border: 2px solid white;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(167, 0, 0, 255), stop:1 rgba(252, 159, 0, 255));\n"
"color: rgba(255, 255, 255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 20, 20, 255), stop:1 rgba(255, 179, 20, 255));\n"
"}")
        self.compareDesc = QLabel(self.comparePage)
        self.compareDesc.setObjectName(u"compareDesc")
        self.compareDesc.setGeometry(QRect(25, 60, 451, 80))
        self.compareDesc.setFont(font3)
        self.compareDesc.setStyleSheet(u"color: rgb(200, 255, 240);")
        self.compareDesc.setTextFormat(Qt.RichText)
        self.compareDesc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.compareDesc.setWordWrap(True)
        self.detectPost_2 = QLabel(self.comparePage)
        self.detectPost_2.setObjectName(u"detectPost_2")
        self.detectPost_2.setGeometry(QRect(245, 160, 231, 171))
        self.detectPost_2.setStyleSheet(u"border-radius: 40px;\n"
"border-top-left-radius: 0px;\n"
"border-image: url(:/images/images/compare_success.webp)")
        self.detectTitle_2 = QLabel(self.comparePage)
        self.detectTitle_2.setObjectName(u"detectTitle_2")
        self.detectTitle_2.setGeometry(QRect(75, 10, 361, 40))
        self.detectTitle_2.setFont(font4)
        self.detectTitle_2.setStyleSheet(u"color: white\n"
"")
        self.detectTitle_2.setAlignment(Qt.AlignCenter)
        self.detectPre_2 = QLabel(self.comparePage)
        self.detectPre_2.setObjectName(u"detectPre_2")
        self.detectPre_2.setGeometry(QRect(10, 160, 231, 171))
        self.detectPre_2.setStyleSheet(u"border-radius: 40px;\n"
"border-top-left-radius: 0px;\n"
"border-image: url(:/images/images/compare_failed.webp)")
        self.mainPages.addWidget(self.comparePage)
        self.ocrPage = QWidget()
        self.ocrPage.setObjectName(u"ocrPage")
        self.ocrDemo = QPushButton(self.ocrPage)
        self.ocrDemo.setObjectName(u"ocrDemo")
        self.ocrDemo.setGeometry(QRect(180, 370, 120, 40))
        self.ocrDemo.setStyleSheet(u"QPushButton{\n"
"border-radius: 12px;\n"
"border: 2px solid white;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(167, 0, 0, 255), stop:1 rgba(252, 159, 0, 255));\n"
"color: rgba(255, 255, 255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 20, 20, 255), stop:1 rgba(255, 179, 20, 255));\n"
"}")
        self.mainPages.addWidget(self.ocrPage)
        self.posePage = QWidget()
        self.posePage.setObjectName(u"posePage")
        self.poseDemo = QPushButton(self.posePage)
        self.poseDemo.setObjectName(u"poseDemo")
        self.poseDemo.setGeometry(QRect(180, 370, 120, 40))
        self.poseDemo.setStyleSheet(u"QPushButton{\n"
"border-radius: 12px;\n"
"border: 2px solid white;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(167, 0, 0, 255), stop:1 rgba(252, 159, 0, 255));\n"
"color: rgba(255, 255, 255,255)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 20, 20, 255), stop:1 rgba(255, 179, 20, 255));\n"
"}")
        self.mainPages.addWidget(self.posePage)
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
        self.mainPages.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
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
        self.align_desc.setText(QCoreApplication.translate("MainWindow", u"SenseTime's facial keypoint framework can identify all the most important keypoints of the face. This framework is only applicable to one face at a time.", None))
        self.alignPost.setText("")
        self.alignPre.setText("")
        self.alignTitle.setText(QCoreApplication.translate("MainWindow", u"Facial Keypoint Demonstration", None))
        self.alignDemo.setText(QCoreApplication.translate("MainWindow", u"Start Demo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"----->", None))
        self.detectTitle.setText(QCoreApplication.translate("MainWindow", u"Facial Detection Demonstration", None))
        self.detectPre.setText("")
        self.detectDesc.setText(QCoreApplication.translate("MainWindow", u"SenseTime's facial detection system can identify the amount of faces in an image and locate them. This is an efficient and fast model and is usually used for frame-by-frame video processing.", None))
        self.detectDemo.setText(QCoreApplication.translate("MainWindow", u"Start Demo", None))
        self.detectPost.setText("")
        self.compareDemo.setText(QCoreApplication.translate("MainWindow", u"Start Demo", None))
        self.compareDesc.setText(QCoreApplication.translate("MainWindow", u"SenseTime's facial comparison framework is used extract data about facial features and is used to compare faces, determining whether or not two images (each with a single face only) have the same person in them.", None))
        self.detectPost_2.setText("")
        self.detectTitle_2.setText(QCoreApplication.translate("MainWindow", u"Facial Comparison Demonstration", None))
        self.detectPre_2.setText("")
        self.ocrDemo.setText(QCoreApplication.translate("MainWindow", u"Start Demo", None))
        self.poseDemo.setText(QCoreApplication.translate("MainWindow", u"Start Demo", None))
    # retranslateUi

