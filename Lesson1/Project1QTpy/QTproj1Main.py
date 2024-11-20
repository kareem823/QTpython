from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox)
import sys  # Add this import at the top


class ApplicationWidgets(QDialog):
    def __init__(self, parent=None):
        super(ApplicationWidgets, self).__init__(parent)
        
        # Remove these lines as they're redundant with the main block
        # app = QApplication(sys.argv)
        # window = QWidget()
        # window.setWindowTitle("Input output project")

        # Create the layout and set it for this dialog
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create input text box
        inputTextBox = QTextEdit()
        inputTextBox.setPlaceholderText("input text here")
        layout.addWidget(inputTextBox)
        
        # Create button
        button = QPushButton("Show Text")
        layout.addWidget(button)

        # Update the button connection to show a message box
        button.clicked.connect(lambda: self.showText(inputTextBox.toPlainText()))
    
    def showText(self, text):
        QMessageBox.information(self, "Input Text", text)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    widget = ApplicationWidgets()  # Create the widget
    widget.show()
    sys.exit(app.exec())  # Start the event loop