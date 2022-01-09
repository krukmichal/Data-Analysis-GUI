from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QEvent, Qt
from presenter.trendItem import TrendItem
from model import transforms

class GraphList(QListWidget):
    def __init__(self, graphLayout):
        super(GraphList, self).__init__()
        self.setMaximumWidth(120)
        self.itemChanged.connect(self.handleItemChanged)
        self.graphLayout = graphLayout
        self.isShown = True
        self.addNewGraph()

    def handleItemChanged(self, item):
        for i in range(len(self.graphLayout.graphs)):
            if self.item(i).checkState() == Qt.Checked:
                self.graphLayout.showGraph(i)
            else:
                self.graphLayout.hideGraph(i)

        #if item.checkState() == Qt.Checked:
        #    self.graphLayout.showGraph(self.row(item))            
        #else:
        #    self.graphLayout.hideGraph(self.row(item))            

    def addNewGraph(self):
        name = "graph " + str(len(self.graphLayout.graphs))
        newItem = QListWidgetItem(name)
        newItem.setFlags(newItem.flags() | QtCore.Qt.ItemIsUserCheckable) # CZY TO POTRZEBNE
        newItem.setCheckState(QtCore.Qt.Checked)
        self.addItem(newItem)
