import os 
import csv

def readSingleRowMultipleColumns(row, X, Y):
    X.append(float(row[0]))
    for i in range(1,len(row)):
        Y[i-1].append(float(row[i]))

def readSingleRowOneColumn(row, X, Y):
    if len(X) == 0:
        X.append(0)
    else:
        X.append(X[-1] + 1)

    Y[0].append(float(row[0]))

def readSingleRow(row, X, Y, isFirstLine):
    if len(row) == 1:
        if isFirstLine:
            Y.append([])
        readSingleRowOneColumn(row,X,Y)

    else:
        if isFirstLine:
            for i in range(1,len(row)):
                Y.append([])
        readSingleRowMultipleColumns(row,X,Y)


def readSpaceSeperatedFile(filename):
    X = []
    Y = []
    with open(filename, 'r') as f:
        isFirstLine = True
        for line in f:
            row = line.strip().split(' ')
            readSingleRow(row,X,Y,isFirstLine)
            isFirstLine = False
    return X, Y

def readCsvFile(filename):
    X = []
    Y = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        isFirstLine = True
        for row in csvreader:
            readSingleRow(row, X, Y, isFirstLine)
            isFirstLine = False
    return X, Y

def getFileExtension(filename):
    i = filename.rfind('.')
    if (i == -1 or i > len(filename)-2):
        raise Exception('can not get file format')
    result = filename[i+1:]

    if result != "txt" and result != "csv":
        raise Exception('wrong file format')

    return result

def readFiles(filenames):
    result = []
    for filename in filenames:
        X, Y = None, None
        if getFileExtension(filename) == "txt":
            X, Y = readSpaceSeperatedFile(filename)
        else:
            X, Y = readCsvFile(filename)
        for i in range(len(Y)):
            name = os.path.basename(filename) + str(i)
            result.append([name, X, Y[i]])

    return result
