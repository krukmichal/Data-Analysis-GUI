import math

def calcArithmeticAverage(X):
    result = 0 
    for x in X:
        result += x
    return result / len(X);

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

def calcKurtosis(X, average, standardDeviation):
    sum = 0
    for x in X:
        sum += (x - average) ** 4

    return sum / len(X) / standardDeviation ** 4 - 3
 
def findMin(Y):
    return min(Y)

def findMax(Y):
    return max(Y)
