import sys
from PyQt5 import QtWidgets as QtW


class Window(QtW.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtW.QLabel('Hello World', self)
        

def main():
    app = QtW.QApplication([])
    main_window = Window()
    main_window.show()
    app.exec()


main()
