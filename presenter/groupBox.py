from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt

class GroupBox(QGroupBox):
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

        self.button = QPushButton("Set")
        self.button.setMaximumWidth(150)

        self.button.clicked.connect(self.handleButtonClicked)

        self.editStart.setMaximumWidth(200)
        self.editEnd.setMaximumWidth(200)

        self.layout.addWidget(self.xPos)
        self.layout.addWidget(self.yPos)
        self.layout.addWidget(self.editStart)
        self.layout.addWidget(self.editEnd)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def setGraphLayout(self, graphLayout):
        self.graphLayout = graphLayout

    def handleButtonClicked(self):
        startPos = float(self.editStart.text())
        endPos = float(self.editEnd.text())

        if startPos >= endPos:
            msgBox = QMessageBox()
            msgBox.setText("ERROR: Start position cannot be smaller or equal end position")
            msgBox.exec_()
            return
        
        self.graphLayout.setRangeForEachGraph(startPos, endPos)

    def setXText(self, text):
        self.xPos.setText("x: " + text)

    def setYText(self, text):
        self.yPos.setText("y: " + text)
