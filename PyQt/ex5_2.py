## updated version of Example 5


import sys
from PyQt4 import QtGui, QtCore
from random_words import RandomWords

class MyWindow(QtCore.QObject):
    def __init__(self):
        super(MyWindow, self).__init__()

    self.textbox = QtGui.QLineEdit(self)





def run_app():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Random Word Generator")

    sys.exit(app.exec_())



if __name__ == "__main__":
    run_app()
