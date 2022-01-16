from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QTableWidgetItem, QLabel

from model.calcMetric import covarianceMatrix
from model.calcMetric import correlationMatrix


class MatrixWindow(QDialog):
    def __init__(self, statsType, dataY, names):
        super().__init__()

        self.setWindowTitle(statsType)

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
                self.table.setItem(i,j,QTableWidgetItem(str(data[i][j])))

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)
        self.resize(1000, 600)
