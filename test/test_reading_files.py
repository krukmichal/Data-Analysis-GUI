from fileReader.fileReader import *

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




