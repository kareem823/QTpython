from PySide6.QtWidgets import *

from PySide6.QtCore import *
from PySide6.QtGui import *

from GuiTools import *
from UserInputMethods import *

import sys
import os
from docx import Document

class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.app = app
        self.setWindowTitle("Text Editor")
        self.setGeometry(530, 100, 800, 600)  # Combined move and setGeometry

        # Initialize the text widget
        self.textWidget = QTextEdit()
        self.textWidget.setUndoRedoEnabled(True)
        self.textWidget.setVisible(False)  # Initially hidden until a file is opened or new is created
        self.setCentralWidget(self.textWidget)

        self.currentFilePath = None  # Initialize to track the current file path

        self.createMenuBar()
        self.createToolBar()

        self.showWelcomeScreen()

        self.boldAction = QAction("Bold", self)
        self.boldAction.setShortcut(QKeySequence("Ctrl+b"))
        self.boldAction.triggered.connect(self.bold_text)
        self.toolBar.addAction(self.boldAction)

        self.guitool = GuiTools(app)
        self.boldAction.triggered.connect(self.guitool.toolBarMessages)


    #make a function to convert the contents in my text widget to html format
    def convertToHtml(self):
        #get the current text cursor
        cursor = self.textWidget.textCursor()
        #get the selected text
        selectedText = cursor.selectedText()
        #if there is selected text, convert that to html
        if selectedText:
            html = f"<html><body><p>{selectedText}</p></body></html>"
            #insert the html into the text widget at the current position
            cursor.insertHtml(html)
        else:
            #get the entire text from the widget
            text = self.textWidget.toPlainText()
            #convert it to html
            html = f"<html><body><p>{text}</p></body></html>"
            #set the text of the widget to html
            self.textWidget.setHtml(html)

    def bold_text(self):
        cursor = self.textWidget.textCursor()
        if cursor.hasSelection():
            # Get the current format of the selected text
            currentFormat = cursor.charFormat()
            
            # Check if the text is already bold
            isBold = currentFormat.fontWeight() == QFont.Bold
            
            # Toggle bold state
            newWeight = QFont.Normal if isBold else QFont.Bold
            currentFormat.setFontWeight(newWeight)
            
            # Apply the new format to the selected text
            cursor.mergeCharFormat(currentFormat)
        else:
            # If no text is selected, toggle the bold state at the cursor position
            currentCharFormat = self.textWidget.currentCharFormat()
            isBold = currentCharFormat.fontWeight() == QFont.Bold
            currentCharFormat.setFontWeight(QFont.Normal if isBold else QFont.Bold)
            self.textWidget.setCurrentCharFormat(currentCharFormat)

    def showWelcomeScreen(self):
        """Display the welcome screen with an 'Open File' button."""
        # Create a welcome widget
        self.welcomeWidget = QWidget()
        layout = QVBoxLayout()

        welcomeLabel = QLabel("Welcome! Please open a file or create a new document to begin.")
        openButton = QPushButton("Open File")
        newButton = QPushButton("New File")

        openButton.clicked.connect(self.openFile)
        newButton.clicked.connect(self.makeTextWidget)

        layout.addWidget(welcomeLabel)
        layout.addWidget(openButton)
        layout.addWidget(newButton)
        layout.addStretch()

        self.welcomeWidget.setLayout(layout)
        self.welcomeWidget.setFixedSize(self.size())  # Ensure it covers the entire window

        # Create a container widget to hold both welcome and text widgets
        self.containerWidget = QWidget()
        self.containerLayout = QStackedLayout()
        self.containerLayout.addWidget(self.welcomeWidget)
        self.containerLayout.addWidget(self.textWidget)
        self.containerWidget.setLayout(self.containerLayout)
        self.setCentralWidget(self.containerWidget)


    def openFile(self):
        """Open an existing file and display its content."""
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if filePath:
            try:
                with open(filePath, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.textWidget.setText(content)
                self.currentFilePath = filePath
                self.updateWindowTitle()
                self.containerLayout.setCurrentWidget(self.textWidget)
                self.textWidget.setVisible(True)
                self.textWidget.setFocus()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {e}")

    def createMenuBar(self) -> None:
        """Create a menu bar and add menu items to it."""
        self.menu: QMenuBar = self.menuBar()
        self.fileMenu: QMenu = self.menu.addMenu("File")
        self.editMenu: QMenu = self.menu.addMenu("Edit")

        self.addFileMenuItems()
        self.addEditMenuItems()

        aboutAction = QAction("About", self)
        aboutAction.triggered.connect(GuiTools.showFAQMessageBox)
        self.menu.addAction(aboutAction)


    def createToolBar(self):
        """Create a toolbar with redo functionality."""
        self.toolBar = QToolBar("Tools")
        self.toolBar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolBar)

        # Create the redo action
        self.redoAction = QAction("↷ Redo", self)
        self.redoAction.setShortcut("Ctrl+R")  # Common redo shortcut
        self.redoAction.triggered.connect(self.textWidget.redo)
        self.redoAction.setEnabled(False)  # Initially disabled

        # Add the redo action to the toolbar
        self.toolBar.addAction(self.redoAction)

        # Connect signals to enable/disable actions based on availability
        self.textWidget.redoAvailable.connect(self.redoAction.setEnabled)

        # Similarly, you can add an Undo action
        self.undoAction = QAction("↶ Undo", self)
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.textWidget.undo)
        self.undoAction.setEnabled(False)

        self.toolBar.addAction(self.undoAction)
        self.textWidget.undoAvailable.connect(self.undoAction.setEnabled)

        #create a QAction button to convert text to html
        self.htmlAction = QAction("To HTML", self)
        self.htmlAction.triggered.connect(self.convertToHtml)
        self.toolBar.addAction(self.htmlAction)

        #create a QToolButton to insert an image into the text file
        self.imageButton = QToolButton()
        self.imageButton.setText("Insert Image")
        self.imageButton.clicked.connect(lambda: GuiTools.imageInFile(self, self.textWidget))
        self.toolBar.addWidget(self.imageButton)

        #user the change font size method from the userinput class
        self.sizeSelector = UserInputMethods.FontSizeSelector(self, self.toolBar,self.textWidget, 11)

        #user the change font style method from the userinput class
        self.selectFont = UserInputMethods.FontStyleSelector(self, self.toolBar, self.textWidget)



    def addFileMenuItems(self) -> None:
        """Add items to the File menu."""
        # Create menu items
        self.newItem: QAction = self.fileMenu.addAction("New")
        self.openItem: QAction = self.fileMenu.addAction("Open")
        self.saveItem: QAction = self.fileMenu.addAction("Save")
        self.saveAs: QAction = self.fileMenu.addAction("Save As")
        self.fileMenu.addSeparator()
        self.exitItem: QAction = self.fileMenu.addAction("Exit")
        

        # Connect menu items to their respective methods
        self.newItem.triggered.connect(self.makeTextWidget)
        self.openItem.triggered.connect(self.openFile)
        self.saveItem.triggered.connect(self.saveFile)
        self.saveAs.triggered.connect(self.saveFileAs)
        self.exitItem.triggered.connect(self.exitApp)

    def addEditMenuItems(self) -> None:
        """Add items to the Edit menu."""
        self.undoMenuAction = QAction("Undo", self)
        self.undoMenuAction.setShortcut("Ctrl+Z")
        self.undoMenuAction.triggered.connect(self.textWidget.undo)
        self.undoMenuAction.setEnabled(False)

        self.redoMenuAction = QAction("Redo", self)
        self.redoMenuAction.setShortcut("Ctrl+Shift+Z")
        self.redoMenuAction.triggered.connect(self.textWidget.redo)
        self.redoMenuAction.setEnabled(False)

        self.editMenu.addAction(self.undoMenuAction)
        self.editMenu.addAction(self.redoMenuAction)

        # Connect signals to enable/disable menu actions
        self.textWidget.undoAvailable.connect(self.undoMenuAction.setEnabled)
        self.textWidget.redoAvailable.connect(self.redoMenuAction.setEnabled)

    def exitApp(self) -> None:
        """Exit the application."""
        self.close()
        sys.exit()

    def makeTextWidget(self) -> None:
        """Prepare the text widget for a new document."""
        self.textWidget.clear()
        self.currentFilePath = None
        self.updateWindowTitle()
        self.containerLayout.setCurrentWidget(self.textWidget)
        self.textWidget.setVisible(True)
        self.textWidget.setFocus()

    def saveFile(self) -> None:
        """Save the file to the current path or prompt for 'Save As'."""
        if not self.currentFilePath:
            self.saveFileAs()
        else:
            self.writeToFile(self.currentFilePath)


    def saveFileAs(self) -> None:
        """Save the current content to a new file."""
        if not self.textWidget.toPlainText():
            QMessageBox.warning(self, "Empty Document", "Cannot save an empty document.")
            return

        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Save As", "", "Text Files (*.txt);; Word Documents (*.docx) ;; All Files (*)", options=options
        )
        if filePath:
            self.currentFilePath = filePath
            self.writeToFile(filePath)

    def writeToFile(self, filePath):
        """Write the current content to the specified file."""
        try:
            content = self.textWidget.toPlainText()
            with open(filePath, 'w', encoding='utf-8') as file:
                file.write(content)
            self.updateWindowTitle()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save file: {e}")

    def updateWindowTitle(self):
        """Update the window title based on the current file."""
        if self.currentFilePath:
            fileName = os.path.basename(self.currentFilePath)
            self.setWindowTitle(f"{fileName} - Text Editor")
        else:
            self.setWindowTitle("Untitled - Text Editor")
