from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor with Font Selection")
        self.setGeometry(100, 100, 800, 600)

        # Initialize the text edit widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Create a toolbar
        self.toolbar = QToolBar("Formatting")
        self.addToolBar(self.toolbar)

        # Create a combo box for font selection
        self.font_combo = QComboBox()
        self.font_combo.setEditable(False)  # Non-editable combo box
        self.toolbar.addWidget(self.font_combo)

        # Populate the combo box with available fonts
        #The QFontDatabase class provides information about 
        # the fonts available in the underlying window system. 
        fontTree = QTreeWidget()
        fontTree.setColumnCount(2)
        fontFamilies = QFontDatabase.families()
        for family in fontFamilies:
            self.font_combo.addItem(family)

        # Connect the combo box selection change to the handler
        self.font_combo.currentTextChanged.connect(self.change_font)

    def change_font(self, font_name):
        """Change the font of the selected text or current cursor position."""
        current_font = self.text_edit.currentFont()
        current_font.setFamily(font_name)
        self.text_edit.setCurrentFont(current_font)


