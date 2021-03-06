from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 60, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent;\n"
"color: white;")
        self.label.setObjectName("label")
        self.forcaButton = QtWidgets.QPushButton(self.centralwidget)
        self.forcaButton.setGeometry(QtCore.QRect(260, 430, 221, 221))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(14)
        self.forcaButton.setFont(font)
        self.forcaButton.setStyleSheet("background-color: transparent;\n"
"")
        self.forcaButton.setText("")
        self.forcaButton.setObjectName("forcaButton")
        self.velhaButton = QtWidgets.QPushButton(self.centralwidget)
        self.velhaButton.setGeometry(QtCore.QRect(450, 180, 201, 201))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(14)
        self.velhaButton.setFont(font)
        self.velhaButton.setStyleSheet("background-color: transparent;\n"
"")
        self.velhaButton.setText("")
        self.velhaButton.setObjectName("velhaButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("misc/menu/menu.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.jokenpoButton = QtWidgets.QPushButton(self.centralwidget)
        self.jokenpoButton.setGeometry(QtCore.QRect(70, 190, 221, 181))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(14)
        self.jokenpoButton.setFont(font)
        self.jokenpoButton.setStyleSheet("background-color: transparent;\n"
"")
        self.jokenpoButton.setText("")
        self.jokenpoButton.setObjectName("jokenpoButton")
        self.label_3.raise_()
        self.label.raise_()
        self.forcaButton.raise_()
        self.velhaButton.raise_()
        self.jokenpoButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IKOP MINIGAMES"))
        self.label.setText(_translate("MainWindow", "Jogos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
