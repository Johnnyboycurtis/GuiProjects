import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):

    def __init__(self, *args):
        super(MyWindow, self).__init__(*args)

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
        cmd = str(self.le.text())
        stdouterr = os.popen(cmd).read() ## https://docs.python.org/3/library/os.html#os.popen
        #(Note that the subprocess module provides more powerful facilities for spawning new processes and retrieving their results;
        #using that module is preferable to using these functions. Check especially the Replacing Older Functions with the subprocess Module section.)
        self.te.setText(stdouterr)

if __name__ == "__main__":
    main()
