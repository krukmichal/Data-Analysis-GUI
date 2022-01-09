import os 
import csv

def writeFile(X, Y, filename, separator):
    print(filename)
    f = open(filename, "w")
    for i in range(len(X)):
        f.write(str(X[i]) + separator + str(Y[i]) + "\n")
    f.close()

def writeCsvFile(X, Y, filename):
    writeFile(X, Y, filename, ",")

def writeTxtFile(X, Y, filename):
    writeFile(X, Y, filename, " ")

