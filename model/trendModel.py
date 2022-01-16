import model.calcMetric as calcMetric
import logging
import numpy as np

class TrendModel():
    def __init__(self, X, Y):
        self.dataX = X
        self.dataY = Y

        self.metric = dict()
        self.calcAllMetrics()
    
    def calcAllMetrics(self):
        self.metric["minValue"] = calcMetric.findMin(self.dataY)
        self.metric["maxValue"] = calcMetric.findMax(self.dataY)
        self.metric["peakToPeak"] = calcMetric.peakToPeak(self.metric["maxValue"], self.metric["minValue"])
        self.metric["arithmeticAverage"] = calcMetric.calcArithmeticAverage(self.dataY)
        self.metric["median"] = calcMetric.calcMedian(self.dataY)
        self.metric["variance"] = calcMetric.calcVariance(self.dataY, self.metric["arithmeticAverage"])
        self.metric["standardDeviation"] = calcMetric.calcStandardDeviation(self.metric["variance"])
        self.metric["skewness"] = calcMetric.calcSkewness(
                self.metric["arithmeticAverage"], 
                self.metric["median"], 
                self.metric["standardDeviation"]
                )
        self.metric["kurtosis"] = calcMetric.calcKurtosis(
                self.dataY, 
                self.metric["arithmeticAverage"],
                self.metric["standardDeviation"]
                )

