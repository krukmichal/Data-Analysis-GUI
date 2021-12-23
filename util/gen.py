import math
import numpy
import random

def gen_sin(x_range):
    dataX = []
    dataY = []

    array = numpy.arange(0,x_range,0.01)

    for i in array:
        dataX.append(i)
        dataY.append(math.sin(i) + random.random()/3)

    with open("sin-noise.txt", 'w') as f:
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

    
gen_poly(4.5)



        




