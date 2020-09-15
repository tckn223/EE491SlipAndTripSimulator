import sys
import Database
import CustomSimulationWindows
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtCore import Qt

class NewPatientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'New Patient'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 220
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('You clicked New Patient', self)
        label.adjustSize()
        label.move(100, 70)

        button = QPushButton('OK', self)
        button.move(100, 120)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class ExistingPatientWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Existing Patient'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 220
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('You clicked Existing Patient', self)
        label.adjustSize()
        label.move(100, 70)

        button = QPushButton('OK', self)
        button.move(100, 120)
        button.clicked.connect(self.close_window)

        self.show()

    def close_window(self):
        self.close()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'dummyUI'
        self.left = 10
        self.top = 10
        self.width = 900
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        new_patient = QPushButton('New Patient', self)
        new_patient.setGeometry(100, 70, 100, 25)
        new_patient.clicked.connect(self.new_patient_click)

        existing_patient = QPushButton('Existing Patient', self)
        existing_patient.setGeometry(100, 120, 100, 25)
        existing_patient.clicked.connect(self.existing_patient_click)

        create_simulation = QPushButton('Create Simulation', self)
        create_simulation.setGeometry(250, 70, 100, 25)
        create_simulation.clicked.connect(self.create_simulation_click)

        load_simulation = QPushButton('Load Simulation', self)
        load_simulation.setGeometry(250, 120, 100, 25)
        load_simulation.clicked.connect(self.load_simulation_click)

        self.debug_text = QLabel('Debug Window', self)
        self.debug_text.setGeometry(400, 70, 400, 140)
        self.debug_text.setStyleSheet('background-color: white')
        self.debug_text.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.debug_text.setIndent(4)

        button = QPushButton('Exit', self)
        button.setGeometry(100, 170, 100, 25)
        button.clicked.connect(self.close_window)

        self.show()

    def new_patient_click(self):
        self.new_patient_window = NewPatientWindow()
        self.new_patient_window.show()

    def existing_patient_click(self):
        self.existing_patient_window = ExistingPatientWindow()
        self.existing_patient_window.show()

    def create_simulation_click(self):
        self.create_simulation_window = CustomSimulationWindows.CreateSimulationWindow()
        self.create_simulation_window.new_simulation.connect(self.create_simulation_handler)
        self.create_simulation_window.show()

    def create_simulation_handler(self, name, new_simulation):
        self.debug_text.setText(name + "\n" + str(new_simulation))
        Database.custom_simulation[name] = new_simulation
        Database.write_to_database()

    def load_simulation_click(self):
        self.load_simulation_window = CustomSimulationWindows.LoadSimulationWindow(Database.custom_simulation)
        self.load_simulation_window.selected_simulation.connect(self.load_simulation_handler)
        self.load_simulation_window.show()

    def load_simulation_handler(self, name):
        self.debug_text.setText(name + "\n" + str(Database.custom_simulation[name]))

    def close_window(self):
        self.close()

if __name__ == '__main__':
    Database.load_database()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
