
import sys
from PyQt4 import QtGui, QtCore

class myWindow(QtGui.QMainWindow):
	"""
	Class to create myWindow
	"""

	def __init__(self):
		super(myWindow, self).__init__()
		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("PyQt ex4.py")
		self.setWindowIcon(QtGui.QIcon("Harambe-president.jpg"))
		self.home()

	def close_window(self):
		sys.exit()

	def home(self):
		button = QtGui.QPushButton("Quit", self)
		button.clicked.connect(self.close_window)
		button.resize(button.sizeHint())
		button.move(12, 12)
		self.show()


def run():
	"runs the appliction"
	app = QtGui.QApplication(sys.argv)
	window = myWindow()
	sys.exit(app.exec_())



if __name__ == "__main__":

	run()
