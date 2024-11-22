from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
from rockWidget import *

app = QApplication(sys.argv)

# Create an instance of the RockWidget class
rockWidgetWindow = RockWidget()

#connect the radiobutton clicked signal to the radio button colors clicked method


# Show the window
rockWidgetWindow.show()

# Start the event loop
sys.exit(app.exec())