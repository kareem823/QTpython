from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
from mainWindow import *

app = QApplication(sys.argv)

window = MainWindow(app)

GuiTool = GuiTools(app)


window.show()

# This line starts the application's main event loop. This is what makes the GUI
# appear on screen and start accepting user input. The event loop will continue
# to run until the user closes the application. Once the event loop exits, the
# application will terminate. The sys.exit() function call is used to ensure that
# the application exits cleanly.
sys.exit(app.exec())
