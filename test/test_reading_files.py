from fileio.fileReader import *
from fileio.fileWriter import *

def test_example():
    assert 3 == 3

def test_reading_csv():
    result = readFiles(["test/files/simple.csv"])
    assert result == [
                [
                    "simple.csv0", 
                    [1.0,2.0,3.0,4.0,5.0,6.0], 
                    [4.0,2.0,3.0,3.0,4.0,6.0]
                ]
            ]

def test_reading_txt():
    result = readFiles(["test/files/simple.txt"])
    assert result == [
                [
                    "simple.txt0", 
                    [1.0,2.0,3.0,4.0,5.0,6.0], 
                    [4.0,2.0,3.0,3.0,4.0,6.0]
                ]
            ]


def test_reading_one_line_file():
    result = readFiles(["test/files/oneline.txt"])

    assert result == [
                [
                    "oneline.txt0",
                    [0,1,2,3],
                    [0.0,2.0,4.0,6.0]
                ]
            ]

def test_write_and_read_txt():
    X = [1,2,3,4,5,6]
    Y = [4,3,5,6,7,3]

    writeTxtFile(X, Y, "test/files/testwrite1.txt")
    result = readFiles(["test/files/testwrite1.txt"])

    assert result == [
                [
                    "testwrite1.txt0",
                    [1,2,3,4,5,6],
                    [4.0,3.0,5.0,6.0,7.0,3.0]
                ]
            ]

def test_write_and_read_csv():
    X = [1,2,3,4,5,6]
    Y = [4,3,5,6,7,3]

    writeCsvFile(X, Y, "test/files/testwrite1.csv")
    result = readFiles(["test/files/testwrite1.csv"])

    assert result == [
                [
                    "testwrite1.csv0",
                    [1,2,3,4,5,6],
                    [4.0,3.0,5.0,6.0,7.0,3.0]
                ]
            ]

