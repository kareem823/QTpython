from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")
                
        # Set the window size
        self.setGeometry(400, 400, 300, 400)
        # Create a vertical layout
        rockLayout = QVBoxLayout()

        # I want to have 3 radio buttons, red, blue, green
        self.redRadioButton = QRadioButton("Red")
        self.blueRadioButton = QRadioButton("Blue")
        self.greenRadioButton = QRadioButton("Green")

        # Add buttons to the layout
        rockLayout.addWidget(self.redRadioButton)
        rockLayout.addWidget(self.blueRadioButton)
        rockLayout.addWidget(self.greenRadioButton)

        # Create checkBoxes
        self.redCheckBox = QCheckBox("Red")
        self.blueCheckBox = QCheckBox("Blue")
        self.greenCheckBox = QCheckBox("Green")

        # Add checkboxes to the layout
        rockLayout.addWidget(self.redCheckBox)
        rockLayout.addWidget(self.blueCheckBox)
        rockLayout.addWidget(self.greenCheckBox)

        # Create a button to deselect all radio buttons and checkboxes
        self.deselectButton = QPushButton("Deselect All")
        rockLayout.addWidget(self.deselectButton)

        # Connect the deselect button to a method to deselect all
        self.deselectButton.clicked.connect(self.deselectAll)

        # Set the layout on the widget
        self.setLayout(rockLayout)

        #connect the radio buttons to the radioButtonColorsClicked method
        #via toggled signal
        self.redRadioButton.toggled.connect(self.buttonColorsClicked)
        self.blueRadioButton.toggled.connect(self.buttonColorsClicked)
        self.greenRadioButton.toggled.connect(self.buttonColorsClicked)

        #connect the checkboxes to the radioButtonColorsClicked method
        self.redCheckBox.toggled.connect(self.buttonColorsClicked)
        self.blueCheckBox.toggled.connect(self.buttonColorsClicked)
        self.greenCheckBox.toggled.connect(self.buttonColorsClicked)


    def buttonColorsClicked(self):


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

        #I want to have a label that displays the color of the selected checkbox
        elif self.redCheckBox.isChecked():
            self.setStyleSheet("background-color: red;")
            print("Red checkbox changed.")

        elif self.blueCheckBox.isChecked():
            
            self.setStyleSheet("background-color: blue;")
            print("Blue checkbox changed.")

        elif self.greenCheckBox.isChecked():
            
            self.setStyleSheet("background-color: green;")
            print("Green checkbox changed.")
        else:
            print("No button changed.")
            self.setStyleSheet("background-color: yellow;")



    def deselectAll(self):
        # Ensure radio buttons are deselected
        self.redRadioButton.setAutoExclusive(False)
        self.blueRadioButton.setAutoExclusive(False)
        #I want to deselect the green radio
        self.greenRadioButton.setAutoExclusive(False)

        self.redRadioButton.setChecked(False)
        self.blueRadioButton.setChecked(False)
        self.greenRadioButton.setChecked(False)

        # Restore auto-exclusive behavior
        self.redRadioButton.setAutoExclusive(True)
        self.blueRadioButton.setAutoExclusive(True)
        self.greenRadioButton.setAutoExclusive(True)
        self.redCheckBox.setChecked(False)
        self.blueCheckBox.setChecked(False)
        self.greenCheckBox.setChecked(False)

