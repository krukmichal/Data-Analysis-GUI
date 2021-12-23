from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    view = pg.GraphicsView()
    l = pg.GraphicsLayout()
    view.show()
    window = QtWidgets.QWidget()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
