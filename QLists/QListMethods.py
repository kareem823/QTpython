from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

class QListMethods(QWidget):


    #########################################################
    '''
    Try using currentItemChange in this project for the list or in the main project1

    .currentItemChanged signal for the list is used to detect changes in the current item.
    '''
    #################################################


    def __init__(self):
        super().__init__()

        self.setWindowTitle("QList Methods")
        self.setGeometry(500, 500, 600, 500)

        #Create a list object
        self.numList = QListWidget()

        #create the layout
        layout = QVBoxLayout()

        #create the buttons to add, delete, and clear the list
        self.addBtn = QPushButton("Add")
        self.deleteBtn = QPushButton("Delete")
        self.clearBtn = QPushButton("Clear")

                #Add the Text box to input values into the list
        self.inputValue = QLineEdit()
        self.inputValue.setPlaceholderText("Enter a value")
        layout.addWidget(self.inputValue)

        #Add the buttons to the layout
        layout.addWidget(self.addBtn)
        layout.addWidget(self.deleteBtn)
        layout.addWidget(self.clearBtn)


        #add the signals and slots between buttons, list and the functions
        self.addBtn.clicked.connect(self.addToList)
        #I want the add button to activate when i press enter
        self.inputValue.returnPressed.connect(self.addToList)

        self.deleteBtn.clicked.connect(self.deleteFromList)

        self.clearBtn.clicked.connect(self.clearList)

        #add the list to the layout
        layout.addWidget(self.numList)

        #add the input box and the layout to the window
        self.setLayout(layout)

        #create an empty list
        self.numbersArray = []


        #create a function to add values to the list
    def addToList(self):
        #get the value from the input box
        value = self.inputValue.text()
        #add the value to the list
        self.numbersArray.append(value)

        #clear the input box
        self.inputValue.clear()

        #add the value to the list widget
        if value is not None:
            self.numList.addItem(value)


    #create a function to delete values from the list
    def deleteFromList(self):
        #presson the item in the list that you want to delete
        item = self.numList.currentItem()
        #remove the item from the list by pressing the delete button
        self.numList.takeItem(self.numList.row(item))
        #delete the item from the list when i press the delete key on my keyboard.
        self.numList.keyPressEvent = lambda event: self.numList.takeItem(
            self.numList.row(self.numList.currentItem())) if event.key() == Qt.Key_Delete else super().keyPressEvent(event)


    #create a function to clear the whole list
    def clearList(self):
        #clear the list
        self.numList.clear()

