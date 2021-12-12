from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from model.trendModel import TrendModel
import globalConfig
import logging
logging.basicConfig(level=logging.DEBUG)

class TrendPresenter(QtWidgets.QListWidgetItem):
    def __init__(self, plotWidget, metricList, dataX, dataY, name):
        super().__init__()
        self.setText(name)
        self.setFlags(self.flags() | QtCore.Qt.ItemIsUserCheckable) # CZY TO POTRZEBNE
        self.setCheckState(QtCore.Qt.Checked)

        self.plotWidget = plotWidget
        self.metricList = metricList
        self.name = name
        self.color = globalConfig.setColor()
        self.trendModel = TrendModel(dataX, dataY)

        self.plot = self.plotWidget.plot(self.trendModel.dataX, self.trendModel.dataY, pen=self.color)
        #self.showMetrics() # not used right now -> handleItemSelectionChanged do this

    def handleItemSelectionChanged(self):
        logging.info("trendPresenter item selection changed")
        self.showMetrics()

    def handleItemChanged(self):
        logging.info("state changed")
        if self.checkState() == Qt.Checked:
            self.plot = self.plotWidget.plot(self.trendModel.dataX, self.trendModel.dataY, pen=self.color)
            logging.info("checked")
        else:
            self.plotWidget.removeItem(self.plot)
            logging.info("unchecked")

    def showMetrics(self):
        self.metricList.clear()

        for key, value in globalConfig.whichMetricsToShow.items():
            if value:
                metricItem = QtWidgets.QListWidgetItem()
                name = globalConfig.metricName[key] + ": " + str(round(self.trendModel.metric[key], globalConfig.precision))
                metricItem.setText(name)
                self.metricList.addItem(metricItem)
