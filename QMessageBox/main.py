from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
import sys

from MessageBoxMethods import *


app = QApplication(sys.argv)

widget = BoxWidget()
widget.show()

#start the program
sys.exit(app.exec())
