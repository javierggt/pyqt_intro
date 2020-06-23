import sys
#import matplotlib
#matplotlib.use('Qt5Agg')

import numpy as np

from PyQt5 import QtWidgets as QtW

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure



class MainWindow(QtW.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        fig = Figure(figsize=(5, 4), dpi=100)
        sc = FigureCanvas(fig)

        axes = fig.subplots(1, 1)
        x = np.linspace(-10, 10, 51)
        y = np.cos(x/2) + 0.5*np.random.normal(size=51)
        axes.plot(x, y, '.', label='data')
        axes.set_xlabel('X')
        axes.set_ylabel('Y')
        axes.legend()
        fig.tight_layout()

        self.setCentralWidget(sc)

        self.show()


def main():
    app = QtW.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
