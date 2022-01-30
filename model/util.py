import numpy as np

def checkIfSameData(X,Y):
    if len(X) != len(Y):
        return False

    for i in range(len(X)):
        if not np.isclose(X[i], Y[i], rtol=1e-05, atol=1e-08):
            return False

    return True


def binSearch(data, val):
    l = 0
    r = len(data) - 1

    res = l
    while l <= r:
        m = l + (r - l) // 2
        if data[m] < val:
            l = m + 1
        elif data[m] > val:
            r = m - 1
        else:
            res = m
            break
        if abs(data[m] - val) < abs(data[res] - val):
            res = m

    return res

def findLeftRightIndices(X, value):
    if value <= X[0] or value >= X[-1]:
        return (None, None)

    result = np.searchsorted(X, [value], side='right')[0]
    return (result-1, result)
    

def interpolate(X, Y, point):
    left, right = findLeftRightIndices(X, point)

    if left == None:
        return None

    return (Y[right] - Y[left])/(X[right] - X[left])*(point - X[left]) + Y[left]
