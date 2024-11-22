from PySide6.QtWidgets import *

from PySide6.QtCore import *
from PySide6.QtGui import *

from GuiTools import *

#create methods to change the user input like Fonts size, style, color, indentation
class UserInputMethods(QMainWindow):
    def __init__(self, app):
        super(UserInputMethods, self).__init__()

        self.app = app  # Store a reference to the QApplication instance


    def FontSizeSelector(self, toolbar: QToolBar, textEdit: QTextEdit, initialSize: int) -> None:
        fontSizeSelector = QSpinBox()
        fontSizeSelector.setRange(5, 80)
        fontSizeSelector.setValue(initialSize)
        fontSizeSelector.valueChanged.connect(lambda: textEdit.setFontPointSize(fontSizeSelector.value()))
        toolbar.addWidget(fontSizeSelector)

    #create a method to make a combo box for selecting the font style
    def FontStyleSelector(self, toolbar: QToolBar, textEdit: QTextEdit) -> None:
        fontSelector = QComboBox()
        #get the font style libraries and add them to the combo box
        fontFamilies = QFontDatabase.families()
        for family in fontFamilies:
            fontSelector.addItem(family)
        #connect the combo box selection change to the handler
        fontSelector.currentTextChanged.connect(lambda: textEdit.setFontFamily(fontSelector.currentText()))
        toolbar.addWidget(fontSelector)

