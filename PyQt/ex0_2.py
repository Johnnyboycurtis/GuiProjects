#implementing the following example using classes
#https://www.tutorialspoint.com/pyqt/pyqt_quick_guide.htm

## http://www.saltycrane.com/blog/2007/12/pyqt-example-how-to-run-command-and/


import sys
from PyQt4 import QtGui

class MyWindow(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.window_label = QtGui.QLabel(self)
        self.window_label.setText("Hello, world!")
        self.setGeometry(100, 100, 300, 300)
        self.window_label.move(50, 100)
        self.setWindowTitle("PyQt Window Here")
        #self.show()



def run_app():
    app = QtGui.QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    run_app()
