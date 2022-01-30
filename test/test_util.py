from model.util import checkIfSameData, binSearch, findLeftRightIndices, interpolate
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
 
def test_findLeftRightIndices0():
    Y = [0,1,2,5,6]
    assert findLeftRightIndices(Y,-1) == (None,None)

def test_findLeftRightIndices1():
    Y = [0,1,2,5,6]
    assert findLeftRightIndices(Y,6) == (None,None)

def test_findLeftRightIndices2():
    Y = [0,1,2,5,6]
    assert findLeftRightIndices(Y,7) == (None,None)

def test_findLeftRightIndices3():
    Y = [0,1,2,5,6]
    assert findLeftRightIndices(Y,0) == (None,None)

def test_findLeftRightIndices4():
    Y = [0,1,2,5,6]
    assert findLeftRightIndices(Y,2.5) == (2,3)

def test_findLeftRightIndices5():
    Y = [1,3]
    assert findLeftRightIndices(Y,1.5) == (0,1)

def test_interpolate0():
    X = [1,3]
    Y = [1,3]
    assert interpolate(X,Y,2) == 2

def test_interpolate1():
    X = [1,3]
    Y = [1,3]
    assert interpolate(X,Y,1.5) == 1.5


