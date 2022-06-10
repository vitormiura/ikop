from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Hangman(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 544)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.NewGame = QtGui.QPushButton(self.centralwidget)
        self.NewGame.setGeometry(QtCore.QRect(0, 0, 151, 27))
        self.NewGame.setObjectName(_fromUtf8("NewGame"))
        self.Score = QtGui.QLabel(self.centralwidget)
        self.Score.setGeometry(QtCore.QRect(210, 0, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        self.Score.setFont(font)
        self.Score.setText(_fromUtf8(""))
        self.Score.setAlignment(QtCore.Qt.AlignCenter)
        self.Score.setObjectName(_fromUtf8("Score"))
        self.HeaderTag = QtGui.QLabel(self.centralwidget)
        self.HeaderTag.setGeometry(QtCore.QRect(150, 66, 321, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.HeaderTag.setFont(font)
        self.HeaderTag.setAlignment(QtCore.Qt.AlignCenter)
        self.HeaderTag.setObjectName(_fromUtf8("HeaderTag"))
        self.SecretWord = QtGui.QLabel(self.centralwidget)
        self.SecretWord.setGeometry(QtCore.QRect(0, 139, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SecretWord.setFont(font)
        self.SecretWord.setText(_fromUtf8(""))
        self.SecretWord.setAlignment(QtCore.Qt.AlignCenter)
        self.SecretWord.setObjectName(_fromUtf8("SecretWord"))
        self.TriesLeft = QtGui.QLabel(self.centralwidget)
        self.TriesLeft.setGeometry(QtCore.QRect(450, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        self.TriesLeft.setFont(font)
        self.TriesLeft.setText(_fromUtf8(""))
        self.TriesLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.TriesLeft.setObjectName(_fromUtf8("TriesLeft"))
        self.GuessLabel = QtGui.QLabel(self.centralwidget)
        self.GuessLabel.setGeometry(QtCore.QRect(160, 260, 301, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GuessLabel.setFont(font)
        self.GuessLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GuessLabel.setObjectName(_fromUtf8("GuessLabel"))
        self.InputChar = QtGui.QLineEdit(self.centralwidget)
        self.InputChar.setGeometry(QtCore.QRect(170, 380, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.InputChar.setFont(font)
        self.InputChar.setObjectName(_fromUtf8("InputChar"))
        self.Entered = QtGui.QLabel(self.centralwidget)
        self.Entered.setGeometry(QtCore.QRect(150, 320, 311, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Entered.setFont(font)
        self.Entered.setText(_fromUtf8(""))
        self.Entered.setAlignment(QtCore.Qt.AlignCenter)
        self.Entered.setObjectName(_fromUtf8("Entered"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.NewGame, QtCore.SIGNAL(_fromUtf8("clicked()")), self.InputChar.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.NewGame, QtCore.SIGNAL(_fromUtf8("clicked()")), self.restart)
        QtCore.QObject.connect(self.InputChar, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.update)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Hangman", "Hangman", None))
        self.NewGame.setText(_translate("Hangman", "New Game", None))
        self.HeaderTag.setText(_translate("Hangman", "Guess the Secret Word", None))
        self.GuessLabel.setText(_translate("Hangman", "Your Guesses", None))
        self.Score.setText(_translate("Hangman", "Score: "+str(score), None))
        self.TriesLeft.setText(_translate("Hangman", "Tries Left: "+str(triesLeft), None))
        self.SecretWord.setText(_translate("Hangman", secretDisplay, None))
        self.Entered.setText(_translate("Hangman", guesses, None))
        self.InputChar.setFocus()

    def update(self):
        global guesses, triesLeft, score, playing, secretWord, secretDisplay
        if playing:
            text=""
            try:
                text=_fromUtf8(self.InputChar.text())[-1]
                self.InputChar.setText(_translate("Hangman", "", None))
                guesses+=text+" "
            except IndexError:
                triesLeft+=1
            if triesLeft!=0:
                temp=[]
                for i in range(len(secretWord)):
                    if text==secretWord[i]:
                        temp.append(i)
                if len(temp)!=0:
                    for num in temp:
                        secretDisplay=secretDisplay[:2*num]+secretWord[num]+secretDisplay[2*num+1:]
                    if secretDisplay.count("_")==0:
                        guesses="You Win!! Start a New Game!"
                        score+=1
                        playing=False
                else:
                    triesLeft-=1
            if triesLeft==0:
                guesses="You Lose!! Start a New Game!"
                secretDisplay=""
                for char in secretWord:
                    secretDisplay+=char+" "
                score-=1
                playing=False
        self.retranslateUi(MainWindow)

    def restart(self):
        global score
        if playing:
            score-=1
        start()
        self.retranslateUi(MainWindow)

def start():
    global score, triesLeft, wordList, secretWord, secretDisplay, guesses, playing
    import random
    triesLeft=7
    # Provide a txt file named HangDict.txt containing a list of words, 1 word per line
    filehang=open("words.txt", "r").read() 
    separe = filehang.split(";")  
    secretWord=separe[random.randint(0, len(separe)-1)]
    #filehang.close()
    secretDisplay="_ "*len(secretWord)
    guesses=""
    playing=True

score=0
triesLeft=7
playing=True

if __name__ == "__main__":
    start()
    app = QtGui.QGuiApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Hangman()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
