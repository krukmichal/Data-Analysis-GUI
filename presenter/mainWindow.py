from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QVBoxLayout, QListWidget, QMenu, QAction, QLabel, QWidget, QMessageBox
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import numpy as np
import globalConfig as gc

from functools import partial

from presenter.trendItem import TrendItem
from presenter.trendList import TrendList
from presenter.metricList import MetricList
from presenter.graphItem import GraphItem
from presenter.graphLayout import GraphLayout
from presenter.graphList import GraphList
from presenter.matrixWindow import MatrixWindow
from presenter.groupBox import GroupBox
from fileio.fileReader import readFiles

from model.util import checkIfSameData

import sys
import os

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Data Presenter")

        self.setGeneralView()
        self.graphList.hide()

        self.createMenuBar()

        self.connectSignals()

    def setGeneralView(self):
        self.groupBox = GroupBox()

        self.mainLayout = QVBoxLayout()
        self.trendLayout = QHBoxLayout()
        self.graphLayout = GraphLayout(self.groupBox)
        self.graphList = GraphList(self.graphLayout)
        self.graphLayout.setGraphList(self.graphList)

        self.groupBox.setGraphLayout(self.graphLayout)

        self.trendList = TrendList(self.graphLayout)
        self.trendLayout.addWidget(self.trendList)

        self.trendLayout.addLayout(self.graphLayout) 
        self.mainLayout.addLayout(self.trendLayout)

        self.trendLayout.addWidget(self.graphList)

        self.mainLayout.addWidget(self.groupBox)

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
        self.viewMenu = self.menu.addMenu("&View")
        self.configureMenu = self.menu.addMenu("&Configure")
        self.statisticsMenu = self.menu.addMenu("&Statistics")
        self.metricMenu = self.viewMenu.addMenu("&Metrics")

        self.createMenuActions()

    def createMenuActions(self):
        self.browseAction = QAction("&Browse", self)
        self.browseAction.triggered.connect(self.browseFiles)
        self.fileMenu.addAction(self.browseAction)

        self.toggleGraphListAction = QAction("Graph List", checkable=True)
        self.toggleGraphListAction.setChecked(False)
        self.toggleGraphListAction.triggered.connect(lambda: self.toggleWidget(self.graphList))

        self.toggleTrendListAction = QAction("Trend List", checkable=True)
        self.toggleTrendListAction.setChecked(True)
        self.toggleTrendListAction.triggered.connect(lambda: self.toggleWidget(self.trendList))

        self.toggleMetricListAction = QAction("Metric List", checkable=True)
        self.toggleMetricListAction.setChecked(True)
        self.toggleMetricListAction.triggered.connect(lambda: self.toggleWidget(self.metricList))

        self.toggleGroupBoxAction = QAction("Group Box", checkable=True)
        self.toggleGroupBoxAction.setChecked(True)
        self.toggleGroupBoxAction.triggered.connect(lambda: self.toggleWidget(self.groupBox))

        self.markPoints = QAction("Mark Points", checkable=True)
        self.markPoints.triggered.connect(self.setMarkPoints)
        self.configureMenu.addAction(self.markPoints)

        self.minAction = QAction("Min Value", checkable=True)
        self.minAction.setChecked(True)
        self.minAction.triggered.connect(partial(self.changeShownMetric, "minVal"))

        self.maxAction = QAction("Max Value", checkable=True)
        self.maxAction.setChecked(True)
        self.maxAction.triggered.connect(partial(self.changeShownMetric, "maxVal"))

        self.ptpAction = QAction("Peak To Peak", checkable=True)
        self.ptpAction.setChecked(True)
        self.ptpAction.triggered.connect(partial(self.changeShownMetric, "peakToPeak"))

        self.averageAction = QAction("Average", checkable=True)
        self.averageAction.setChecked(True)
        self.averageAction.triggered.connect(partial(self.changeShownMetric, "arithmeticAverage"))

        self.medianAction = QAction("Median", checkable=True)
        self.medianAction.setChecked(True)
        self.medianAction.triggered.connect(partial(self.changeShownMetric, "median"))

        self.variationAction = QAction("Variation", checkable=True)
        self.variationAction.setChecked(True)
        self.variationAction.triggered.connect(partial(self.changeShownMetric, "variation"))

        self.standardDeviationAction = QAction("Standard Deviation", checkable=True)
        self.standardDeviationAction.setChecked(True)
        self.standardDeviationAction.triggered.connect(partial(self.changeShownMetric, "standardDeviation"))

        self.kurtosisAction = QAction("Kurtosis", checkable=True)
        self.kurtosisAction.setChecked(True)
        self.kurtosisAction.triggered.connect(partial(self.changeShownMetric, "kurtosis"))

        self.skewnessAction = QAction("Skewness", checkable=True)
        self.skewnessAction.setChecked(True)
        self.skewnessAction.triggered.connect(partial(self.changeShownMetric, "skewness"))

        self.viewMenu.addAction(self.toggleGraphListAction)
        self.viewMenu.addAction(self.toggleTrendListAction)
        self.viewMenu.addAction(self.toggleMetricListAction)
        self.viewMenu.addAction(self.toggleGroupBoxAction)

        self.metricMenu.addAction(self.minAction)
        self.metricMenu.addAction(self.maxAction)
        self.metricMenu.addAction(self.ptpAction)
        self.metricMenu.addAction(self.averageAction)
        self.metricMenu.addAction(self.medianAction)
        self.metricMenu.addAction(self.variationAction)
        self.metricMenu.addAction(self.standardDeviationAction)
        self.metricMenu.addAction(self.kurtosisAction)
        self.metricMenu.addAction(self.skewnessAction)

        self.covarianceAction = QAction("Covariance")
        self.covarianceAction.triggered.connect(partial(self.handleStatistic, "covariance"))
        self.correlationAction = QAction("Correlation")
        self.correlationAction.triggered.connect(partial(self.handleStatistic, "correlation"))

        self.statisticsMenu.addAction(self.covarianceAction)
        self.statisticsMenu.addAction(self.correlationAction)

    def handleStatistic(self, statsType):
        dataY = []
        names = []
        indices = []

        for i in range(self.trendList.count()):
            if self.trendList.item(i).checkState() == Qt.Checked:
                dataY.append(self.trendList.item(i).trendModel.dataY)
                names.append(self.trendList.item(i).text())
                indices.append(i)

        if len(indices) < 2:
            msgBox = QMessageBox()
            msgBox.setText("ERROR: Less then 2 trends selected")
            msgBox.exec_()
            return
        
        length = len(self.trendList.item(indices[0]).trendModel.dataX)
        for i in range(1,len(indices)):
            if len(self.trendList.item(indices[i]).trendModel.dataX) != length:
                print(len(self.trendList.item(indices[i]).trendModel.dataX))
                msgBox = QMessageBox()
                msgBox.setText("ERROR: data must be same length")
                msgBox.exec_()
                return

        matrixWindow = MatrixWindow(statsType, dataY, names)
        matrixWindow.show()
        matrixWindow.exec_()

    def changeShownMetric(self, metric):
        self.metricList.whichMetricsToShow[metric] = not self.metricList.whichMetricsToShow[metric]
        self.handleItemSelectionChanged()

    def setMarkPoints(self, test):
        if self.markPoints.isChecked():
            gc.symbol = 'o'
        else:
            gc.symbol = None

    def toggleWidget(self, widget):
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()

    def browseFiles(self):
        fileDialogData = QFileDialog.getOpenFileNames(
                parent=self,
                caption='Select a data file',
                )
        try:
            for data in readFiles(fileDialogData[0]):
                self.trendList.addTrendItem(
                        np.array(data[1],dtype=float),
                        np.array(data[2],dtype=float),
                        data[0],
                        self.graphLayout.graphs[0]
                        )
        except Exception as e: 
            msgBox = QMessageBox()
            msgBox.setText("Error while reading files " + str(e))
            msgBox.exec_()
