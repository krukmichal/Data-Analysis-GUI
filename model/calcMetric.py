import math
import numpy as np

from scipy import stats

def calcArithmeticAverage(X):
    result = 0
    for x in X:
        result += x
    return result / len(X)

def calcMedian(X):
    Y = X.copy()
    Y.sort()
    if len(Y) % 2 == 0:
        return (Y[len(Y) // 2] + Y[len(Y) // 2 - 1]) / 2
    return Y[len(Y) // 2]

def calcStandardDeviation(variance):
    return math.sqrt(variance)

def calcVariance(X, average):
    res = 0
    for x in X:
        res += (x - average) ** 2
    return res / len(X)

def calcSkewness(average, median, standardDeviation):
    return 3 * (average - median) / standardDeviation

def calcKurtosis(X):
    return stats.kurtosis(X, fisher=False)

def findMin(Y):
    return min(Y)

def findMax(Y):
    return max(Y)

def covarianceMatrix(X):
    return np.cov(X, bias=True)

def correlationMatrix(X):
    return np.corrcoef(X)

def peakToPeak(maxVal, minVal):
    return maxVal - minVal

def calcRMS(X):
    return np.sqrt(np.mean(X**2))

if __name__ == "__main__":
    Y = [55, 78, 65, 98, 97, 60, 67, 65, 83, 65]
    print(Y)
    print(calcKurtosis(Y))
