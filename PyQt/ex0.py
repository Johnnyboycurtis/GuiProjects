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

from PyQt4 import QtGui


def window():
	app = QtGui.QApplication(sys.argv)

	window = QtGui.QWidget()
	window.setGeometry(50, 50, 500, 500)
	window.setWindowTitle("PyQT Title: ex0.py")
	window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	window()




