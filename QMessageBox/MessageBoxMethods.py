from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
import sys

#make a class for MessageBox Methods
class BoxWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")
        self.setGeometry(300, 300, 400, 300)

        FAQButton = QPushButton("Hard")
        FAQButton.clicked.connect(self.FAQButtonClicked)

        #create the layout to store all widgets
        layout = QVBoxLayout()
        layout.addWidget(FAQButton)
        self.setLayout(layout)

    #Create a QMessageBox function for when the user presses the 
    #QPushButton for FAQ they get a pop up for what the app is about.
    #with a button to confirm
    def FAQButtonClicked(self):
        FAQMsgMessageBox = QMessageBox()
        FAQMsgMessageBox.setMinimumSize(500, 400)
        FAQMsgMessageBox.setWindowTitle("App FAQ")
        FAQMsgMessageBox.setText("This is an App to Help you with your ____ needs!")
        FAQMsgMessageBox.setInformativeText("This is a text to inform you about the app")
        FAQMsgMessageBox.setIcon(QMessageBox.Icon.Information)
        FAQMsgMessageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #set the default Button
        FAQMsgMessageBox.setDefaultButton(QMessageBox.Ok)

        #Show the message box
        showMessage = FAQMsgMessageBox.exec()

        #if the ok button is clicked then confirm
        # if the cancel button is clicked then do nothing
        if showMessage == QMessageBox.Ok:
            print("You clicked OK")
        else:
            print("You clicked Cancel")
        

    






