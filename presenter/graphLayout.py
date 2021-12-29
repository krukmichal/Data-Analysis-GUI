import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout

from presenter.graphItem import GraphItem

class GraphLayout(QVBoxLayout):
    def __init__(self):
        super(GraphLayout, self).__init__()

        self.graphs = []
        self.initGraph()

    def initGraph(self):
        self.graphs.append(GraphItem())
        self.addWidget(self.graphs[-1])

    def changeGraph(self, item, i):
        print(i)
        item.removePlot()
        item.graph = self.graphs[i]
        item.drawPlot()

    def newGraph(self, item):
        graphItem = GraphItem()
        self.graphs.append(graphItem)
        self.addWidget(graphItem)

        item.removePlot()
        item.graph = graphItem
        graphItem.drawPlot(item)

