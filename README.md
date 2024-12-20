# QTpython and PySide6 Projects, Practice, and Lessons 1

# -----------------------
# Author: Kareem,
 2024
# -----------------------

# QAction:

- QAction is a class in PyQt that represents a menu item, context menus, or toolbar button.
- It acts as a reusable command that can be triggered by the user, for example, by clicking a menu item or a toolbar button.
- Reusable: A single QAction can be added to multiple menus or toolbars.
- Customizable: It can be enabled/disabled, have a checkable state, and carry data via its data() method.
- Event Handling: The triggered signal allows connecting to custom functionality when the action is triggered.

# QAction Example:

        `
        # Create a QAction
        self.exitAction = QAction("Exit", self)  # Text label "Exit"
        
        self.exitAction.setShortcut("Ctrl+Q")  
        
        # Add a keyboard shortcut
        
        self.exitAction.setStatusTip("Exit the application")  # Add a tooltip
        
        self.exitAction.triggered.connect(self.exitApp)  # Connect to a method 
        `

# Signals and Slots:

- Signals are emitted when an event occurs
- Slots are functions that are called when a signal is emitted
- Signals and slots are used to handle events in PyQt6
- Signals and slots are used to connect widgets together
- Signals are connected to slots using the `.connect()` method
- Most widgets have a signal, and the common signals are `.clicked, .pressed, .released,` and `.toggled`


# QMessageBox:

- QMessageBox is a class in PyQt that provides a simple way to display a message to the user.
- It can be used to display a message box with a title, text, and buttons.


# Types of common UI Widgets Used in Python QT6:

- **Widget (`QWidget`):** A basic container widget that can be used to group other widgets.
- **Layout (`QLayout`):** A container widget that can be used to manage the layout of other widgets.
- **Container (`QContainer`):** A container widget that can be used to manage the layout of other widgets.
- **Dialog (`QDialog`):** A dialog widget that can be used to display a dialog box.
- **MainWindow (`QMainWindow`):** A main window widget that can be used to display a main window.
- **Menu Bar (`QMenuBar`):** A menu bar widget that can be used to display a menu bar.
- **Tool Bar (`QToolBar`):** A tool bar widget that can be used to display a tool bar.
- **Status Bar (`QStatusBar`):** A status bar widget that can be used to display a status bar.
- **Dock Widget (`QDockWidget`):** A dock widget that can be used to display a dock widget.
- **Tool Box (`QToolBox`):** A tool box widget that can be used to display a tool box.
- **Scroll Area (`QScrollArea`):** A scroll area widget that can be used to display a scroll area.
- **Splitter (`QSplitter`):** A splitter widget that can be used to display a splitter.

-----------------------------------------

- **Button (`QPushButton`):** A clickable button that triggers an action.

- **Label (`QLabel`):** Displays text or images.
- **Radio Button (`QRadioButton`):** Allows the user to select one option from a set.
- **Check Box (`QCheckBox`):** Enables the user to select or deselect an option.
- **Combo Box (`QComboBox`):** A drop-down list for selecting an item.
- **Line Edit (`QLineEdit`):** A single-line text input field.
- **Text Edit (`QTextEdit`):** A multi-line text input field.
- **Spin Box (`QSpinBox`):** Allows the user to select an integer value.
- **Double Spin Box (`QDoubleSpinBox`):** Allows the user to select a floating-point number.
- **Slider (`QSlider`):** A horizontal or vertical slider for selecting a value.
- **Progress Bar (`QProgressBar`):** Displays the progress of an operation.
- **Dial (`QDial`):** A round widget for selecting a value, similar to a volume knob.
- **Calendar Widget (`QCalendarWidget`):** Provides a monthly calendar for date selection.
- **QListWidget**: Displays a list of items. Users can select one or multiple items.

- **QTreeWidget**: Shows data in a hierarchical tree structure with expandable and collapsible nodes.

- **QTableWidget**: Presents data in a table format with rows and columns, allowing for item-based data manipulation.

- **QTabWidget**: Provides a tabbed interface, enabling the organization of multiple widgets in tabs.

- **QGroupBox**: Encapsulates a group of widgets within a titled frame, often used to group related controls.

- **QLCDNumber**: Displays numbers in an LCD-like digital format.

- **QStackedWidget**: Manages a stack of widgets where only one widget is visible at a time, useful for creating wizards or multi-page forms.

- **QFrame**: Serves as a generic container widget with a frame, often used for grouping or separating other widgets visually.


In PyQt6, `QWidget` and `QMainWindow` are fundamental classes for creating graphical user interfaces.

# **QWidget**:

`QWidget` is the base class for all UI objects in PyQt6. It provides the basic functionality needed for all UI elements, including event handling, painting, and geometry management. Widgets can serve as containers for other widgets, allowing for the creation of complex interfaces. For example, a `QWidget` can contain buttons, labels, and other interactive elements.

**QMainWindow**:

`QMainWindow` is a specialized subclass of `QWidget` designed to create main application windows. It offers a framework for building standard application windows with features like menus, toolbars, status bars, and dockable widgets. The `QMainWindow` class provides specific areas for these components, including a central widget area where the main content is displayed. This structure facilitates the organization and management of complex interfaces.

**Key Differences**:

- **Structure**: `QMainWindow` includes predefined areas for menus, toolbars, and status bars, whereas `QWidget` does not.
- **Use Case**: `QWidget` is suitable for simple or custom widgets, while `QMainWindow` is ideal for main application windows requiring standard features.

# Policy Size and Stretches
In PyQt6, widgets can be resized and stretched to accommodate their contents or to fit within a layout
Example:

`

        #Size policy : how the widgets behaves if container space is expanded or shrunk.
        label = QLabel("Some text : ")
        line_edit = QLineEdit()

        
        line_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        `


# Displaying Images:

- QLabel: A versatile widget that can display both text and images.
- QPixmap: Handles image data and supports various formats.

`
app = QApplication(sys.argv)
label = QLabel()
pixmap = QPixmap('path_to_image.jpg')
label.setPixmap(pixmap)
label.resize(pixmap.width(), pixmap.height())
`

# Displaying Videos:

- QMediaPlayer: Manages media playback.
- QVideoWidget: Displays video content.
- QMediaDevices: Provides access to available media devices.

# QButtonGroup

  `QButtonGroup` is a non-visual container that manages the behavior of button widgets, such as QRadioButton, QCheckBox, or QPushButton. It allows you to group buttons together, enabling collective management of their states and simplifying signal handling.

`        # Create a QButtonGroup
        self.button_group = QButtonGroup(self)`

`#add a button to the group`
`
 self.button_group.addButton(radio_button, id=i)`

`# Connect the buttonClicked signal to a slot`
`self.button_group.buttonClicked.connect(self.on_button_clicked)`


---------------------------------------
Common methods and functions used with Python lists:

1. **`append(item)`**: Adds an item to the end of the list.
   ```python
   my_list.append(5)
   ```

2. **`extend(iterable)`**: Extends the list by appending elements from the iterable.
   ```python
   my_list.extend([6, 7, 8])
   ```

3. **`insert(index, item)`**: Inserts an item at a specified position.
   ```python
   my_list.insert(2, 'apple')
   ```

4. **`remove(item)`**: Removes the first occurrence of a specified item.
   ```python
   my_list.remove('apple')
   ```

5. **`pop([index])`**: Removes and returns the item at the given index; defaults to the last item if index is not specified.
   ```python
   last_item = my_list.pop()
   ```

6. **`clear()`**: Removes all items from the list.
   ```python
   my_list.clear()
   ```

7. **`index(item, [start, [end]])`**: Returns the index of the first occurrence of the item.
   ```python
   position = my_list.index('apple')
   ```

8. **`count(item)`**: Returns the number of occurrences of the item.
   ```python
   occurrences = my_list.count('apple')
   ```

9. **`sort(key=None, reverse=False)`**: Sorts the list in ascending order by default; can be customized with a key function and reverse flag.
   ```python
   my_list.sort()
   ```

10. **`reverse()`**: Reverses the elements of the list in place.
    ```python
    my_list.reverse()
    ```

11. **`copy()`**: Returns a shallow copy of the list.
    ```python
    new_list = my_list.copy()
    ```

12. **`len(list)`**: Returns the number of items in the list.
    ```python
    length = len(my_list)
    ```

13. **`max(list)`**: Returns the largest item in the list.
    ```python
    largest = max(my_list)
    ```

14. **`min(list)`**: Returns the smallest item in the list.
    ```python
    smallest = min(my_list)
    ```

15. **`sum(list)`**: Returns the sum of all numeric items in the list.
    ```python
    total = sum(my_list)
    ```

16. **`list(iterable)`**: Converts an iterable (e.g., tuple, string) into a list.
    ```python
    my_list = list('hello')
    ```

17. **`enumerate(iterable, start=0)`**: Returns an iterator of tuples containing indices and items from the iterable.
    ```python
    for index, item in enumerate(my_list):
        print(index, item)
    ```

18. **`filter(function, iterable)`**: Constructs an iterator from elements of the iterable for which the function returns true.
    ```python
    even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
    ```

19. **`map(function, iterable)`**: Applies a function to all items in the iterable and returns a map object.
    ```python
    squared_numbers = list(map(lambda x: x**2, my_list))
    ```

20. **`zip(*iterables)`**: Aggregates elements from multiple iterables into tuples.
    ```python
    paired = list(zip(list1, list2))
    ```

These methods and functions are fundamental for manipulating lists in Python. 

# 
