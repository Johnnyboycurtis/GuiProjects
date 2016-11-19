#example from
#https://pythonspot.com/en/pyqt4-textbox/

import sys
from PyQt4 import QtCore, QtGui


def run_app(title):
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.setWindowTitle(title)

    textbox = QtGui.QLineEdit(w)
    textbox.move(10, 10)
    textbox.resize(280, 40)

    w.resize(400, 400)

    button1 = QtGui.QPushButton("Press me", w)
    button1.move(100, 80)

    ## create the actions
    @QtCore.pyqtSlot()
    def on_click():
        textbox.setText("Button was clicked")

    button1.clicked.connect(on_click)




    w.show()
    sys.exit(app.exec_())





if __name__ == "__main__":
    run_app("new window app")
