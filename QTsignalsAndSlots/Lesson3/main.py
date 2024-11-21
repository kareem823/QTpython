from PyQt6.QtWidgets import *
from WidgetMethods import *

import sys

app = QApplication(sys.argv)
button = QPushButton("Click Me!")
button.setCheckable(True) #allows the button to be checked(on) or unchecked(off)

window = ProjectMethods()

#connect the buttons clicked signal to the button_clicked method for results. 
button.clicked.connect(window.button_clicked)

button.show() #always need to .show() the widget and/or window

sys.exit(app.exec())

