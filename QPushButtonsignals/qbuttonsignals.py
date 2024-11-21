from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

#create a class with functions to display the different QPushButtons
class QPushButtonSignals(QMainWindow):
    def __init__(self):
        super().__init__()

        #set the title and creat the Main button
        self.setWindowTitle("QPushButton Signals")
        self.setGeometry(100, 100, 400, 300)

                # Set up the central widget and layout
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        self.MainButton = QPushButton(self)
        self.MainButton.setText("Click Me")
        self.MainButton.clicked.connect(self.buttonClicked)
        self.MainButton.pressed.connect(self.buttonPressed)
        self.MainButton.released.connect(self.buttonReleased)
        self.layout.addWidget(self.MainButton)


        #create the different functions for pushing button signals
    def buttonClicked(self):
        print("Button clicked")
        
    def buttonPressed(self):
        print("Button pressed")

    def buttonReleased(self):
        print("Button released")
