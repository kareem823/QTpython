from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
import os

#my class
from ButtonHolder import *

app = QApplication(sys.argv)

window = ButtonHolder()

#show the window
window.show()
#start the event loop
sys.exit(app.exec())


