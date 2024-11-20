# Import required Qt widgets from PySide6
from PySide6.QtWidgets import QApplication, QWidget
import sys #command line arguments

# Create a Qt Application instance
# sys.argv allows command line arguments to be passed to the application
app = QApplication(sys.argv)

# Create a basic Qt widget (window)
window = QWidget()
# Make the window visible on screen
window.show()

# Start the application's event loop
# This keeps the window running and responsive to user input
app.exec()