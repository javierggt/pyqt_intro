import sys
from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG


class Dialog(QtW.QDialog):
    text_changed = QtC.pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self._text = QtW.QLineEdit()
        layout = QtW.QVBoxLayout()
        layout.addWidget(self._text)
        layout2 = QtW.QHBoxLayout()
        self._cancel_button = QtW.QPushButton('Cancel')
        self._ok_button = QtW.QPushButton('OK')
        self._ok_button.setDefault(True)
        layout2.addWidget(self._cancel_button)
        layout2.addWidget(self._ok_button)
        layout.addLayout(layout2)
        self.setLayout(layout)

        self.accepted.connect(self._set_text)
        self._ok_button.released.connect(self.accept)
        self._cancel_button.released.connect(self.reject)

    def _set_text(self):
        self.text = self._text.text()


class Window(QtW.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtW.QLabel('Hello World!', self)
        self.label.setAlignment(QtC.Qt.AlignHCenter | QtC.Qt.AlignVCenter)
        self.button = QtW.QPushButton('Change text', self)

        layout = QtW.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.clicked)

    def clicked(self):
        dialog = Dialog(self)
        if dialog.exec():
            self.change_label(dialog.text)
    
    def change_label(self, label):
        self.label.setText(label)


def main():
    app = QtW.QApplication(sys.argv)
    with open('style.qss') as f:
        app.setStyleSheet(f.read())
    main_window = Window()
    main_window.show()
    app.exec()


main()
