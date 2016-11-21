import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import wolframalpha

client = wolframalpha.Client("2UKVAK-94LL934UKV")


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        # create objects
        label = QLabel(self.tr("Enter command and press Return"))
        self.le = QLineEdit()
        self.te = QTextEdit()

        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout)

        # create connection
        self.connect(self.le, SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        #print(type(self.le.text()))
        cmd = str(self.le.text())
        stdouterr = os.popen(cmd).read() ## i converted this to os.popen, list then string for printing #[1].read()
        self.te.setText(stdouterr)

if __name__ == "__main__":
    main()
