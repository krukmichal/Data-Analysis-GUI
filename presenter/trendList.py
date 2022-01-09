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

        self.symbol = None
        self.color = ['r', 'b', 'g', 'y', 'c', 'k']
        self.currentColor = 0

    def setDefaultColor(self):
        res = self.color[self.currentColor]
        self.currentColor = (self.currentColor + 1) % len(self.color)
        return res

    def handleItemChanged(self, item):
        item.handleItemChanged()

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self:

            item = source.itemAt(event.pos())
            
            if item is not None:
                menu = TrendMenu(self, item)
                menu.exec_(event.globalPos())

            return True;

        return super().eventFilter(source, event)

    def addTrendItem(self, dataX, dataY, name, graph):
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
        Y = transforms.calcSMA(item.trendModel.dataY, 20)
        name = item.name + "-SMA"
        self.addTrendItem(item.trendModel.dataX.copy(), Y, name, item.graph)

    def createEMAItem(self, item):
        alpha = 0.1
        Y = transforms.calcEMA(item.trendModel.dataY, 20, alpha)
        name = item.name + "-EMA N=" + str(20)
        self.addTrendItem(item.trendModel.dataX.copy(), Y, name, item.graph)

    def createRemovePeaksItem(self, item):
        threshold = 1.7
        Y = transforms.removePeaks(item.trendModel.dataY, threshold)
        name = item.name + "-RP"
        self.addTrendItem(item.trendModel.dataX.copy(), Y, name, item.graph)

    def checkIfEqualIntervals(self, X):
        if len(X) >  1:
            interval = X[1] - X[0]

            for i in range(len(X) - 1):
                if X[i+1] - X[i] != interval:
                    return False

        return True

    def createFFTItem(self, item):
        if not self.checkIfEqualIntervals(item.trendModel.dataX):
            print("NOT EQUAL INTERVALS")
            return

        X, Y = transforms.calcFFT(item.trendModel.dataX, item.trendModel.dataY)
        name = item.name + "-FFT"
        self.addTrendItem(X, Y, name, item.graph)

    def deleteTrendItem(self, item):
        item.removePlot()
        index = self.indexFromItem(item)
        self.takeItem(index.row())

    def createNewResolutionItem(self, item):
        resolution, done = QtWidgets.QInputDialog.getDouble(
                self, "Input Dialog", 'Enter resulution:')
    
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



