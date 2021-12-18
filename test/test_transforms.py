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
