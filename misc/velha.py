from json.tool import main
from lib2to3.refactor import MultiprocessRefactoringTool
from operator import truediv
from pickletools import markobject
from pydoc import plain
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

playRow = 0
pX, pO = 0, 0


class Ui_MainWindow(object):

    def btnClick(self,pos):
        global playRow
        marca = ''
        
        if(playRow%2 == 0):
            marca = 'X'
        else:
            marca = 'O'
        
        if pos == 1:
            self.pb1.setText(marca)
            self.pb1.setEnabled(False)
        if pos == 2:
            self.pb2.setText(marca)
            self.pb2.setEnabled(False)
        if pos == 3:
            self.pb3.setText(marca)
            self.pb3.setEnabled(False) 
        if pos == 4:
            self.pb4.setText(marca)
            self.pb4.setEnabled(False)
        if pos == 5:
            self.pb5.setText(marca)
            self.pb5.setEnabled(False)
        if pos == 6:
            self.pb6.setText(marca)
            self.pb6.setEnabled(False)
        if pos == 7:
            self.pb7.setText(marca)
            self.pb7.setEnabled(False)
        if pos == 8:
            self.pb8.setText(marca)
            self.pb8.setEnabled(False)
        if pos == 9:
            self.pb9.setText(marca)
            self.pb9.setEnabled(False)
                
        playRow += 1  
        self.checkWin()
    
    def checkWin(self):
        global pX, pO
        win, loser = '', ''
        
        #LINHA 1
        if self.pb1.text() == self.pb2.text() and self.pb2.text() == self.pb3.text() and self.pb1.text() != '':
            win = self.pb1.text()
        #LINHA 2
        elif self.pb4.text() == self.pb5.text() and self.pb5.text() == self.pb6.text() and self.pb4.text() != '':
            win = self.pb5.text()
        #LINHA 3
        elif self.pb7.text() == self.pb8.text() and self.pb8.text() == self.pb9.text() and self.pb7.text() != '':
            win = self.pb8.text()
        #COLUNA 1   
        elif self.pb1.text() == self.pb4.text() and self.pb4.text() == self.pb7.text():
            win = self.pb1.text()
        #COLUNA 2
        elif self.pb2.text() == self.pb5.text() and self.pb5.text() == self.pb8.text():
            win = self.pb2.text()
        #COLUNA 3
        elif self.pb3.text() == self.pb6.text() and self.pb6.text() == self.pb9.text():
            win = self.pb3.text()
        #TRANSVERSAL DIRETA -> ESQUERDA
        elif self.pb1.text() == self.pb5.text() and self.pb5.text() == self.pb9.text():
            win = self.pb1.text()
        #TRANSVERSAL ESQUERDA -> DIREITA
        elif self.pb3.text() == self.pb5.text() and self.pb5.text() == self.pb7.text():
            win = self.pb3.text()

        if win == 'X':
            pX += 1
            self.xscore.setText("Jogador (X): "+str(pX))
            self.resetGame()
        if win == 'O':
            pO += 1
            self.oscore.setText("Jogador (O): "+str(pO))
            self.resetGame()        
    
    def resetGame(self):
        self.pb1.setEnabled(True)
        self.pb2.setEnabled(True)
        self.pb3.setEnabled(True)
        self.pb4.setEnabled(True)
        self.pb5.setEnabled(True)
        self.pb6.setEnabled(True)
        self.pb7.setEnabled(True)
        self.pb8.setEnabled(True)
        self.pb9.setEnabled(True)
        
        self.pb1.setText('')
        self.pb2.setText('')
        self.pb3.setText('')
        self.pb4.setText('')
        self.pb5.setText('')
        self.pb6.setText('')
        self.pb7.setText('')
        self.pb8.setText('')
        self.pb9.setText('')
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 457)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 420, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.pb6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb6.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb6.setFont(font)
        self.pb6.setText("")
        self.pb6.setObjectName("pb6")
        self.gridLayout.addWidget(self.pb6, 1, 2, 1, 1)
        self.pb6.clicked.connect(lambda: self.btnClick(6))
        
        self.pb4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb4.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb4.setFont(font)
        self.pb4.setText("")
        self.pb4.setObjectName("pb4")
        self.gridLayout.addWidget(self.pb4, 1, 0, 1, 1)
        self.pb4.clicked.connect(lambda: self.btnClick(4))
        
        self.pb7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb7.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb7.setFont(font)
        self.pb7.setText("")
        self.pb7.setObjectName("pb7")
        self.gridLayout.addWidget(self.pb7, 2, 0, 1, 1)
        self.pb7.clicked.connect(lambda: self.btnClick(7))
        
        self.pb2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb2.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.pb2.setText("")
        self.pb2.setObjectName("pb2")
        self.gridLayout.addWidget(self.pb2, 0, 1, 1, 1)
        self.pb2.clicked.connect(lambda: self.btnClick(2))
        
        self.pb5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb5.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb5.setFont(font)
        self.pb5.setText("")
        self.pb5.setObjectName("pb5")
        self.gridLayout.addWidget(self.pb5, 1, 1, 1, 1)
        self.pb5.clicked.connect(lambda: self.btnClick(5))
        
        self.pb1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb1.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb1.setFont(font)
        self.pb1.setText("")
        self.pb1.setObjectName("pb1")
        self.gridLayout.addWidget(self.pb1, 0, 0, 1, 1)
        self.pb1.clicked.connect(lambda: self.btnClick(1))
        
        self.pb8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb8.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb8.setFont(font)
        self.pb8.setText("")
        self.pb8.setObjectName("pb8")
        self.gridLayout.addWidget(self.pb8, 2, 1, 1, 1)
        self.pb8.clicked.connect(lambda: self.btnClick(8))
        
        self.pb3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb3.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.pb3.setText("")
        self.pb3.setObjectName("pb3")
        self.gridLayout.addWidget(self.pb3, 0, 2, 1, 1)
        self.pb3.clicked.connect(lambda: self.btnClick(3))
        
        self.pb9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb9.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pb9.setFont(font)
        self.pb9.setText("")
        self.pb9.setObjectName("pb9")
        self.gridLayout.addWidget(self.pb9, 2, 2, 1, 1)
        self.pb9.clicked.connect(lambda: self.btnClick(9))
        
        #SCORE label
        self.xscore = QtWidgets.QLabel(self.centralwidget)
        self.xscore.setGeometry(QtCore.QRect(40, 350, 111, 16))
        self.xscore.setObjectName("xscore")
        self.oscore = QtWidgets.QLabel(self.centralwidget)
        self.oscore.setGeometry(QtCore.QRect(40, 380, 111, 16))
        self.oscore.setObjectName("oscore")
        
        #RESET GAME
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(340, 340, 91, 71))
        self.reset.setMinimumSize(QtCore.QSize(50, 50))
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.resetGame)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.xscore.setText(_translate("MainWindow", "Jogador (X): 0"))
        self.oscore.setText(_translate("MainWindow", "Jogador (O): 0"))
        self.reset.setText(_translate("MainWindow", "RESET"))
          
class velhinha(Ui_MainWindow):
    def __init__(self, velha):
        self.setupUi(velha)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())