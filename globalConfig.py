
color = ['r', 'b', 'g', 'y', 'c', 'k']
currentColor = 0

movingAverageN = 5
movingAverageAlpha = 0.1

def setColor():
    global currentColor
    res = color[currentColor]
    currentColor = (currentColor + 1) % len(color)
    return res


