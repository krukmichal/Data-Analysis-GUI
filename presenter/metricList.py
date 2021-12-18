from PyQt5.QtWidgets import QListWidget
from PyQt5 import QtWidgets
import globalConfig
import logging

class MetricList(QListWidget):
    def __init__(self):
        super(MetricList, self).__init__()
        self.setMaximumHeight(30)
        self.setFlow(QListWidget.LeftToRight)
        self.precision = 4

        self.whichMetricsToShow = {
                "arithmeticAverage" : True,
                "median" : True,
                "standardDeviation" : True,
                "variance" : True
                }

        self.metricName = {
                "arithmeticAverage" : "Average",
                "median" : "Median",
                "standardDeviation" : "Standard Deviation",
                "variance" : "Variance"
                }

    def showMetrics(self, item):
        logging.info("showMetrics")
        self.clear()

        for key, value in self.whichMetricsToShow.items():
            if value:
                metricItem = QtWidgets.QListWidgetItem()
                name = self.metricName[key] + ": " + str(round(item.trendModel.metric[key], self.precision))
                metricItem.setText(name)
                self.addItem(metricItem)
