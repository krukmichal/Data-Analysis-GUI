import sys
from PyQt5 import QtWidgets
from presenter.mainWindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.resize(1700, 800)
    main.show()
    sys.exit(app.exec_())
