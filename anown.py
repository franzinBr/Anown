# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anown.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QSize(600, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left = QFrame(self.centralwidget)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setMinimumSize(QSize(40, 0))
        self.frame_left.setMaximumSize(QSize(40, 16777215))
        self.frame_left.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.settingsButton = QPushButton(self.frame_left)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border: 2px solid;\n"
" border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Menu_icon/res/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.settingsButton)

        self.verticalSpacer_4 = QSpacerItem(20, 555, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.closeFileButton = QPushButton(self.frame_left)
        self.closeFileButton.setObjectName(u"closeFileButton")
        self.closeFileButton.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border: 2px solid;\n"
" border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/closeFile_icon/res/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeFileButton.setIcon(icon1)
        self.closeFileButton.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.closeFileButton)

        self.fileButton = QPushButton(self.frame_left)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setStyleSheet(u"QPushButton {\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border: 2px solid;\n"
" border-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/openFile_icon/res/icons/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileButton.setIcon(icon2)
        self.fileButton.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.fileButton)


        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(self.centralwidget)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setStyleSheet(u"")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_right)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_right)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_2 = QHBoxLayout(self.home)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_cam = QFrame(self.frame_3)
        self.frame_cam.setObjectName(u"frame_cam")
        self.frame_cam.setMaximumSize(QSize(16777215, 16777215))
        self.frame_cam.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_cam.setFrameShape(QFrame.NoFrame)
        self.frame_cam.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_cam)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameLabel = QLabel(self.frame_cam)
        self.frameLabel.setObjectName(u"frameLabel")
        self.frameLabel.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frameLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frameLabel)


        self.horizontalLayout_4.addWidget(self.frame_cam)

        self.buttons_frame = QFrame(self.frame_3)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMinimumSize(QSize(0, 0))
        self.buttons_frame.setMaximumSize(QSize(100, 16777215))
        self.buttons_frame.setLayoutDirection(Qt.LeftToRight)
        self.buttons_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.buttons_frame.setFrameShape(QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_4 = QFrame(self.buttons_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.recordButton = QPushButton(self.frame_4)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setGeometry(QRect(10, 60, 80, 80))
        self.recordButton.setLayoutDirection(Qt.LeftToRight)
        self.recordButton.setAutoFillBackground(False)
        self.recordButton.setStyleSheet(u"QPushButton { \n"
" border-color: rgb(140, 140, 140);\n"
" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:39px;\n"
" max-width:78px;\n"
" max-height:78px;\n"
" min-width:78px;\n"
" min-height:78px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border-color: rgb(190, 190, 190);\n"
" border-width:3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
" border-color: rgb(221, 70, 10);\n"
" border-width:3px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Recording_icon/res/icons/recording.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.recordButton.setIcon(icon3)
        self.recordButton.setIconSize(QSize(60, 60))
        self.pauseButton = QPushButton(self.frame_4)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(25, 2, 50, 50))
        self.pauseButton.setLayoutDirection(Qt.LeftToRight)
        self.pauseButton.setStyleSheet(u"QPushButton { \n"
" border-color: rgb(140, 140, 140);\n"
" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:24px;\n"
" max-width:48px;\n"
" max-height:48px;\n"
" min-width:48px;\n"
" min-height:48px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border-color: rgb(190, 190, 190);\n"
" border-width:3px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/pause_icon/res/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseButton.setIcon(icon4)
        self.pauseButton.setIconSize(QSize(40, 40))
        self.pictureButton = QPushButton(self.frame_4)
        self.pictureButton.setObjectName(u"pictureButton")
        self.pictureButton.setGeometry(QRect(25, 148, 50, 50))
        self.pictureButton.setStyleSheet(u"QPushButton { \n"
" border-color: rgb(140, 140, 140);\n"
" background-color: white;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:24px;\n"
" max-width:48px;\n"
" max-height:48px;\n"
" min-width:48px;\n"
" min-height:48px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" border-color: rgb(190, 190, 190);\n"
" border-width:3px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(200, 200, 200);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/picture_icon/res/icons/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pictureButton.setIcon(icon5)
        self.pictureButton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.buttons_frame)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.home)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.verticalLayout_2 = QVBoxLayout(self.settings)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame_2 = QFrame(self.settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(53, 53, 53);\n"
"border-radius: 15%;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.settings)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 15%;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_5 = QFrame(self.settings)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"border-radius: 15%;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.footer_frame = QFrame(self.settings)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setMaximumSize(QSize(16777215, 20))
        self.footer_frame.setStyleSheet(u"background-color: rgb(53, 53, 53);")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_credits_3 = QLabel(self.footer_frame)
        self.label_credits_3.setObjectName(u"label_credits_3")
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.label_credits_3.setFont(font)
        self.label_credits_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_credits_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_credits_3)


        self.verticalLayout_2.addWidget(self.footer_frame)

        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_right)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Anown", None))
        self.settingsButton.setText("")
        self.closeFileButton.setText("")
        self.fileButton.setText("")
        self.frameLabel.setText("")
        self.recordButton.setText("")
        self.pauseButton.setText("")
        self.pictureButton.setText("")
        self.label_credits_3.setText(QCoreApplication.translate("MainWindow", u"Dev by: Alan Franzin de Oliveira", None))
    # retranslateUi

