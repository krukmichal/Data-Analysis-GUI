from model.calcMetric import *
import numpy as np
import math

def test_calcMedian():
    X = np.array([2,1,2])
    median = calcMedian(X)
    assert median == 2

def test_calcAverage():
    X = np.array([1,2,3,4,5,6])
    average = calcArithmeticAverage(X)
    assert average == 3.5

def test_calcAverage2():
    X = np.array([0.1, 0.5, 6.5])
    avg = calcArithmeticAverage(X)
    assert round(avg,2) == 2.37

def test_standardDeviation():
    X = np.array([1,5])
    mean = calcArithmeticAverage(X)
    assert mean == 3
    variance = calcVariance(X, mean)
    assert variance == 4
    sd = calcStandardDeviation(variance)
    assert sd == 2

def test_calcSkewness():
    X = np.array([1,2,3,4,5,6])

    mean = calcArithmeticAverage(X)
    assert mean == 3.5

    median = calcMedian(X)
    assert median == 3.5

    variance = calcVariance(X, mean)
    standardDeviation = calcStandardDeviation(variance)

    assert np.around(standardDeviation, 4) == 1.7078

    result = calcSkewness(mean, median, standardDeviation)

    assert result == 0
    
def test_calcKurtosis():
    X = np.array([55, 78, 65, 98, 97, 60, 67, 65, 83, 65])
    assert np.isclose(calcKurtosis(X), 2.0453729382893178)

def test_minValue():
    Y = [1,2,65,1,45,0,1,6,54]
    assert findMin(Y) == 0

def test_maxValue():
    Y = [-3,2,55,12,1,1,1,1,2,5,2,99]
    assert findMax(Y) == 99

def test_calcRMS0():
    Y = np.array([1,1,1])
    assert calcArithmeticAverage(Y) == calcRMS(Y)

def test_calcRMS1():
    Y = np.array([1,2,3])
    assert calcRMS(Y) == math.sqrt((1+4+9)/3)
