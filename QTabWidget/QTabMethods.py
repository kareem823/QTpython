from PySide6.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        #1 Create the Qtab widget object
        self.tabWidget = QTabWidget(self)
        #2 set the attributes of the tab widget
        self.tabWidget.setGeometry(200, 200, 300, 200)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        #create a layout object
        self.layout = QVBoxLayout()
        #add the tab widget to the layout
        self.layout.addWidget(self.tabWidget)
        #add tabs to the widget
        #creat a ne QWidget for each tab
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabWidget.addTab(self.tab1, "Tab1")
        self.tabWidget.addTab(self.tab2, "Tab2")

        
        #add items to the layout
        self.button = QPushButton("Click Me", self.tab1)
        self.tab1.layout = QVBoxLayout()
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.layout.addWidget(self.button)
        
        def change_color():
            self.tab1.setStyleSheet("background-color: lightblue;")
        
        self.button.clicked.connect(change_color)

        #add another button
        #add items to the layout
        self.button2 = QPushButton("button 2", self.tab2)
        self.tab2.layout = QVBoxLayout()
        self.tab2.setLayout(self.tab2.layout)
        self.tab2.layout.addWidget(self.button2)
        
        def change_color():
            self.tab2.setStyleSheet("background-color: lightgreen;")
        
        self.button2.clicked.connect(change_color)

        self.setLayout(self.layout)
