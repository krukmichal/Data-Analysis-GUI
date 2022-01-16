from PyQt5.QtWidgets import QListWidget, QMessageBox, QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from presenter.trendMenu import TrendMenu
from presenter.trendItem import TrendItem
from model import transforms
from fileio.fileWriter import *

class TrendList(QListWidget):
    def __init__(self, graphLayout):
        super(TrendList, self).__init__()
        self.setMaximumWidth(200)
        self.itemChanged.connect(self.handleItemChanged)
        self.installEventFilter(self)
        self.graphLayout = graphLayout

        self.colors = ['red', 'green', 'blue', 'yellow', 'purple', 'pink', 'darkGreen', 'black', 'orange', 'cyan']
        self.colorsRGB = {
                'red' : (255,0,0),
                'green' : (0,255,0),
                'blue' : (0,0,255),
                'yellow' : (255,255,0),
                'purple' : (153,0,153),
                'pink' : (255,51,255),
                'darkGreen': (52,102,0),
                'black' : (0,0,0),
                'orange' : (205,102,0),
                'cyan' : (51,255,255)
                }

        self.currentColor = 0

    def setDefaultColor(self):
        color = self.colors[self.currentColor]
        self.currentColor = (self.currentColor + 1) % len(self.colors)
        return self.colorsRGB[color]

    def handleItemChanged(self, item):
        if item.text() == item.name:
            item.handleItemChanged()
        else:
            item.renamePlot(item.text())

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self:

            item = source.itemAt(event.pos())
            
            if item is not None:
                menu = TrendMenu(self, item)
                menu.exec_(event.globalPos())

            return True;

        return super().eventFilter(source, event)

    def addTrendItem(self, dataX, dataY, name, graph):
        if len(dataX)  == 0:
            return # there is no data provided

        trendItem = TrendItem(
                graph, 
                dataX, 
                dataY, 
                name, 
                self.setDefaultColor()
                )
        self.addItem(trendItem)
        self.setCurrentRow(self.count()-1)

    def createSMAItem(self, item):
        N, done = QtWidgets.QInputDialog.getInt(self, "Simple Moving Average", 'Enter N:', 1, 1, len(item.trendModel.dataY))

        if done:
            Y = transforms.calcSMA(item.trendModel.dataY, N)
            name = item.name + "-SMA N=" + str(N)
            self.addTrendItem(item.trendModel.dataX.copy(), Y, name, item.graph)

    def createEMAItem(self, item):
        N, done = QtWidgets.QInputDialog.getInt(self, "Exponential Moving Average", 'Enter N:', 1, 1, len(item.trendModel.dataY))

        if done:
            alpha = 2 / (N + 1)
            Y = transforms.calcEMA(item.trendModel.dataY, N, alpha)
            name = item.name + "-EMA N=" + str(N)
            self.addTrendItem(item.trendModel.dataX.copy(), Y, name, item.graph)

    def createRemovePeaksItem(self, item):
        threshold, done = QtWidgets.QInputDialog.getDouble(self, "Remove Peaks", 'Set threshold', 1, 0.00001, 10000000, 5)

        if done:
            Y = transforms.removePeaks(item.trendModel.dataY, threshold)
            name = item.name + "-RP"
            self.addTrendItem(item.trendModel.dataX.copy(), Y, name, item.graph)

    def createFFTItem(self, item):
        X, Y = transforms.calcFFT(item.trendModel.dataX, item.trendModel.dataY)
        name = item.name + "-FFT"
        self.addTrendItem(X, Y, name, item.graph)

    def deleteTrendItem(self, item):
        item.removePlot()
        index = self.indexFromItem(item)
        self.takeItem(index.row())

    def createNewResolutionItem(self, item):
        resolution, done = QtWidgets.QInputDialog.getDouble(self, "Change Resolution", 'Enter resolution:', 1, 0.00001, 10000000, 5)
    
        if done:
            X,Y = transforms.changeResolutionLinear(
                    item.trendModel.dataX, 
                    item.trendModel.dataY, 
                    resolution
                    )

            name = item.name + "-res-" + str(resolution)
            self.addTrendItem(X, Y, name, item.graph)

    def exportItemToTxt(self, item):
        name = QFileDialog.getSaveFileName(self, 'SaveFile')[0]
        writeTxtFile(item.trendModel.dataX, item.trendModel.dataY, name)
        
    def exportItemToCsv(self, item):
        name = QFileDialog.getSaveFileName(self, 'SaveFile')[0]
        writeCsvFile(item.trendModel.dataX, item.trendModel.dataY, name)

    def createCutItem(self, item):
        startPoint, done1 = QtWidgets.QInputDialog.getDouble(self, "Cut Trend", 'Start point', 1, 0.00001, 10000000, 5)
        endPoint, done2 = QtWidgets.QInputDialog.getDouble(self, "Cut Trend", 'End point', 1, 0.00001, 10000000, 5)

        if done1 and done2:
            X, Y = transforms.cutTrend(item.trendModel.dataX, item.trendModel.dataY, startPoint, endPoint)
            name = item.name + "-cut-" + str(startPoint) + "-" + str(endPoint)
            self.addTrendItem(X, Y, name, item.graph)
