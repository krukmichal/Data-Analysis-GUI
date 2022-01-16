from model.util import checkIfSameData, binSearch
import numpy as np

def test_checkIfSameData0():
    Y = [1,2,3,4,5,6]
    X = [1,2,3,4,5,6]
    assert checkIfSameData(Y,X) == True

def test_checkIfSameData1():
    Y = [1,2,3,4,5,7]
    X = [1,2,3,4,5,6]
    assert checkIfSameData(X,Y) == False

def test_checkIfSameData1():
    Y = [1,2,3,7]
    X = [1,2,3,4,5,6]
    assert checkIfSameData(X,Y) == False

def test_checkIfSameData2():
    Y = [0.6000000000000001]
    X = [0.6]
    assert checkIfSameData(X,Y) == True

def test_checkIfSameData3():
    Y = [0.600011]
    X = [0.6]
    assert checkIfSameData(X,Y) == False

def test_binSearch():
    Y = [0,1,2,3,4,5,6]
    res = binSearch(Y, 2.3)
    assert res == 2
 
