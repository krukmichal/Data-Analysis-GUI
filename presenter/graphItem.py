import pyqtgraph as pg
import globalConfig as gc

class GraphItem(pg.PlotWidget):
    def __init__(self):
        super(GraphItem, self).__init__()

        self.setBackground('w')
        self.showGrid(x = True, y = True)
        self.isShown = True

    def drawPlot(self, trendItem):
        trendItem.plot = self.plot(
                trendItem.trendModel.dataX, 
                trendItem.trendModel.dataY, 
                pen=pg.mkPen(trendItem.color, width = 2), symbol=gc.symbol)

