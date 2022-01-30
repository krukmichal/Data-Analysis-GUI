from PyQt5.QtWidgets import QListWidget
from PyQt5 import QtWidgets
import globalConfig as gc

class MetricList(QListWidget):
    def __init__(self):
        super(MetricList, self).__init__()
        self.setMaximumHeight(40)
        self.setFlow(QListWidget.LeftToRight)
        self.setSpacing(7)

        self.whichMetricsToShow = {
                "minValue" : True,
                "maxValue" : True,
                "peakToPeak" : True,
                "rms" : True,
                "arithmeticAverage" : True,
                "median" : True,
                "standardDeviation" : True,
                "variance" : True,
                "kurtosis" : True,
                "skewness" : True
                }

        self.metricName = {
                "minValue" : "Min",
                "maxValue" : "Max",
                "peakToPeak" : "Peak to Peak",
                "rms" : "Rms",
                "arithmeticAverage" : "Average",
                "median" : "Median",
                "standardDeviation" : "Standard Deviation",
                "variance" : "Variance",
                "kurtosis" : "Kurtosis",
                "skewness" : "Skewness"
                }

    def showMetrics(self, trendModel):
        self.clear()
        for key, value in self.whichMetricsToShow.items():
            if value:
                metricItem = QtWidgets.QListWidgetItem()
                name = self.metricName[key] + ": " + str(round(trendModel.metric[key], gc.precision))
                metricItem.setText(name)
                self.addItem(metricItem)
    

