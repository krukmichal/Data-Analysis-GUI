import math
import numpy
import random

def gen_sin(x_range):
    dataX = numpy.linspace(0,x_range, 10000)
    dataY = []


    for x in dataX:
        dataY.append(math.sin(i) + random.random()/3)

    with open("sin-noise.txt", 'w') as f:
        for i in range(len(dataX)):
            f.write(str(dataX[i]) + " " + str(dataY[i]) + "\n")

def gen_sin2(x_range):
    dataX = numpy.linspace(0,x_range, 30000)
    dataY = []


    for x in dataX:
        dataY.append(math.sin(x) + math.sin(2.3*x))

    with open("sin2.txt", 'w') as f:
        for i in range(len(dataX)):
            f.write(str(dataX[i]) + " " + str(dataY[i]) + "\n")


def gen_poly(x_range):
    dataX = []
    dataY = []

    array = numpy.arange(-0.5,x_range,0.01)

    for i in array:
        dataX.append(i)
        dataY.append((i-1)*(i-2)*(i-3) + random.random())

    with open("polynomial.txt", 'w') as f:
        for i in range(len(dataX)):
            f.write(str(dataX[i]) + " " + str(dataY[i]) + "\n")

    

gen_sin2(16)



        




