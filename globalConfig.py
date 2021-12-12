whichMetricsToShow = {
        "arithmeticAverage" : True,
        "median" : True,
        "standardDeviation" : True,
        "variance" : True
        }

metricName = {
        "arithmeticAverage" : "Average",
        "median" : "Median",
        "standardDeviation" : "Standard Deviation",
        "variance" : "Variance"
        }

precision = 4;
color = ['r', 'b', 'g', 'y', 'c', 'k']
currentColor = 0

def setColor():
    global currentColor
    res = color[currentColor]
    currentColor = (currentColor + 1) % len(color)
    return res


