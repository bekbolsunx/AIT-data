import sys  # Import the sys module for system-related functionality
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit  # Import necessary classes from PyQt5 for GUI
from PyQt5.QtCore import QSize  # Import QSize class from PyQt5 for specifying widget sizes
from PyQt5.QtGui import QFont  # Import QFont class from PyQt5 for setting font properties

from random import randint  # Import the randint function from the random module

# Define a class named AIT that inherits from QWidget
class AIT(QWidget):
    # Define the constructor (initialization method) for the AIT class
    def __init__(self):
        # Call the constructor of the parent class (QWidget)
        super().__init__()

        # Initialize QLabel widgets for displaying numbers, operator, equal sign, and user input
        self.label1 = QLabel("Label1")
        self.label2 = QLabel("Label2")
        self.operator = QLabel("OPS")
        self.equal = QLabel("=")
        self.result = QLineEdit("")

        # Create a horizontal layout to arrange the QLabel widgets and QLineEdit widget
        self.operation_layout = QHBoxLayout()
        self.operation_layout.addWidget(self.label1)
        self.operation_layout.addWidget(self.operator)
        self.operation_layout.addWidget(self.label2)
        self.operation_layout.addWidget(self.equal)
        self.operation_layout.addWidget(self.result)

        # Initialize QPushButton widgets for OK, RETRY, and NEXT actions
        self.button_ok = QPushButton("OK")
        self.button_retry = QPushButton("RETRY")
        self.button_next = QPushButton("NEXT")

        # Connect button clicks to corresponding methods
        self.button_next.clicked.connect(self.generate_random_number)
        self.button_retry.clicked.connect(self.clear_result)
        self.button_ok.clicked.connect(self.check_result)

        # Add buttons to the horizontal layout
        self.operation_layout.addWidget(self.button_ok)
        self.operation_layout.addWidget(self.button_retry)
        self.operation_layout.addWidget(self.button_next)

        # Generate a random arithmetic operation and display it
        self.generate_random_number()

        # Set the layout of the main window to the horizontal layout
        self.setLayout(self.operation_layout)

        # Set window properties such as title and fixed size
        self.setWindowTitle("Вычислите")
        self.setFixedSize(QSize(500, 500))

        # Display the main window
        self.show()

    # Method to check the user's result against the correct answer
    def check_result(self):
        # Retrieve values from labels and operator, convert them to integers
        v1 = int(self.label1.text())
        v2 = int(self.label2.text())
        op = self.operator.text()

        # Perform addition or subtraction based on the operator
        if op == '+':
            result = v1 + v2
        else:
            result = v1 - v2

        # Compare the result with the user's input and update the result field's background color
        if result == int(self.result.text()):
            self.result.setStyleSheet("background-color :green")
        else:
            self.result.setStyleSheet("background-color :red")

    # Method to clear the user's input and reset the result field's background color
    def clear_result(self):
        self.result.setText("")
        self.result.setStyleSheet("background-color:white")

    # Method to generate random numbers and operator for a new arithmetic operation
    def generate_random_number(self):
        # Clear the user's input and reset the result field's background color
        self.result.setText("")
        self.result.setStyleSheet("background-color:white")

        # Generate two random numbers and an operator
        val1 = randint(10, 99)
        val2 = randint(10, 99)
        op = ['+', '-'][randint(0, 1)]

        # Ensure correct order of values for subtraction
        if op == '-':
            if val1 < val2:
                val1, val2 = val2, val1

        # Update labels and operator with generated values
        self.label1.setText(str(val1))
        self.label2.setText(str(val2))
        self.operator.setText(op)

# Check if the script is being run directly
if __name__ == "__main__":
    # Create a QApplication instance
    app = QApplication(sys.argv)
    
    # Create an instance of the AIT class
    counter = AIT()

    # Start the application's event loop and exit when it's done
    sys.exit(app.exec_())
