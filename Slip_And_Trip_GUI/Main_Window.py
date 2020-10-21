# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_WindowQQjaYK.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Reference Sans Serif")
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Patient = QPushButton(self.frame_top_menus)
        self.Patient.setObjectName(u"Patient")
        self.Patient.setMinimumSize(QSize(0, 40))
        self.Patient.setFont(font)
        self.Patient.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Patient.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.Patient)

        self.Platform = QPushButton(self.frame_top_menus)
        self.Platform.setObjectName(u"Platform")
        self.Platform.setMinimumSize(QSize(0, 40))
        self.Platform.setFont(font)
        self.Platform.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Platform.setAutoDefault(True)

        self.verticalLayout_4.addWidget(self.Platform)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Patient_Information = QWidget()
        self.Patient_Information.setObjectName(u"Patient_Information")
        self.Add_Patient = QPushButton(self.Patient_Information)
        self.Add_Patient.setObjectName(u"Add_Patient")
        self.Add_Patient.setGeometry(QRect(0, 0, 251, 71))
        font1 = QFont()
        font1.setFamily(u"MS Reference Sans Serif")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.Add_Patient.setFont(font1)
        self.Add_Patient.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.listWidget = QListWidget(self.Patient_Information)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 70, 251, 361))
        self.listWidget.setFont(font1)
        self.listWidget.setMouseTracking(True)
        self.listWidget.setTabletTracking(True)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")
        self.formLayoutWidget = QWidget(self.Patient_Information)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(260, 0, 641, 392))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(28)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.genderLabel = QLabel(self.formLayoutWidget)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setFont(font1)
        self.genderLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.genderLabel)

        self.genderLineEdit = QLineEdit(self.formLayoutWidget)
        self.genderLineEdit.setObjectName(u"genderLineEdit")
        self.genderLineEdit.setMinimumSize(QSize(0, 19))
        self.genderLineEdit.setFont(font1)
        self.genderLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.genderLineEdit)

        self.heightLabel = QLabel(self.formLayoutWidget)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setFont(font1)
        self.heightLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.heightLabel)

        self.heightLineEdit = QLineEdit(self.formLayoutWidget)
        self.heightLineEdit.setObjectName(u"heightLineEdit")
        self.heightLineEdit.setFont(font1)
        self.heightLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.heightLineEdit)

        self.ageLabel = QLabel(self.formLayoutWidget)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setFont(font1)
        self.ageLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.ageLabel)

        self.ageLineEdit = QLineEdit(self.formLayoutWidget)
        self.ageLineEdit.setObjectName(u"ageLineEdit")
        self.ageLineEdit.setFont(font1)
        self.ageLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ageLineEdit)

        self.shoeSizeLabel = QLabel(self.formLayoutWidget)
        self.shoeSizeLabel.setObjectName(u"shoeSizeLabel")
        self.shoeSizeLabel.setFont(font1)
        self.shoeSizeLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.shoeSizeLabel)

        self.shoeSizeLineEdit = QLineEdit(self.formLayoutWidget)
        self.shoeSizeLineEdit.setObjectName(u"shoeSizeLineEdit")
        self.shoeSizeLineEdit.setFont(font1)
        self.shoeSizeLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.shoeSizeLineEdit)

        self.weightLabel = QLabel(self.formLayoutWidget)
        self.weightLabel.setObjectName(u"weightLabel")
        self.weightLabel.setFont(font1)
        self.weightLabel.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.weightLabel)

        self.weightLineEdit = QLineEdit(self.formLayoutWidget)
        self.weightLineEdit.setObjectName(u"weightLineEdit")
        self.weightLineEdit.setFont(font1)
        self.weightLineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.weightLineEdit)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.Save_Patient_Info = QPushButton(self.Patient_Information)
        self.Save_Patient_Info.setObjectName(u"Save_Patient_Info")
        self.Save_Patient_Info.setGeometry(QRect(260, 290, 321, 141))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.Save_Patient_Info.setFont(font2)
        self.Save_Patient_Info.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Save_Patient_Info_2 = QPushButton(self.Patient_Information)
        self.Save_Patient_Info_2.setObjectName(u"Save_Patient_Info_2")
        self.Save_Patient_Info_2.setGeometry(QRect(590, 290, 311, 141))
        self.Save_Patient_Info_2.setFont(font2)
        self.Save_Patient_Info_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"    font: 12pt\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.stackedWidget.addWidget(self.Patient_Information)
        self.Platform_Running = QWidget()
        self.Platform_Running.setObjectName(u"Platform_Running")
        self.gridLayoutWidget = QWidget(self.Platform_Running)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(110, 0, 331, 371))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.checkBox_4, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.checkBox_3, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.gridLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.checkBox, 3, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 1px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.checkBox_2, 2, 2, 1, 1)

        self.Add_Patient_2 = QPushButton(self.Platform_Running)
        self.Add_Patient_2.setObjectName(u"Add_Patient_2")
        self.Add_Patient_2.setGeometry(QRect(450, 0, 451, 431))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.Add_Patient_2.setFont(font3)
        self.Add_Patient_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton = QPushButton(self.Platform_Running)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 101, 23))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.listWidget_2 = QListWidget(self.Platform_Running)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(0, 30, 101, 331))
        self.listWidget_2.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"	font: 12pt\n"
"}")
        self.pushButton_2 = QPushButton(self.Platform_Running)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 370, 101, 61))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}")
        self.Save_Patient_Info_3 = QPushButton(self.Platform_Running)
        self.Save_Patient_Info_3.setObjectName(u"Save_Patient_Info_3")
        self.Save_Patient_Info_3.setGeometry(QRect(110, 380, 331, 51))
        self.Save_Patient_Info_3.setFont(font3)
        self.Save_Patient_Info_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.stackedWidget.addWidget(self.Platform_Running)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"EXPAND", None))
        self.Patient.setText(QCoreApplication.translate("MainWindow", u"Patient", None))
        self.Platform.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.Add_Patient.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.listWidget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.genderLabel.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height (in)", None))
        self.ageLabel.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.shoeSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Shoe Size", None))
        self.weightLabel.setText(QCoreApplication.translate("MainWindow", u"Weight (lbs)", None))
        self.label.setText("")
        self.Save_Patient_Info.setText(QCoreApplication.translate("MainWindow", u"Save Patient Information", None))
        self.Save_Patient_Info_2.setText(QCoreApplication.translate("MainWindow", u"Delete Patient Information", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Acceleration", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"lock", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Lock", None))
        self.Add_Patient_2.setText(QCoreApplication.translate("MainWindow", u"RUN SIMULATION", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Simulation", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete Simulation", None))
        self.Save_Patient_Info_3.setText(QCoreApplication.translate("MainWindow", u"Save Simulation Information", None))
    # retranslateUi
