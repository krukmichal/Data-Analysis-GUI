import os 
import csv

def readBasicFile(filename):
    dataX = []
    dataY = []
    with open(filename, 'r') as f:
        for line in f:
            if line[-1] == 'n':
                line = line[:-2]
            values = line.split(' ')
            dataX.append(float(values[0]))
            dataY.append(float(values[1]))

    return dataX, dataY

def readSingleRow(row, X, Y, isFirstLine):
    if len(row) == 1:
        if len(X) == 0:
            X.append(0)
        else:
            X.append(X[-1] + 1)

    X.append(float(row[0]))
     
    for i in range(1,len(row)):
        if isFirstLine:
            Y.append([])
        Y[i-1].append(float(row[i]))

def readSpaceSeperatedFile(filename):
    X = []
    Y = []
    with open(filename, 'r') as f:
        isFirstLine = True
        for line in f:
            if line[-1] == 'n':
                line = line[:-2]
            row = line.split(' ')
            readSingleRow(row, X, Y, isFirstLine)
            isFirstLine = False
    return X, Y

def readCsvFile(filename):
    X = []
    Y = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        isFirstLine = True
        for row in csvreader:
            print(row)
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

    print(result)
    return result
