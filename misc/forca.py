import random
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

global temp,word,dig,vida
temp = ''
vida = 7
dig = []
word = ''

class Ui_MainWindow(object):

    def comecas(self):
        self.vida1.setVisible(False)
        self.vida2.setVisible(False)
        self.vida3.setVisible(False)
        self.vida4.setVisible(False)
        self.vida5.setVisible(False)
        self.vida6.setVisible(False)
 
    def lifes(self, vida):
        self.vidasTotal.setText(str(vida))
        print(vida)
        if vida == 7:
            self.init.setVisible(True)
        elif vida == 6:
            self.vida1.setVisible(True)
        elif vida == 5:
            self.vida2.setVisible(True)
        elif vida == 4:
            self.vida3.setVisible(True)
        elif vida == 3:
            self.vida4.setVisible(True)
        elif vida == 2:
            self.vida5.setVisible(True)
        elif vida == 1:
            self.vida6.setVisible(True)
            
    def sort(self):
        global word
        f = open("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\palavras.txt", "r").read()
        separe = f.replace('\n', '')
        separe = separe.split(";")   
        sort = separe[random.randint(0, len(separe)-1)]
        word = sort.split(":")
    
    def game(self):
        global dig, vida, word, temp

        while True:
            temp = ''
            letra = self.input.text()
            self.send.clicked.connect(self.game)
            dig.append(letra)  

            for i in word[0]:
                if i in dig:
                    temp += i
                    
                else:
                    temp += "#"
            
            if temp == word[0]:
                #self.mask.setText(word[0])
                print('win')
                
            if letra == word[0]:
                print("win")
            else:
                self.mask.setText(temp)
                print(temp)
            
            if letra not in word[0]:
                vida -= 1   
                self.lifes(vida)   
            break
        #self.mask.setText(temp)
        #self.send.clicked.connect(self.game)
        
    def setupUi(self, MainWindow):
        global word
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 556)
        MainWindow.setStyleSheet("background-color: rgb(250, 250, 250);\n"
        "background-color: rgb(85, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort()
        self.init = QtWidgets.QLabel(self.centralwidget)
        self.init.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.init.setText("")
        self.init.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\init.png"))
        self.init.setScaledContents(True)
        self.init.setObjectName("init")
        
        self.vida1 = QtWidgets.QLabel(self.centralwidget)
        self.vida1.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.vida1.setText("")
        self.vida1.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\macacobraco1.png"))
        self.vida1.setScaledContents(True)
        self.vida1.setObjectName("vida1")
        
        self.vida2 = QtWidgets.QLabel(self.centralwidget)
        self.vida2.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.vida2.setText("")
        self.vida2.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\macacobracos.png"))
        self.vida2.setScaledContents(True)
        self.vida2.setObjectName("vida2")
        
        self.vida3 = QtWidgets.QLabel(self.centralwidget)
        self.vida3.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.vida3.setText("")
        self.vida3.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\macacocabeca.png"))
        self.vida3.setScaledContents(True)
        self.vida3.setObjectName("vida3")
        
        self.vida4 = QtWidgets.QLabel(self.centralwidget)
        self.vida4.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.vida4.setText("")
        self.vida4.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\macacocorpo.png"))
        self.vida4.setScaledContents(True)
        self.vida4.setObjectName("vida4")
        
        self.vida5 = QtWidgets.QLabel(self.centralwidget)
        self.vida5.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.vida5.setText("")
        self.vida5.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\macacoperna1.png"))
        self.vida5.setScaledContents(True)
        self.vida5.setObjectName("vida5")
        
        self.vida6 = QtWidgets.QLabel(self.centralwidget)
        self.vida6.setGeometry(QtCore.QRect(50, 70, 231, 301))
        self.vida6.setText("")
        self.vida6.setPixmap(QtGui.QPixmap("C:\\Users\\Vitor\\Desktop\\ikop\\misc\\hangmonkey\\macacomorto.png"))
        self.vida6.setScaledContents(True)
        self.vida6.setObjectName("vida6")
        
        self.element = QtWidgets.QLabel(self.centralwidget)
        self.element.setGeometry(QtCore.QRect(100, 10, 131, 41))
        self.element.setStyleSheet("border-radius: 15px;\n"
        "background-color: rgb(0, 0, 0);")
        self.element.setText("")
        self.element.setObjectName("element")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
        "color: white;")
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        # label vidas total
        self.vidasTotal = QtWidgets.QLabel(self.centralwidget)
        self.vidasTotal.setGeometry(QtCore.QRect(190, 20, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vidasTotal.setFont(font)
        self.vidasTotal.setStyleSheet("background-color: none;\n"
        "color: white;")
        self.vidasTotal.setText("")
        self.vidasTotal.setTextFormat(QtCore.Qt.MarkdownText)
        self.vidasTotal.setObjectName("vidasTotal")
        
        self.element_2 = QtWidgets.QLabel(self.centralwidget)
        self.element_2.setGeometry(QtCore.QRect(20, 430, 301, 41))
        self.element_2.setStyleSheet("border-radius: 15px;\n"
        "background-color: rgb(0, 0, 0);")
        self.element_2.setText("")
        self.element_2.setObjectName("element_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 440, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;\n"
        "color: white;")
        self.label_4.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_4.setObjectName("label_4")
        # label dica ------
        self.dica = QtWidgets.QLabel(self.centralwidget)
        self.dica.setGeometry(QtCore.QRect(70, 440, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dica.setFont(font)
        self.dica.setStyleSheet("background-color: none;\n"
        "color: white;")
        self.dica.setText(word[1])
        self.dica.setTextFormat(QtCore.Qt.MarkdownText)
        self.dica.setObjectName("dica")
        #line edit to try chars ---------
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(60, 480, 181, 41))
        self.input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 15px;")
        self.input.setObjectName("input")
        #send -------------------
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(250, 480, 61, 41))
        self.send.setStyleSheet("border-radius: 15px;\n"
        "border-color:1px rgb(0, 0, 0);\n"
        "background-color: rgb(213, 213, 213);\n"
        "")
        self.send.setObjectName("send")
        #self.send.clicked.connect(self.btn_ok)
        #label masked letters -----
        self.mask = QtWidgets.QLabel(self.centralwidget)
        self.mask.setGeometry(QtCore.QRect(40, 390, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mask.setFont(font)
        self.mask.setStyleSheet("background-color: none;\n"
        "color: white;")
        self.mask.setText("")
        self.mask.setTextFormat(QtCore.Qt.MarkdownText)
        self.mask.setObjectName("mask")
        self.mask.setText("")
        
        self.element_3 = QtWidgets.QLabel(self.centralwidget)
        self.element_3.setGeometry(QtCore.QRect(20, 380, 301, 41))
        self.element_3.setStyleSheet("border-radius: 15px;\n"
        "background-color: rgb(0, 0, 0);")
        self.element_3.setText("")
        self.element_3.setObjectName("element_3")
        self.element_3.raise_()
        self.init.raise_()
        self.vida1.raise_()
        self.vida2.raise_()
        self.vida3.raise_()
        self.vida4.raise_()
        self.vida5.raise_()
        self.vida6.raise_()
        self.element.raise_()
        self.label_2.raise_()
        self.vidasTotal.raise_()
        self.element_2.raise_()
        self.label_4.raise_()
        self.dica.raise_()
        self.input.raise_()
        self.send.raise_()
        self.mask.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.comecas()
        self.game()
        self.lifes(vida)
      
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "VIDAS:"))
        self.label_4.setText(_translate("MainWindow", "DICA:"))
        self.send.setText(_translate("MainWindow", "SEND"))

class Forca(Ui_MainWindow):
    def __init__(self, forca):
        self.setupUi(forca)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
