from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

from QListMethods import *

app = QApplication(sys.argv)

window = QListMethods()
window.show()

sys.exit(app.exec())