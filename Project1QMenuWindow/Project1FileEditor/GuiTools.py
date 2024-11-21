from PySide6.QtWidgets import *

from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import os

class GuiTools(QMainWindow):
    def __init__(self, app):
        super(GuiTools, self).__init__()
        self.app = app  # Store a reference to the QApplication instance

    def toolBarMessages(self) -> None:
        """Display a message in the status bar."""
        #need to make the status bar later
        self.statusBar().showMessage("Tool Bar Activated!", 8000)

    #I want to make a modal message box for the User when they 
    #click on the FAQ button in the app
    def showFAQMessageBox(self) -> None:
        """Display a modal message box with FAQ information."""
        FAQMsgBox = QMessageBox()
        FAQMsgBox.setWindowTitle("App FAQ")
        FAQMsgBox.setIcon(QMessageBox.Icon.Information)
        FAQMsgBox.setText("This is an app to help you read, write and create new text files on your pc!")
        FAQMsgBox.setInformativeText("Please press okay to confirm or cancel to exit the app.")

        #Create the FAQ buttons for ok or cancel
        FAQMsgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        showMessage =FAQMsgBox.exec_()
        #If the user clicks cancel, close the app
        if  showMessage == QMessageBox.Cancel:
            print("User exited App")
            sys.exit()
        #if the user clicks Okay then exit the modal and print a message
        elif showMessage == QMessageBox.Ok:
            print("User confirmed App FAQ")
        


