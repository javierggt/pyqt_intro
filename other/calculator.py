#!/usr/bin/env python3

import sys
from PyQt5 import QtCore as QtC, QtWidgets as QtW, QtGui as QtG


class Calculator(QtW.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtW.QGridLayout()

        self.text = QtW.QLineEdit()
        self.text.setReadOnly(True)

        self.numbers = [QtW.QPushButton(text=str(i)) for i in range(10)]
        self.c = QtW.QPushButton(text='C')
        self.pm = QtW.QPushButton(text='\xb1')
        self.dot = QtW.QPushButton(text='.')
        self.eq = QtW.QPushButton(text='=')
        self.div = QtW.QPushButton(text='/')
        self.mult = QtW.QPushButton(text='x')
        self.sum = QtW.QPushButton(text='+')
        self.sub = QtW.QPushButton(text='-')

        layout.addWidget(self.text, 0, 0, 1, 4)
        layout.addWidget(self.numbers[1], 4, 0)
        layout.addWidget(self.numbers[2], 4, 1)
        layout.addWidget(self.numbers[3], 4, 2)
        layout.addWidget(self.numbers[4], 3, 0)
        layout.addWidget(self.numbers[5], 3, 1)
        layout.addWidget(self.numbers[6], 3, 2)
        layout.addWidget(self.numbers[7], 2, 0)
        layout.addWidget(self.numbers[8], 2, 1)
        layout.addWidget(self.numbers[9], 2, 2)
        layout.addWidget(self.numbers[0], 5, 0, 1, 2)

        layout.addWidget(self.c, 1, 0)
        layout.addWidget(self.pm, 1, 1)
        layout.addWidget(self.dot, 5, 2)

        layout.addWidget(self.div, 1, 3)
        layout.addWidget(self.mult, 2, 3)
        layout.addWidget(self.sum, 3, 3)
        layout.addWidget(self.sub, 4, 3)
        layout.addWidget(self.eq, 5, 3)

        self.setLayout(layout)

        self.expr = ''
        self.op_last = False

        for n in self.numbers:
            n.clicked.connect(lambda clicked, button=n: self.add_digit(button.text()))
        self.dot.clicked.connect(lambda clicked: self.add_digit('.'))

        for op in [self.div, self.sum, self.sub]:
            op.clicked.connect(lambda clicked, button=op: self.add_operator(button.text()))
        self.mult.clicked.connect(lambda clicked, button=op: self.add_operator('*'))

        self.eq.clicked.connect(self.result)
        self.c.clicked.connect(self.clear)
        self.pm.clicked.connect(self.toggle_sign)

    def toggle_sign(self):
        text = self.text.text()
        if text:
            if text[0] == '-':
                self.text.setText(text[1:])
            else:
                self.text.setText('-' + text)

    def add_digit(self, char):
        if self.op_last:
            self.text.setText(char)
        else:
            self.text.setText(self.text.text() + char)
        self.op_last = False

    def add_operator(self, char):
        if not self.op_last:
            self.flush()
            self.expr += char
            self.op_last = True

    def result(self):
        self.flush()
        try:
            text = str(eval(self.expr))
            self.clear()
            self.text.setText(text)
        except:
            self.text.setText('syntax err')

    def flush(self):
        text = self.text.text()
        self.expr += f'({text})'

    def clear(self):
        self.text.setText('')
        self.expr = ''
        self.last = None


def main():
    app = QtW.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    app.exec()


main()
