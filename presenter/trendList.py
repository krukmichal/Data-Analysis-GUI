from PyQt5.QtWidgets import QListWidget 
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from presenter.trendMenu import TrendMenu
from presenter.trendItem import TrendItem
from model import transforms

class TrendList(QListWidget):
    def __init__(self, graphs):
        super(TrendList, self).__init__()
        self.setMaximumWidth(200)
        self.itemChanged.connect(self.handleItemChanged)
        self.installEventFilter(self)

        self.graphs = graphs

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

    def addTrendItem(self, dataX, dataY, name):
        trendItem = TrendItem(self.graphs[0], dataX, dataY, name)
        self.addItem(trendItem)
        self.setCurrentRow(self.count()-1)

    def createSMAItem(self, item):
        Y = transforms.calcSMA(item.trendModel.dataY, 20)
        name = item.name + "-SMA"
        self.addTrendItem(item.trendModel.dataX.copy(), Y, name)

    def createEMAItem(self, item):
        alpha = 0.1
        Y = transforms.calcEMA(item.trendModel.dataY, 20, alpha)
        name = item.name + "-EMA"
        self.addTrendItem(item.trendModel.dataX.copy(), Y, name)

    def createRemovePeaksItem(self, item):
        threshold = 1.7
        Y = transforms.removePeaks(item.trendModel.dataY, threshold)
        name = item.name + "-RP"
        self.addTrendItem(item.trendModel.dataX.copy(), Y, name)






