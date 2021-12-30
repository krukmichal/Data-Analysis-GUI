from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction
from functools import partial

class TrendMenu(QtWidgets.QMenu):
    def __init__(self, trendList, item):
        super(TrendMenu, self).__init__()

        algorithms = self.addMenu("Algorithms")
        sma = algorithms.addAction("SMA")
        ema = algorithms.addAction("EMA")
        removePeaks = algorithms.addAction("Remove Peaks")
        fft = algorithms.addAction("FFT")

        changeGraph = self.addMenu("Change Graph")
        for i in range(len(trendList.graphLayout.graphs)):
            action = changeGraph.addAction("Graph " + str(i + 1))
            action.triggered.connect(partial(trendList.graphLayout.changeGraph, item, i))

        newGraph = changeGraph.addAction("New Graph")
        newGraph.triggered.connect(lambda: trendList.graphLayout.newGraph(item))

        configure = self.addAction("Configure")
        rename = self.addAction("Rename")
        delete = self.addAction("Delete")

        sma.triggered.connect(lambda: trendList.createSMAItem(item))
        ema.triggered.connect(lambda: trendList.createEMAItem(item))
        removePeaks.triggered.connect(lambda: trendList.createRemovePeaksItem(item))

        delete.triggered.connect(lambda: trendList.deleteTrendItem(item))

