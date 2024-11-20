from PySide6.QtWidgets import QApplication, QWidget
import sys #command line arguments

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()
