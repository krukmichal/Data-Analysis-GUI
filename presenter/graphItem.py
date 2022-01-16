import pyqtgraph as pg
import globalConfig as gc
import numpy as np

class GraphItem(pg.PlotWidget):
    def __init__(self, graphs, groupBox):
        super(GraphItem, self).__init__()

        self.graphs = graphs
        self.groupBox = groupBox

        self.setBackground('w')
        self.showGrid(x = True, y = True)
        self.isShown = True
        self.addLegend()

        self.getAxis('left').setWidth(50)

        pen = pg.mkPen(color=(130,21,190), width=0.6)

        self.vLine = pg.InfiniteLine(angle=90, movable=False,pen=pen)
        self.hLine = pg.InfiniteLine(angle=0, movable=False, pen=pen)
        self.addItem(self.vLine, ignoreBounds=True)
        self.addItem(self.hLine, ignoreBounds=True)

        #self.cursorlabel = pg.TextItem(anchor=(-1,10))
        #self.addItem(self.cursorlabel)

        self.scene().sigMouseMoved.connect(self.mouseMoved)
        self.sigRangeChanged.connect(self.onSigRangeChanged)

    def drawPlot(self, trendItem):
        trendItem.plot = self.plot(
                trendItem.trendModel.dataX, 
                trendItem.trendModel.dataY, 
                pen=pg.mkPen(trendItem.color, width = 2), symbol=gc.symbol, name=trendItem.name)

    def onSigRangeChanged(self, r):
        self.enableAutoRange(axis='y')
        self.setAutoVisible(y=True)
        ax = self.getAxis('bottom')

        for graph in self.graphs:
            if graph != self:
                graph.blockSignals(True)
                graph.setRange(xRange=ax.range, padding=0)
                graph.blockSignals(False)
        
    def mouseMoved(self, evt):
            pos = evt
            if self.sceneBoundingRect().contains(pos):
                mousePoint = self.plotItem.vb.mapSceneToView(pos)
                #index = int(mousePoint.x())
                # if index > 0 and index < self.MFmax:
                #if index > 0:
                #    self.cursorlabel.setHtml(
                #        "<span style='font-size: 12pt'>x={:0.1f}, \
                #         <span style='color: red'>y={:0.1f}</span>".format(
                #    mousePoint.x(), mousePoint.y()))
                self.vLine.setPos(mousePoint.x())
                self.hLine.setPos(mousePoint.y())

                print(str(mousePoint.x()) + ", " + str(mousePoint.y()))
                self.groupBox.setXText(str(mousePoint.x()))
                self.groupBox.setYText(str(mousePoint.y()))
