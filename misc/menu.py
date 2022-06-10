from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 338)
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
        self.forcaButton.setGeometry(QtCore.QRect(210, 180, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(14)
        self.forcaButton.setFont(font)
        self.forcaButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.forcaButton.setObjectName("forcaButton")
        self.velhaButton = QtWidgets.QPushButton(self.centralwidget)
        self.velhaButton.setGeometry(QtCore.QRect(10, 180, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(14)
        self.velhaButton.setFont(font)
        self.velhaButton.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;\n"
"background-color: rgb(255, 170, 255);")
        self.velhaButton.setObjectName("velhaButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-60, 0, 471, 361))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("fund-programacao\Python\pyqt\misc\hqdefault.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.jokenpoButton = QtWidgets.QPushButton(self.centralwidget)
        self.jokenpoButton.setGeometry(QtCore.QRect(110, 270, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(14)
        self.jokenpoButton.setFont(font)
        self.jokenpoButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Jogos"))
        self.forcaButton.setText(_translate("MainWindow", "Jogo da Forca"))
        self.velhaButton.setText(_translate("MainWindow", "Jogo da Velha"))
        self.jokenpoButton.setText(_translate("MainWindow", "Jankenpon"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
