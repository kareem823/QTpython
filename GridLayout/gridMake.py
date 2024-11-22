from PySide6.QtWidgets import QWidget,  QSizePolicy, QGridLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QGridLayout Demo")


        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button_4 = QPushButton("Four")
        button_5 = QPushButton("Five")
        button_6 = QPushButton("Six")
        button_7 = QPushButton("Seven")

        # Create a QGridLayout and add buttons to specific grid positions
        grid_layout = QGridLayout()

        # Place button_1 at row 0, column 0
        grid_layout.addWidget(button_1, 0, 0)  
        # Place button_2 at row 0, column 1,
                #spanning 1 row and 2 columns
        grid_layout.addWidget(button_2, 0, 1, 1, 2)   
        # Place button_3 at row 1, column 0, spanning 2 rows and 1 column
        grid_layout.addWidget(button_3, 1, 0, 2, 1)
        # Place button_4 at row 1, column 1
        grid_layout.addWidget(button_4, 1, 1) 
         
        grid_layout.addWidget(button_5,1,2)
        grid_layout.addWidget(button_6,2,1)
        grid_layout.addWidget(button_7,2,2)

        self.setLayout(grid_layout)