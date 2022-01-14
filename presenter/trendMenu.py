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
        changeResolution = algorithms.addAction("Change Resolution")
        cut = algorithms.addAction("Cut")

        changeGraph = self.addMenu("Change Graph")
        for i in range(len(trendList.graphLayout.graphs)):
            action = changeGraph.addAction("Graph " + str(i + 1))
            action.triggered.connect(partial(trendList.graphLayout.changeGraph, item, i))

        newGraph = changeGraph.addAction("New Graph")
        newGraph.triggered.connect(lambda: trendList.graphLayout.newGraph(item))

        configure = self.addAction("Configure")
        export = self.addMenu("Export")
        exportTxt = export.addAction("To .txt")
        exportCsv = export.addAction("To .csv")

#        rename = self.addAction("Rename")
        delete = self.addAction("Delete")

        sma.triggered.connect(lambda: trendList.createSMAItem(item))
        ema.triggered.connect(lambda: trendList.createEMAItem(item))
        removePeaks.triggered.connect(lambda: trendList.createRemovePeaksItem(item))
        fft.triggered.connect(lambda: trendList.createFFTItem(item))
        changeResolution.triggered.connect(lambda: trendList.createNewResolutionItem(item))
        delete.triggered.connect(lambda: trendList.deleteTrendItem(item))
        exportTxt.triggered.connect(lambda: trendList.exportItemToTxt(item))
        exportCsv.triggered.connect(lambda: trendList.exportItemToCsv(item))
        cut.triggered.connect(lambda: trendList.createCutItem(item))

