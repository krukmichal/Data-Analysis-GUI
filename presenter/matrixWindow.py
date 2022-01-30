from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QTableWidgetItem, QLabel
from PyQt5.QtGui import QColor, QBrush

from model.calcMetric import covarianceMatrix
from model.calcMetric import correlationMatrix
import math

class MatrixWindow(QDialog):
    def __init__(self, statsType, dataY, names):
        super().__init__()

        self.setWindowTitle(statsType)
        self.statsType = statsType

        data = None
        if statsType == "correlation":
            data = correlationMatrix(dataY)
        else:
            data = covarianceMatrix(dataY)

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(len(data))
        self.table.setRowCount(len(data))

        self.table.setHorizontalHeaderLabels(names)
        self.table.setVerticalHeaderLabels(names)

        for i in range(len(data)):
            for j in range(len(data)):
                if i != j:
                    backgroundColor = self.setBackgroundColor(data[i][j])
                    foregroundColor = self.setForegroundColor(data[i][j])
                    item = QTableWidgetItem(str(data[i][j]))
                    item.setBackground(QBrush(backgroundColor))
                    item.setForeground(QBrush(foregroundColor))
                    self.table.setItem(i,j,item)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)
        self.resize(1000, 600)

    def setBackgroundColor(self, value):
        if self.statsType == "covariance" or math.isnan(value):
            return QColor(255,255,255)

        if value < 0:
            return QColor(0, int((1+value)*255),int(-1 * value*255))

        return QColor(int(value*255),int((1-value)*255),0)

    def setForegroundColor(self, value):
        if self.statsType == "covariance":
            return QColor(0,0,0)

        if value < -0.2:
            return QColor(255,255,255)
        return QColor(0,0,0)
