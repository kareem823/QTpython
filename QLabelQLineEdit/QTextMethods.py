from PySide6.QtWidgets import *

from PySide6.QtCore import *
from PySide6.QtGui import *

import sys
import os


# I want to make a class for QLabels and QLines
class QTextMethods(QWidget):
    def __init__(self):
        super().__init__()

        #create the Window title
        self.setWindowTitle("QTextMethods")
        self.setGeometry(400,400,500,400)
        self.setStyleSheet("background-color:green;")

        #create the QLine object
        self.lineEdit = QLineEdit()
        
        #Create the QLabel
        self.enterlabel = QLabel("Enter Name")

        #Create a QButton for showing name
        self.button = QPushButton("Show Name")
        self.button.clicked.connect(self.show_name)

        self.label = QLabel("User Name")

        #create a Horizontal qlayout
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.enterlabel)
        self.hlayout.addWidget(self.lineEdit)

        #create a verticle layout
        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(self.hlayout)
        #add the button
        self.vlayout.addWidget(self.button)
        self.vlayout.addWidget(self.label)

        self.setLayout(self.vlayout)



    #a function for getting the input from the qLineedit and displaying it in the qlabel
    def show_name(self):
        name = self.lineEdit.text()
        self.label.setText(name)
        