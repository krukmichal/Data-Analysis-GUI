from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from model.trendModel import TrendModel
import pyqtgraph as pg
import globalConfig
import logging
logging.basicConfig(level=logging.DEBUG)

class TrendItem(QtWidgets.QListWidgetItem):
    def __init__(self, graph, dataX, dataY, name):
        super().__init__()
        self.setText(name)
        self.setFlags(self.flags() | QtCore.Qt.ItemIsUserCheckable) # CZY TO POTRZEBNE
        self.setCheckState(QtCore.Qt.Checked)

        self.graph = graph
        self.name = name
        self.color = globalConfig.setColor()
        self.trendModel = TrendModel(dataX, dataY)

        self.plot = None
        self.graph.drawPlot(self)

        #self.showMetrics() # not used right now -> handleItemSelectionChanged do this

    def handleItemChanged(self):
        logging.info("state changed")
        if self.checkState() == Qt.Checked:
            self.graph.drawPlot(self)
            logging.info("checked")
        else:
            self.graph.removeItem(self.plot)
            logging.info("unchecked")

    def removePlot(self):
        print(self.name)
        self.graph.removeItem(self.plot)

    def drawPlot(self):
        self.graph.drawPlot(self)


