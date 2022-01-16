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
