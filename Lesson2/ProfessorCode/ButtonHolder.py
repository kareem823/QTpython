from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

import sys
import os


#create the button holder class that will hold the buttons for the user to click on

#buttonHolder wll inherit everything from QWidget.
#this is single inheretance , meaning it can only inherit from one class
class ButtonHolder(QMainWindow):
    #over ride the constructor that initializes the class
    def __init__(self):
        #call the constructor of the super class
        super().__init__()

        #create the window for the button holder
        self.setWindowTitle("Button")
        button = QPushButton("Click me!")

        #set up the button as a central widget
        self.setCentralWidget(button)

















'''
(14:29:03) Courtney said:
Good afternoon, if you would like to be reinstated you would have to reply back to the email regarding being cancelled so they can take a look at seat availability. If you are wanting to switch to part time you can submit the following form to request the change:
(14:29:14) Courtney said:
https://forms.fanshawec.ca/readmission_program_transfer
(14:29:25) You said:
hi
(14:29:51) You said:
okay
(14:30:15) You said:
and can my advisor help me with going part time on monday in our meeting?
(14:30:31) You said:
when is the deadline for admissions?

(14:33:58) Courtney said:
Your advisor can definitely help you with your evaluation and options
(14:34:14) You said:
okay
(14:34:27) Courtney said:
The admissions will close once the program is full so there is no exact date
(14:34:44) You said:
okay,
(14:35:33) You said:
thanks for the help. Do you know of any common issues 
reguarding doing this? I am in a grad program AIM2. Does 
that make any difference?
(14:35:43) You said:
Im a domestic student.
(14:44:00) Courtney said:
Can I have your student number please?
(14:44:10) You said:
0881393
(14:48:57) Courtney said:
You would have to discuss with your advisor as it appears
 that program only runs on a full time basis so typically you 
 would need special permission if you are wanting to do that part time
'''