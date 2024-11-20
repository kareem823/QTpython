from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys



app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Lesson 3")
window.setFixedSize(900, 600)


# Create a central widget to hold the layout
centralWidget = QWidget()
window.setCentralWidget(centralWidget)

# Create and set the layout for the central widget
initialLayout = QVBoxLayout()
initialLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the layout contents
centralWidget.setLayout(initialLayout)

# Create a button to take the user to the next window
button = QPushButton("Go to Lesson 4")
button.setFixedSize(120, 50)
button.setStyleSheet("font-size: 15px;")

# Add the button to the layout
initialLayout.addWidget(button)

#create a new page for the user to go to Lesson4
def nextPage():
###this is a widget that will be the center of the window, 
#it will replace the button that the user clicked on
    centerWidget2 = QWidget()
    layout = QVBoxLayout(centerWidget2)

   ### #this is a non editable text box that will display the text that the user inputs
    #create a label to tell the user that they are in the next window for lesson 4
    lesson4Label = QLabel("You are now in Lesson 4")
    lesson4Label.setStyleSheet("font-size: 15px;")

    layout.addWidget(lesson4Label)
    layout.setAlignment(lesson4Label, Qt.AlignmentFlag.AlignCenter)

    window.setCentralWidget(centerWidget2)

button.clicked.connect(nextPage)

window.show()
app.exec()

