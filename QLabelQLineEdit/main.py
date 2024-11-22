from PySide6.QtWidgets import QApplication
import sys
from QTextMethods import *

app = QApplication(sys.argv)

widget = QTextMethods()
widget.show()

sys.exit(app.exec())
