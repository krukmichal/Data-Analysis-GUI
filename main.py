from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout, QListWidget, QMenu, QAction, QLabel
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from presenter.mainWindow import MainWindow

import sys
import os

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.resize(1700, 800)
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
