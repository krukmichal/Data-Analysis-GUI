from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction

class TrendMenu(QtWidgets.QMenu):
    def __init__(self, trendList, item):
        super(TrendMenu, self).__init__()

        sma = self.addAction("sma")
        ema = self.addAction("ema")
        fft = self.addAction("fft")
        rename = self.addAction("rename")
        delete = self.addAction("delete")

        sma.triggered.connect(lambda: trendList.createSMAItem(item))
        ema.triggered.connect(lambda: trendList.createEMAItem(item))
