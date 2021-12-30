from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout, QListWidget, QMenu, QAction, QLabel
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np

from presenter.trendItem import TrendItem
from presenter.trendList import TrendList
from presenter.metricList import MetricList
from presenter.graphItem import GraphItem
from presenter.graphLayout import GraphLayout

from fileReader.fileReader import readFiles

import sys
import os
import logging
logging.basicConfig(level=logging.DEBUG)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Data Presenter")

        self.createMenuBar()
        self.setGeneralView()

        self.connectSignals()

    def setGeneralView(self):
        self.mainLayout = QVBoxLayout()
        self.trendLayout = QHBoxLayout()
        self.graphLayout = GraphLayout()

        self.trendList = TrendList(self.graphLayout)
        self.trendLayout.addWidget(self.trendList)

        self.trendLayout.addLayout(self.graphLayout) 
        self.mainLayout.addLayout(self.trendLayout)

        self.metricList = MetricList()
        self.mainLayout.addWidget(self.metricList);

        self.window = QtWidgets.QWidget(self)
        self.window.setLayout(self.mainLayout)
        self.setCentralWidget(self.window)

    def connectSignals(self):
        self.trendList.itemSelectionChanged.connect(self.handleItemSelectionChanged)

    def handleItemSelectionChanged(self):
        if len(self.trendList.selectedItems()) == 0:
            self.metricList.clear()
            return

        item = self.trendList.selectedItems()[0]
        self.metricList.showMetrics(item)

    def createMenuBar(self):
        self.menu = self.menuBar()
        self.fileMenu = self.menu.addMenu("&File")
        self.configureMenu = self.menu.addMenu("&Configure")
        self.helpMenu = self.menu.addMenu("&Help")
        self.transformMenu = self.menu.addMenu("&Transform")

        self.createMenuActions()

    #TODO MORE
    def createMenuActions(self):
        self.browseAction = QAction("&Browse", self)
        self.browseAction.triggered.connect(self.browseFiles)
        self.fileMenu.addAction(self.browseAction)

    #TO DO -> what if many files chosen, wrong file format??? 
    def browseFiles(self):
        fileDialogData = QFileDialog.getOpenFileNames(
                parent=self,
                caption='Select a data file',
                )

        for data in readFiles(fileDialogData[0]):
            logging.debug(data)
            self.trendList.addTrendItem(
                    np.array(data[1],dtype=float),
                    np.array(data[2],dtype=float),
                    data[0],
                    self.graphLayout.graphs[0]
                    )
