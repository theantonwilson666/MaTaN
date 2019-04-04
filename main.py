import integral
import sys
import math
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.ticker

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtCore import QCoreApplication

class MaTaN(QMainWindow):

    def __init__(self):
        super().__init__()

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)

        self.initMenu()
        self.initWidgets()
        self.initUI()

    def initMenu(self):
        self.statusBar().showMessage('Ready')
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setStatusTip('Exit application')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)


    def initWidgets(self):
        wid = QWidget()
        self.setCentralWidget(wid)

        self.textFunc = QLineEdit()
        self.textA = QLineEdit()
        self.textB = QLineEdit()
        self.textN = QLineEdit()

        hlayAB = QHBoxLayout()
        hlayAB.addWidget(self.textA)
        hlayAB.addWidget(QLabel(":"))
        hlayAB.addWidget(self.textB)

        countButton = QPushButton("Вывести")
        countButton.clicked.connect(self.buttonClicked)

        vlayUpRight = QVBoxLayout()
        vlayUpRight.addWidget(QLabel("Область рисования: [a, b]"))
        vlayUpRight.addLayout(hlayAB)
        vlayUpRight.addWidget(countButton)

        hlayNumbText = QHBoxLayout()
        hlayNumbText.addWidget(QLabel("\t\t\t\t\t\t\tКол-во рядов Фурье: "))
        hlayNumbText.addWidget(self.textN)

        hlayFunc = QHBoxLayout()
        hlayFunc.addWidget(QLabel("f(x) =  "))
        hlayFunc.addWidget(self.textFunc)

        vlayUpLeft = QVBoxLayout()
        vlayUpLeft.addLayout(hlayFunc)
        #vlayUpLeft.addStretch(1)
        vlayUpLeft.addLayout(hlayNumbText)

        hlayUp = QHBoxLayout()
    #    hlayUp.addWidget(QLabel("f(x) = "))
        hlayUp.addLayout(vlayUpLeft, 7)
        hlayUp.addLayout(vlayUpRight, 3)

        vlay = QVBoxLayout()
        vlay.addStretch(1)
        vlay.addLayout(hlayUp)
        vlay.addWidget(self.canvas)


        wid.setLayout(vlay)

    def graphics(self):
        self.ax.clear()


        dx = 0.01
        xlist = np.arange(self.data.a, self.data.b, dx)
        ylistOrig = [self.data.f(x) for x in xlist]
        ylistFourier = [self.data.Foureie_f(x) for x in xlist]
        self.ax.plot(xlist, ylistOrig)
        self.ax.plot(xlist, ylistFourier)
        self.ax.legend(("Функция", "Ряд Фурье"))
        self.ax = plt.gca()
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.grid()
        self.canvas.draw()

    def initUI(self):
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Foureie Series')
        self.setWindowIcon(QIcon('roflan.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):
        self.data = integral.integral(self.textFunc.text(), self.textA.text(), self.textB.text(), self.textN.text())
        self.graphics()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MaTaN()
    sys.exit(app.exec_())
