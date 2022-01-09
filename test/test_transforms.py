from model.transforms import *
import numpy as np

def test_sma0():
    Y = [1,2,3,4,5,6]
    tY = calcSMA(Y,3)

    assert np.all(tY == [1,2,2,3,4,5])

def test_sma1():
    Y = [2,4,6,12,8,12,16,8,4,2,0]
    tY = calcSMA(Y,4)

    assert np.all(tY == [2,4,6,6,7.5,9.5,12,11,10,7.5,3.5])

def test_ema0():
    Y = [1,1,1,1,1,1]
    tY = calcEMA(Y,3,0.5)

    assert np.all(tY == [1,1,1,1,1,1])

def test_ema1():
    Y = [1,3,2,4]
    tY = calcEMA(Y,2,0.5)

    for i in range(len(tY)):
        tY[i] = np.around(tY[i],2)

    assert np.all(tY == [1, 2.33, 2.33, 3.33])

def test_removePeaks0():
    Y = [0,1,2,3,4,5,4,22,5]
    tY = removePeaks(Y, 11)

    assert np.all(tY == [0,1,2,3,4,5,4,4.5,5])

def test_changeResolutionLinear0():
    X = [3,8]
    Y = [2,7]

    newX, newY = changeResolutionLinear(X,Y,1)

    assert np.all(newX == [3,4,5,6,7,8])
    assert np.all(newY == [2,3,4,5,6,7])

def test_changeResolutionLinear1():
    X = [0,3,5,7]
    Y = [3,3,7,0]

    newX, newY = changeResolutionLinear(X,Y,0.5)

    assert np.all(newX == np.linspace(0,7,15,endpoint=True))
    assert np.all(newY == [3,3,3,3,3,3,3,4,5,6,7,5.25,3.5,1.75,0])

def test_changeResolutionLinear2():
    X = [0,1,2]
    Y = [1,2,1]

    newX, newY = changeResolutionLinear(X,Y,0.2)
    assert len(newX) == len(newY)

    for x in range(len(newX)):
        newX[x] = np.around(newX[x],2)
        newY[x] = np.around(newY[x],2)

    assert np.all(newX == [0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2.0])
    assert np.all(newY == [1,1.2,1.4,1.6,1.8,2,1.8,1.6,1.4,1.2,1])

def test_changeResolutionLinear3():
    X = [1,2,3,4,5,6]
    Y = [4,2,3,3,4,6]

    newX, newY = changeResolutionLinear(X,Y,0.2)

    for x in range(len(newX)):
        newX[x] = np.around(newX[x],1)
        #newY[x] = np.around(newY[x],1)

    assert len(newX) == len(newY)
    assert np.all(newX == [1.0,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0])


