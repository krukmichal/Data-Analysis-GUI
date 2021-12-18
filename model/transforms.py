import numpy as np

def expMovingAverage(X, Y, N):
    a = 2 / (N + 1)
    newY = []
    
    for i in range(len(Y)):
        curSum = 0
        curDivisor = 0
        for j in range(min(N, i+1)):
            weight = (1 - a) ** j
            curSum += weight * Y[i-j]
            curDivisor += weight 

        newY.append(curSum / curDivisor)

    return (X.copy(), newY)

def calcEMA(Y,N,alpha):
    newY = np.array(Y, dtype=float)
    divisor = 0
    for i in range(N):
        divisor += (1-alpha) ** i
    
    for i in range(N-1, len(Y)):
        sum = 0
        for j in range(N):
            sum += ((1-alpha)**j) * Y[i-j]

        newY[i] = sum / divisor

    return newY

 

def calcSMA(Y, N):
    newY = np.cumsum(Y, dtype = float)
    newY[N:] = newY[N:] - newY[:-N]
    newY[N-1:] = newY[N - 1:] / N
    newY[:N-1] = Y[:N-1]
    return newY


