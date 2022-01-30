from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt
from model.transforms import cutTrend
from model.trendModel import TrendModel 

class ToolPanel(QGroupBox):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        self.layout.setAlignment(Qt.AlignLeft)
        #self.setStyleSheet("background-color: white;border: 1px ")
        #self.setStyleSheet("background-color: white;border: 1px solid #A9A9A9")
        self.setStyleSheet(" QGroupBox::title { border: 0px ; border-radius: 0px; padding: 0px 0px 0px 0px; margin = 0px 0px 0px 0px } QGroupBox { background-color: white ; border: 1px solid #A9A9A9; border-radius: 0px; padding: 0px 0px 0px 0px;} "
        )

        self.setMaximumHeight(80)
        #self.setFlat(True)
        #self.setStyleSheet("border:0;");

        self.xPos = QLabel("x:")
        self.xPos.setMaximumWidth(180)
        self.yPos = QLabel("y:")
        self.yPos.setMaximumWidth(180)

        self.validator = QDoubleValidator()

        self.editStart = QLineEdit()
        self.editStart.setValidator(self.validator)
        self.editEnd = QLineEdit()
        self.editStart.setValidator(self.validator)

        self.buttonCut = QPushButton("Set")
        self.buttonCut.setMaximumWidth(100)
        self.buttonCut.clicked.connect(self.handleButtonCutClicked)

        self.buttonMetrics = QPushButton("Metrics")
        self.buttonMetrics.setMaximumWidth(100)
        self.buttonMetrics.clicked.connect(self.handleButtonMetricsClicked)

        self.editStart.setMaximumWidth(150)
        self.editEnd.setMaximumWidth(150)

        self.layout.addWidget(self.xPos)
        self.layout.addWidget(self.yPos)
        self.layout.addWidget(self.editStart)
        self.layout.addWidget(self.editEnd)
        self.layout.addWidget(self.buttonCut)
        self.layout.addWidget(self.buttonMetrics)

        self.setLayout(self.layout)

    def setGraphLayout(self, graphLayout):
        self.graphLayout = graphLayout

    def setMetricList(self, metricList):
        self.metricList = metricList

    def setTrendList(self, trendList):
        self.trendList = trendList

    def handleButtonCutClicked(self):
        startPos = float(self.editStart.text())
        endPos = float(self.editEnd.text())

        if startPos >= endPos:
            msgBox = QMessageBox()
            msgBox.setText("ERROR: Wrong limits")
            msgBox.exec_()
            return
        
        self.graphLayout.setRangeForEachGraph(startPos, endPos)

    def handleButtonMetricsClicked(self):
        if len(self.trendList.selectedItems()) == 0:
            msgBox = QMessageBox()
            msgBox.setText("ERROR: No item selected")
            msgBox.exec_()
            return

        item = self.trendList.selectedItems()[0]
        ax = self.graphLayout.graphs[0].getAxis('bottom')

        X,Y = cutTrend(item.trendModel.dataX, item.trendModel.dataY, ax.range[0], ax.range[1])
        if len(X) != 0:
            trendModel = TrendModel(X,Y)
            self.metricList.showMetrics(trendModel)
        
    def setXText(self, text):
        self.xPos.setText("x: " + text)

    def setYText(self, text):
        self.yPos.setText("y: " + text)
