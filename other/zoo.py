#!/usr/bin/env python3

import PyQt5.QtWidgets as QtW, PyQt5.QtCore as QtC, PyQt5.QtGui as QtG

# Only needed for access to command line arguments
import sys


class MainWindow(QtW.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QtW.QVBoxLayout()
        widgets = [QtW.QCheckBox,
                   QtW.QComboBox,
                   QtW.QDateEdit,
                   QtW.QDateTimeEdit,
                   QtW.QDial,
                   QtW.QDoubleSpinBox,
                   QtW.QFontComboBox,
                   QtW.QLCDNumber,
                   QtW.QLabel,
                   QtW.QLineEdit,
                   QtW.QProgressBar,
                   QtW.QPushButton,
                   QtW.QRadioButton,
                   QtW.QSlider,
                   QtW.QSpinBox,
                   QtW.QTimeEdit]

        for w in widgets:
            layout.addWidget(w())

        widget = QtW.QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


def main():
    app = QtW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

main()
