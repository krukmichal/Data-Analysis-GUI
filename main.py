from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
from pyqtgraph import PlotWidget, plot

from presenter.trendPresenter import TrendPresenter
from fileReader import readBasicFile

import sys
import logging
logging.basicConfig(level=logging.DEBUG)

import os

# TODO

# wczytywanie plikow
# pokazywanie pozycji kursora
# wlaczanie/wylaczanie trendow
# zapamietywanie srodowiska

## TREND_OBJECT = TREND_PLOT + TREND_ITEM 

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('view/mainwindow.ui', self)
        self.graphWidget.setBackground('w')

        self.actionBrowse.triggered.connect(self.browseFiles)
        self.trendList.itemSelectionChanged.connect(self.handleItemSelectionChanged)
        self.trendList.itemChanged.connect(self.handleItemChanged)
        self.currentSelectedTrend = None

    def handleItemSelectionChanged(self):
        item = self.trendList.selectedItems()[0]
        item.handleItemSelectionChanged()

    def handleItemChanged(self, item):
        item.handleItemChanged()

    #TO DO -> what if many files chosen, wrong file format
    def browseFiles(self):
        chosenFiles = QFileDialog.getOpenFileNames(
                parent=self,
                caption='Select a data file',
                )

        for trendPresenter in readFiles(chosenFiles)
            self.trendList.addItem(trendPresenter)

        self.trendList.setCurrentRow(self.trendList.count()-1)
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

