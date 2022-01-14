import numpy as np
from scipy.fft import fft, fftfreq

def calcEMA(Y,N,a):
    newY = []
    
    for i in range(len(Y)):
        curSum = 0
        curDivisor = 0
        for j in range(min(N, i+1)):
            weight = (1 - a) ** j
            curSum += weight * Y[i-j]
            curDivisor += weight 

        newY.append(curSum / curDivisor)

    return newY

def calcSMA(Y, N):
    newY = np.cumsum(Y, dtype = float)
    newY[N:] = newY[N:] - newY[:-N]
    newY[N-1:] = newY[N - 1:] / N
    for i in range(N-1):
        newY[i] = newY[i]/(i+1)

    return newY

def removePeaks(Y, threshold):
    newY = np.array(Y, dtype=float)
    for i in range(1, len(newY)-1):
        diff = min(abs(newY[i] - newY[i-1]), abs(newY[i+1] - newY[i]))
        if diff > threshold:
            newY[i] = (newY[i+1] + newY[i-1]) / 2

    return newY

def calcFFT(X, Y):
    T = X[1] - X[0]
    N = len(X)

    yf = np.abs(fft(Y))[0:N//2] / N
    xf = fftfreq(N, T)[:N//2]

    return xf, yf

def changeResolutionLinear(X, Y, res):
    newX = []
    newY = []

    x = X[0]
    while x < X[-1] or np.isclose(x, X[-1], rtol=1e-05, atol=1e-08, equal_nan=False):
        newX.append(x)
        x += res

    j = 0
    i = 0
    while i < len(newX):
        if np.isclose(newX[i], X[j], rtol=1e-05, atol=1e-08, equal_nan=False):
            newY.append(Y[j])
            j += 1
        elif newX[i] > X[j]:
            j += 1
            i -= 1
        else:
            newval = (Y[j] - Y[j-1])/(X[j] - X[j-1]) * (newX[i] - X[j-1]) + Y[j-1]
            newY.append(newval) 
        i += 1

    return newX, newY

def cutTrend(X, Y, xMin, xMax):
    i = 0
    while i < len(X) and X[i] < xMin and not np.isclose(X[i], xMin, rtol=1e-05, atol=1e-08):
        i += 1

    j = i
    while j < len(X) and X[j] < xMax and not np.isclose(X[j], xMax, rtol=1e-05, atol=1e-08):
        j += 1

    if j >= len(X) or (X[j] > xMax and not np.isclose(X[j], xMax, rtol=1e-05, atol=1e-08)):
        return X[i:j], Y[i:j]
    else:
        return X[i:j+1], Y[i:j+1]


    

