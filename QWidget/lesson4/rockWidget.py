from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")
                
        # Set the window size
        self.setGeometry(400, 400, 300, 400)

        #create a vertical layout
        rockLayout = QVBoxLayout()

        #I want to have 3 radio buttons, red, blue, green
        self.redRadioButton = QRadioButton("Red")
        self.blueRadioButton = QRadioButton("Blue")
        self.greenRadioButton = QRadioButton("Green")

        #add buttons to the layout
        rockLayout.addWidget(self.redRadioButton)
        rockLayout.addWidget(self.blueRadioButton)
        rockLayout.addWidget(self.greenRadioButton)

        #set the layout on the widget
        self.setLayout(rockLayout)

        #connect the radio buttons to the radioButtonColorsClicked method
        #via toggled signal
        self.redRadioButton.toggled.connect(self.radioButtonColorsClicked)
        self.blueRadioButton.toggled.connect(self.radioButtonColorsClicked)
        self.greenRadioButton.toggled.connect(self.radioButtonColorsClicked)


    def radioButtonColorsClicked(self):


        #I want to have a label that displays the color of the selected radio button
        if self.redRadioButton.isChecked():
            self.setStyleSheet("background-color: red;")
            print("Red radio button changed.")

        elif self.blueRadioButton.isChecked():
            
            self.setStyleSheet("background-color: blue;")
            print("Blue radio button changed.")
        elif self.greenRadioButton.isChecked():
            
            self.setStyleSheet("background-color: green;")
            print("Green radio button changed.")
        else:
            print("No radio button changed.")
            self.setStyleSheet("background-color: white;")




