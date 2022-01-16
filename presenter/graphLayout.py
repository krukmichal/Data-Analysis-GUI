import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout

from presenter.graphItem import GraphItem

class GraphLayout(QVBoxLayout):
    def __init__(self, groupBox):
        super(GraphLayout, self).__init__()

        self.groupBox = groupBox

        self.graphs = []
        self.initGraph()

    def initGraph(self):
        self.graphs.append(GraphItem(self.graphs, self.groupBox))
        self.addWidget(self.graphs[-1])

    def setGraphList(self, graphList):
        self.graphList = graphList

    def changeGraph(self, item, i):
        item.removePlot()
        item.graph = self.graphs[i]
        item.drawPlot()

    def newGraph(self, item):
        graphItem = GraphItem(self.graphs, self.groupBox)
        self.graphList.addNewGraph()
        self.graphs.append(graphItem)
        self.addWidget(graphItem)

        item.removePlot()
        item.graph = graphItem
        graphItem.drawPlot(item)

    def showGraph(self, i):
        self.graphs[i].show()
        self.graphs[i].isShown = True

    def hideGraph(self, i):
        self.graphs[i].hide()
        self.graphs[i].isShown = False

    def setRangeForEachGraph(self, startPos, endPos):
        for graph in self.graphs:
            graph.setRange(xRange=[startPos,endPos], padding=0)
            graph.setAutoVisible(y=True)

