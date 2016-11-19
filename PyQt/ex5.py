#!/usr/bin/env python
#-*- coding:utf-8 -*-

# http://stackoverflow.com/questions/15637768/pyqt-how-to-capture-output-of-pythons-interpreter-and-display-it-in-qedittext

import sys
from PyQt4 import QtGui, QtCore
from random_words import RandomWords

class MyStream(QtCore.QObject):
    """New signals should only be defined in sub-classes of QObject. """
    message = QtCore.pyqtSignal(str)
    #counts = 0

    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message_pyqtSignal):
        self.message.emit(str(message_pyqtSignal))

    def flush(self):
        #self.counts += 1
        #return self.counts
        return None

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonPrint = QtGui.QPushButton(self)
        self.pushButtonPrint.setText("Click Me!")
        self.pushButtonPrint.clicked.connect(self.on_pushButtonPrint_clicked)

        self.textEdit = QtGui.QTextEdit(self)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPrint)
        self.layoutVertical.addWidget(self.textEdit)

    @QtCore.pyqtSlot()
    def on_pushButtonPrint_clicked(self):
        rw = RandomWords()
        print(rw.random_word())

    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(message)



def run_app(window_name):
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName(window_name)

    window = MyWindow()
    window.show()

    myStream = MyStream()
    myStream.message.connect(window.on_myStream_message)

    sys.stdout = myStream

    #sys.stdout.flush()

    sys.exit(app.exec_())


if __name__ == "__main__":

    run_app("PyQt Window")
