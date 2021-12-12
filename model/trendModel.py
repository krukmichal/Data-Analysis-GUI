import model.calcMetric as calcMetric
import logging

class TrendModel():
    def __init__(self, X, Y):
        self.dataX = X
        self.dataY = Y

        self.metric = dict()
        self.calcAllMetrics()
    
    def calcAllMetrics(self):
        self.metric["arithmeticAverage"] = calcMetric.calcArithmeticAverage(self.dataY)
        self.metric["median"] = calcMetric.calcMedian(self.dataY)
        self.metric["variance"] = calcMetric.calcVariance(self.dataY, self.metric["arithmeticAverage"])
        self.metric["standardDeviation"] = calcMetric.calcStandardDeviation(self.metric["variance"])
