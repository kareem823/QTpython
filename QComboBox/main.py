import sys
from PyQt6.QtWidgets import QApplication
from Methods import TextEditor


app = QApplication(sys.argv)
editor = TextEditor()
editor.show()
sys.exit(app.exec())