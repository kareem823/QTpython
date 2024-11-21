import sys
from PyQt6.QtWidgets import *

class SliderMethods(QMainWindow):
    #the constructor for the class
    def __init__(self):
        #call the constructor of the super class
        super().__init__()

        #create a button
        '''
        #In Python, the self keyword is used to refer to the instance 
         of the class within the class itself.
        #If you don't pass self, the method will be treated as
          a function, not bound to the instance, and calling it will result in an error
        '''
    def slider_moved(self, value):
        print(f"Slider moved to value = {value}")

