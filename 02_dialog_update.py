import sys
from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG


class Dialog(QtW.QDialog):
    text_changed = QtC.pyqtSignal(str)
    
    def __init__(self, parent):
        super().__init__(parent)
        self.text = QtW.QLineEdit()
        layout = QtW.QVBoxLayout()
        layout.addWidget(self.text)
        self.setLayout(layout)
        
        self.text.textChanged.connect(self.text_changed)
        
class Window(QtW.QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QtW.QLabel('Hello World!')
        self.button = QtW.QPushButton('Change text')
        
        layout = QtW.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        
        self.button.clicked.connect(self.clicked)
        
    def clicked(self, event):
        dialog = Dialog(self)
        dialog.setModal(True)
        dialog.text_changed.connect(self.change_label)
        dialog.show()
    
    def change_label(self, label):
        self.label.setText(label)


def main():
    app = QtW.QApplication([])
    main_window = Window()
    main_window.show()
    app.exec()


main()
