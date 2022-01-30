from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import Qt
from model.trendModel import TrendModel
import pyqtgraph as pg
import globalConfig as gc

class TrendItem(QtWidgets.QListWidgetItem):
    def __init__(self, graph, dataX, dataY, name, color):
        super().__init__()
        self.setText(name)
        self.setFlags(self.flags() | QtCore.Qt.ItemIsUserCheckable) # CZY TO POTRZEBNE
        self.setCheckState(QtCore.Qt.Checked)

        self.graph = graph
        self.name = name
        self.color = color
        self.trendModel = TrendModel(dataX, dataY)
        self.isChecked = Qt.Checked
    
        self.plot = None
        self.graph.drawPlot(self)

    def handleItemChanged(self):
        if self.checkState() == Qt.Checked:
            self.graph.drawPlot(self)
            self.isChecked = Qt.Checked
        else:
            self.graph.removeItem(self.plot)
            self.isChecked = Qt.Unchecked

    def removePlot(self):
        self.graph.removeItem(self.plot)

    def drawPlot(self):
        self.graph.drawPlot(self)

    def renamePlot(self, name):
        self.name = name
        self.removePlot()
        self.plot.setData(x=self.trendModel.dataX, y=self.trendModel.dataY, name = self.name)
        self.drawPlot()

    def setPosition(self, y):
        if y:
            y = round(y, gc.precision)
        self.setText(self.name + ": " + str(y))

    def changeColor(self, color):
        self.color = color
        self.removePlot()
        self.drawPlot()
