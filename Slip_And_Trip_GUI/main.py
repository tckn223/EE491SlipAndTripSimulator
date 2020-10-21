import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import Database

## ==> SPLASH SCREEN
from SplashScreen import Ui_SplashScreen

## ==> MAIN WINDOW
from Main_Window import Ui_MainWindow
from Main_Window_Functions import *

## ==> Add Simulation Screen
from Add_Patient import *

## ==> GLOBALS
counter = 0

# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MAIN WINDOW LABEL
        self.ui.Patient.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Patient_Information))
        self.ui.Platform.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Platform_Running))
        self.ui.Add_Patient.clicked.connect(self.Add_Patient)

        # Populate lists
        for patient in Database.patient_information:
            self.ui.listWidget.addItem(patient)
        self.ui.listWidget.itemSelectionChanged.connect(self.Update_Patient_Fields)

        for simulation in Database.custom_simulation:
            self.ui.listWidget_2.addItem(simulation)

    # ADD PATIENT WINDOW
    def Add_Patient(self):
        self.Add_Patient_Screen = QDialog()
        self.Add_Patient_Screen.ui = Ui_Add_Patient_Screen()
        self.Add_Patient_Screen.ui.setupUi(self.Add_Patient_Screen)
        self.Add_Patient_Screen.ui.Add_Patient_2.clicked.connect(self.Write_New_Patient)
        self.Add_Patient_Screen.exec_()
    def Write_New_Patient(self):
        if (self.Add_Patient_Screen.ui.genderLineEdit.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_2.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_3.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_4.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_5.text() != '') and \
        (self.Add_Patient_Screen.ui.genderLineEdit_6.text() != ''):
            Subject_ID = self.Add_Patient_Screen.ui.genderLineEdit.text()
            New_Patient = {
                self.Add_Patient_Screen.ui.genderLabel.text() : self.Add_Patient_Screen.ui.genderLineEdit_2.text(),
                self.Add_Patient_Screen.ui.heightLabel_2.text() : self.Add_Patient_Screen.ui.genderLineEdit_3.text(),
                self.Add_Patient_Screen.ui.ageLabel_2.text() : self.Add_Patient_Screen.ui.genderLineEdit_4.text(),
                self.Add_Patient_Screen.ui.shoeSizeLabel.text() : self.Add_Patient_Screen.ui.genderLineEdit_5.text(),
                self.Add_Patient_Screen.ui.weightLabel_2.text() : self.Add_Patient_Screen.ui.genderLineEdit_6.text()
            }
            Database.patient_information[Subject_ID] = New_Patient
            Database.write_to_database()
            self.Add_Patient_Screen.close()

    # PATIENT TAB
    def Update_Patient_Fields(self):
        patient = self.ui.listWidget.currentItem().text()
        self.ui.genderLineEdit.setText(Database.patient_information[patient][self.ui.genderLabel.text()])
        self.ui.heightLineEdit.setText(Database.patient_information[patient][self.ui.heightLabel.text()])
        self.ui.ageLineEdit.setText(Database.patient_information[patient][self.ui.ageLabel.text()])
        self.ui.shoeSizeLineEdit.setText(Database.patient_information[patient][self.ui.shoeSizeLabel.text()])
        self.ui.weightLineEdit.setText(Database.patient_information[patient][self.ui.weightLabel.text()])

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    Database.load_database()
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
