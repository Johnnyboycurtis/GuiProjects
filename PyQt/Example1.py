#!/usr/bin/python

## Example 1

"""
Creating a simple GUI application using PyQt involves the following steps:

1. Import QtGui module.

2. Create an application object.

3. A QWidget object creates top level window. Add QLabel object in it.

4. Set the caption of label as "hello world"

5. Define the size and position of window by setGeometry() method

6. Enter the mainloop of application by app.exec_() method.
"""


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def b1_clicked():
	print "Hi there!"

def b2_clicked():
	print "You called?"



def pyqt_window():
    myapp = QApplication(sys.argv)


    window = QDialog()

    b1 = QPushButton(window)
    b1.setText("Button 1")
    b1.move(55, 25)
    b1.clicked.connect(b1_clicked)

    b2 = QPushButton(window)
    b2.setText("Button 2")
    b2.move(55, 55)
    QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)



    #window.setGeometry(100, 100, 200, 100)
    window.setGeometry(10, 10, 300, 300)
    window.setWindowTitle("Window Title: PyQt")
    window.show()
    sys.exit(myapp.exec_())
    

if __name__ == '__main__':
    pyqt_window()



