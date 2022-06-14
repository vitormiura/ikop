from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import time

global random, click, dic

playRow = 0
dic = {}
random = []
click = 0

class Ui_MainWindow(object):
    def sort(self):
        global random

        bascas = "misc\\adivinhas\\bascas.png"
        bascas2 = "misc\\adivinhas\\bascas2.png"
        cortinas = "misc\\adivinhas\\cortinas.png"
        cortinas2 = "misc\\adivinhas\\cortinas2.png" 
        diabin = "misc\\adivinhas\\diabin.png"
        diabin2 = "misc\\adivinhas\\diabin2.png"
        ferrari = "misc\\adivinhas\\ferrari.png"
        ferrari2 = "misc\\adivinhas\\ferrari2.png"
        joia = "misc\\adivinhas\\joia.png"
        joia2 = "misc\\adivinhas\\joia2.png"
        macaco = "misc\\adivinhas\\macaco.png"
        macaco2 = "misc\\adivinhas\\macaco2.png"
        martelo = "misc\\adivinhas\\martelo.png"
        martelo2 = "misc\\adivinhas\\martelo2.png"
        sapato = "misc\\adivinhas\\sapato.png"
        sapato2 = "misc\\adivinhas\\sapato2.png"
        
        icons = [bascas, bascas2, cortinas, cortinas2, diabin, diabin2, ferrari, ferrari2, joia, joia2, macaco, macaco2, martelo, martelo2, sapato, sapato2]
        
        random = np.random.choice(icons, size=16, replace=False)
    
    def select(self, botas):
        global dic
        print(dic[botas.objectName()])
        return dic[botas.objectName()]
    
    def game(self):
        global random, playRow
        
        self.a.clicked.connect(lambda:self.select(self.a)) 
        self.b1.clicked.connect(lambda:self.select(self.b1))
        self.b2.clicked.connect(lambda:self.select(self.b2))
        self.b3.clicked.connect(lambda:self.select(self.b3))
        self.b4.clicked.connect(lambda:self.select(self.b4))
        self.b5.clicked.connect(lambda:self.select(self.b5))
        self.b6.clicked.connect(lambda:self.select(self.b6))
        self.b7.clicked.connect(lambda:self.select(self.b7))
        self.b8.clicked.connect(lambda:self.select(self.b8))
        self.b9.clicked.connect(lambda:self.select(self.b9))
        self.b10.clicked.connect(lambda:self.select(self.b10))
        self.b11.clicked.connect(lambda:self.select(self.b11))
        self.b12.clicked.connect(lambda:self.select(self.b12))
        self.b13.clicked.connect(lambda:self.select(self.b13))
        self.b14.clicked.connect(lambda:self.select(self.b14))
        self.b15.clicked.connect(lambda:self.select(self.b15))
        
        mask = ["","","","","","","","","","","","","","",""]
        
        # for i in range(buttonArr):
        #     playRow += 1
            
        # if(playRow == 2):
        #     for i in range(buttonArr):
        #         self.icon[i].addPixmap(QtGui.QPixmap(mask[z]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # else:
        #     for i in range(buttonArr):
        #         for z in range(mask):
        #             self.icon[i].addPixmap(QtGui.QPixmap(mask[z]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        iconNum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        
         
    def setupUi(self, MainWindow):
        global random, click, dic
        click = 0
        self.sort()
        #print(random)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 526, 420))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.b6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b6.setMinimumSize(QtCore.QSize(100, 100))
        self.b6.setText("")
        
        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap(random[0]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b6.setIcon(icon0)
        self.b6.setIconSize(QtCore.QSize(100, 100))
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 1, 1, 1, 1)
        self.a = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.a.setMinimumSize(QtCore.QSize(100, 100))
        self.a.setText("")
        dic[self.b6.objectName()] = random[0]
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(random[1]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.a.setIcon(icon1)
        self.a.setIconSize(QtCore.QSize(100, 100))
        self.a.setObjectName("a")
        self.gridLayout.addWidget(self.a, 3, 3, 1, 1)
        self.b14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b14.setMinimumSize(QtCore.QSize(100, 100))
        self.b14.setText("")
        dic[self.a.objectName()] = random[1]
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(random[2]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b14.setIcon(icon2)
        self.b14.setIconSize(QtCore.QSize(100, 100))
        self.b14.setObjectName("b14")
        self.gridLayout.addWidget(self.b14, 3, 1, 1, 1)
        self.b13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b13.setMinimumSize(QtCore.QSize(100, 100))
        self.b13.setText("")
        dic[self.b14.objectName()] = random[2]
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(random[3]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b13.setIcon(icon3)
        self.b13.setIconSize(QtCore.QSize(100, 100))
        self.b13.setObjectName("b13")
        self.gridLayout.addWidget(self.b13, 3, 0, 1, 1)
        self.b4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b4.setMinimumSize(QtCore.QSize(100, 100))
        self.b4.setText("")
        dic[self.b13.objectName()] = random[3]
        
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(random[4]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b4.setIcon(icon4)
        self.b4.setIconSize(QtCore.QSize(100, 100))
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 0, 3, 1, 1)
        self.b7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b7.setMinimumSize(QtCore.QSize(100, 100))
        self.b7.setText("")
        dic[self.b4.objectName()] = random[4]
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(random[5]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b7.setIcon(icon5)
        self.b7.setIconSize(QtCore.QSize(100, 100))
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 1, 2, 1, 1)
        self.b3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b3.setMinimumSize(QtCore.QSize(100, 100))
        self.b3.setText("")
        dic[self.b7.objectName()] = random[5]
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(random[6]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b3.setIcon(icon6)
        self.b3.setIconSize(QtCore.QSize(100, 100))
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 0, 2, 1, 1)
        self.b5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b5.setMinimumSize(QtCore.QSize(100, 100))
        self.b5.setText("")
        dic[self.b3.objectName()] = random[6]
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(random[7]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b5.setIcon(icon7)
        self.b5.setIconSize(QtCore.QSize(100, 100))
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 1, 0, 1, 1)
        self.b10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b10.setMinimumSize(QtCore.QSize(100, 100))
        self.b10.setText("")
        dic[self.b5.objectName()] = random[7]
        
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(random[8]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b10.setIcon(icon8)
        self.b10.setIconSize(QtCore.QSize(100, 100))
        self.b10.setObjectName("b10")
        self.gridLayout.addWidget(self.b10, 2, 1, 1, 1)
        self.b1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b1.setMinimumSize(QtCore.QSize(100, 100))
        self.b1.setText("")
        dic[self.b10.objectName()] = random[8]
        
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(random[9]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b1.setIcon(icon9)
        self.b1.setIconSize(QtCore.QSize(100, 100))
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 0, 0, 1, 1)
        self.b2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b2.setMinimumSize(QtCore.QSize(100, 100))
        self.b2.setText("")
        dic[self.b1.objectName()] = random[9]
        
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(random[10]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b2.setIcon(icon10)
        self.b2.setIconSize(QtCore.QSize(100, 100))
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 0, 1, 1, 1)
        self.b9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b9.setMinimumSize(QtCore.QSize(100, 100))
        self.b9.setText("")
        dic[self.b2.objectName()] = random[10]
        
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(random[11]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b9.setIcon(icon11)
        self.b9.setIconSize(QtCore.QSize(100, 100))
        self.b9.setObjectName("b9")
        self.gridLayout.addWidget(self.b9, 2, 0, 1, 1)
        self.b11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b11.setMinimumSize(QtCore.QSize(100, 100))
        self.b11.setText("")
        dic[self.b9.objectName()] = random[11]
        
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(random[12]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b11.setIcon(icon12)
        self.b11.setIconSize(QtCore.QSize(100, 100))
        self.b11.setObjectName("b11")
        self.gridLayout.addWidget(self.b11, 2, 2, 1, 1)
        self.b12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b12.setMinimumSize(QtCore.QSize(100, 100))
        self.b12.setText("")
        dic[self.b11.objectName()] = random[12]
        
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(random[13]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b12.setIcon(icon13)
        self.b12.setIconSize(QtCore.QSize(100, 100))
        self.b12.setObjectName("b12")
        self.gridLayout.addWidget(self.b12, 2, 3, 1, 1)
        self.b8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b8.setMinimumSize(QtCore.QSize(100, 100))
        self.b8.setText("")
        dic[self.b12.objectName()] = random[13]
        
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(random[14]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b8.setIcon(icon14)
        self.b8.setIconSize(QtCore.QSize(100, 100))
        self.b8.setObjectName("b8")
        self.gridLayout.addWidget(self.b8, 1, 3, 1, 1)
        self.b15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b15.setMinimumSize(QtCore.QSize(100, 100))
        self.b15.setText("")
        dic[self.b8.objectName()] = random[14]
        
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(random[15]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.b15.setIcon(icon15)
        self.b15.setIconSize(QtCore.QSize(100, 100))
        self.b15.setObjectName("b15")
        dic[self.b15.objectName()] = random[15]
        
        self.gridLayout.addWidget(self.b15, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 460, 371, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: black;\n"
        "color: white;\n"
        "border-radius: 15px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 460, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: black;\n"
        "color: white;\n"
        "border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.a = random[0]
        # self.b1 = random[1]
        # self.b2 = random[2]
        # self.b3 = random[3]
        # self.b4 = random[4]
        # self.b5 = random[5]
        # self.b6 = random[6]
        # self.b7 = random[7]
        # self.b8 = random[8]
        # self.b9 = random[9]
        # self.b10 = random[10]
        # self.b11 = random[11]
        # self.b12 = random[12]
        # self.b13 = random[13]
        # self.b14 = random[14]
        # self.b15 = random[15]
        self.game()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jogo do Adivinhas"))
        self.pushButton.setText(_translate("MainWindow", "RESET"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())