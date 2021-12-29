import pyqtgraph as pg

class GraphItem(pg.PlotWidget):
    def __init__(self):
        super(GraphItem, self).__init__()

        self.setBackground('w')
        self.showGrid(x = True, y = True)

       # p1 = self.plotItem
       # p1.setLabels(left='axis 1')


    def drawPlot(self, trendItem):
        trendItem.plot = self.plot(
                trendItem.trendModel.dataX, 
                trendItem.trendModel.dataY, 
                pen=pg.mkPen(trendItem.color, width = 2))

