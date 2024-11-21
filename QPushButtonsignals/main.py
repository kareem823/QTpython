from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
from qbuttonsignals import *

app = QApplication(sys.argv)

window = QPushButtonSignals()

window.show()

#Start the app
sys.exit(app.exec())

