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

def readSpaceSeperatedFile(filename):
    pass

def readCsvFile(filename):
    pass

def getFileExtension(filename):
    i = filename.rfind('.')
    if (i == -1 || i > len(filename)-2):
        raise Exception('can not get file format')
    result = filename[i+1:]

    if result != ".txt" and result != ".csv":
        raise Exception('wrong file format')

    return result

def readFiles(chosenNames):
    for chosenName in chosenNames:

if __name__ == "__main__":
    X, Y = readBasicFile('test.txt')
"""
        dataX, dataY = readBasicFile(chosenFile)
        trendPresenter = TrendPresenter(
                self.graphWidget,
                self.metricList,
                dataX,
                dataY,
                os.path.basename(chosenFile),
                )
                """
