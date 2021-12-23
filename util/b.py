from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Main Window")

        self.main_widget = QtWidgets.QWidget(self)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        sc = MyStaticMplCanvas(width=5, height=4, dpi=100)  # just some graph
        dc = MyDynamicMplCanvas(width=5, height=4, dpi=100) # another graph
        l.addWidget(sc)
        l.addWidget(dc)        

       # Snippet 3
        x = QtWidgets.QHBoxLayout()         # self.main_widget) # new
        b1 = QtWidgets.QPushButton("Test1") # new
        b2 = QtWidgets.QPushButton("Test2") # new
        x.addWidget(b1)                     # new   + b1
        x.addWidget(b2)                     # new   + b2

        l.addLayout(x)                                                  # <----

if __name__ == "__main__": 
    import sys 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = ApplicationWindow() 
    MainWindow.show() 
    sys.exit(app.exec_())        

