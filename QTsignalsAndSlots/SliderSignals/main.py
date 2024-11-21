from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys
from SliderWidgetMethods import *
app = QApplication(sys.argv)



slider = QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(0)
slider.setMaximum(50)
slider.setTickInterval(2)
'''slider.setTickPosition(QSlider.TickPosition.{pick what you want})

This line configures where the tick marks appear on a QSlider widget

TicksBelow means the tick marks will be shown below the slider track

Other possible options include:
TicksAbove: Shows ticks above the slider
TicksBothSides: Shows ticks on both sides
NoTicks: Hides all tick marks'''
slider.setTickPosition(QSlider.TickPosition.TicksLeft)
window = SliderMethods()

#connect the slider to the slider_moved method
slider.valueChanged.connect(window.slider_moved)

#make the slider visible on screen
#the SliderMethods class inherets from QMainWindow, so we
#  need to call the show method on the slider object which calls
#  the show method on the window instance of the class
slider.show() #always need to .show() the widget and/or window

sys.exit(app.exec())

