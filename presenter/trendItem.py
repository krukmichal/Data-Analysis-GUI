from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from model.trendModel import TrendModel
import pyqtgraph as pg
import logging
logging.basicConfig(level=logging.DEBUG)

class TrendItem(QtWidgets.QListWidgetItem):
    def __init__(self, graph, dataX, dataY, name, color):
        super().__init__()
        self.setText(name)
        self.setFlags(self.flags() | QtCore.Qt.ItemIsUserCheckable) # CZY TO POTRZEBNE
        self.setCheckState(QtCore.Qt.Checked)

        self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)

        self.graph = graph
        self.name = name
        self.color = color
        self.trendModel = TrendModel(dataX, dataY)
    

        self.plot = None
        self.graph.drawPlot(self)

    def handleItemChanged(self):
        if self.checkState() == Qt.Checked:
            self.graph.drawPlot(self)
        else:
            self.graph.removeItem(self.plot)

    def removePlot(self):
        self.graph.removeItem(self.plot)

    def drawPlot(self):
        self.graph.drawPlot(self)
