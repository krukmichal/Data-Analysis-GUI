def writeFile(X, Y, filename, separator):
    with open(filename, "w", encoding='utf-8') as f:
        for i in range(len(X)):
            f.write(str(X[i]) + separator + str(Y[i]) + "\n")

def writeCsvFile(X, Y, filename):
    writeFile(X, Y, filename, ",")

def writeTxtFile(X, Y, filename):
    writeFile(X, Y, filename, " ")
