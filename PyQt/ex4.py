
import sys
from PyQt4 import QtGui, QtCore
from random_words import RandomWords




class newWindow(QtGui.QMainWindow):
    """
    this creates a new Qt window
    """

    def __init__(self):
        super(newWindow, self).__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("New Qt Window")
        self.setWindowIcon(QtGui.QIcon("Harambe-president.jpg"))
        self.QuitButton()
        self.secondbutton()

        self.wordhistory = []

        self.statusBar()
        mainMenu = self.menuBar()
        fileMenue = mainMenu.addMenu("&File")
        fileMenue.addAction(self.file_quit())


        self.show() ## needs to be placed after buttons

    def file_quit(self):
        """
        Function for including a quit method inside File menu in menu bar
        """
        extractAction = QtGui.QAction("&Exit the app", self)
        extractAction.setShortcut("CTRL+Q")
        extractAction.setStatusTip("Quit the app")
        extractAction.triggered.connect(self.close_window)
        return extractAction

    def close_window(self):
        "Method for exiting the application"
        print(self.wordhistory)
        sys.exit()

    def words(self):
        "Method for generating random words using the random_words module"
        rw = RandomWords()
        a = rw.random_word()
        self.wordhistory.append(a)
        print(a)

    def secondbutton(self):
        "Second button for printing some random words"
        button2 = QtGui.QPushButton("Print some words", self)
        button2.clicked.connect(self.words)
        button2.resize(button2.sizeHint())
        button2.move(40,100) ## position of button

        #self.show()


    def QuitButton(self):
        "Method for creating the on screen Quit button"
        button = QtGui.QPushButton("Quit", self)
        button.clicked.connect(self.close_window)
        button.resize(button.sizeHint())
        button.move(40,10) ## position of button
        #self.show()

def run():
    "function to run the module"
    app = QtGui.QApplication(sys.argv)
    window = newWindow() ## already takes in QtGui.QMainWindow
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()




## end of file ##
