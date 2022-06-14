from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 530)
        Form.setMinimumSize(QtCore.QSize(450, 530))
        Form.setMaximumSize(QtCore.QSize(450, 530))
        Form.setStyleSheet("\n"
"background-color: rgb(170, 0, 255);")
        self.btn_pedra = QtWidgets.QPushButton(Form)
        self.btn_pedra.setGeometry(QtCore.QRect(20, 210, 111, 81))
        self.btn_pedra.setStyleSheet("background-color: transparent;")
        self.btn_pedra.setText("")
        self.btn_pedra.setObjectName("btn_pedra")
        self.btn_papel = QtWidgets.QPushButton(Form)
        self.btn_papel.setGeometry(QtCore.QRect(180, 210, 91, 71))
        self.btn_papel.setStyleSheet("background-color: transparent;")
        self.btn_papel.setText("")
        self.btn_papel.setObjectName("btn_papel")
        self.btn_tesoura = QtWidgets.QPushButton(Form)
        self.btn_tesoura.setGeometry(QtCore.QRect(310, 200, 111, 91))
        self.btn_tesoura.setStyleSheet("background-color: transparent;")
        self.btn_tesoura.setText("")
        self.btn_tesoura.setObjectName("btn_tesoura")
        self.resposta = QtWidgets.QLabel(Form)
        self.resposta.setGeometry(QtCore.QRect(90, 330, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resposta.setFont(font)
        self.resposta.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.resposta.setText("")
        self.resposta.setObjectName("resposta")
        self.btn_reset = QtWidgets.QPushButton(Form)
        self.btn_reset.setGeometry(QtCore.QRect(190, 420, 71, 61))
        self.btn_reset.setStyleSheet("background-color: transparent;")
        self.btn_reset.setText("")
        self.btn_reset.setObjectName("btn_reset")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 531))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("misc/jokenpo/Jankenpon.png"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.btn_pedra.raise_()
        self.btn_papel.raise_()
        self.btn_tesoura.raise_()
        self.resposta.raise_()
        self.btn_reset.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Jokenpenbas"))

class Jokenpo(Ui_Form):
    
    escolhas = ['pedra', 'papel', 'tesoura']
    escolha = ''
    
    def __init__(self, joken_po):
        self.setupUi(joken_po)
        self.btn_pedra.clicked.connect(self.pedra_click)
        self.btn_papel.clicked.connect(self.papel_click)
        self.btn_tesoura.clicked.connect(self.tesoura_click)
        self.btn_reset.clicked.connect(self.reset)
        __class__.__sortear()
        
    
    def verificar_vitoria(self):
        if self.escolha == 'pedra' and Jokenpo.escolha == 'tesoura':
            self.resposta.setText("Você venceu!")
        elif self.escolha == 'tesoura' and Jokenpo.escolha == 'pedra':
            self.resposta.setText("Computador venceu!")
        elif self.escolha == 'tesoura' and Jokenpo.escolha == 'papel':
            self.resposta.setText("Você venceu!")
        elif self.escolha == 'papel' and Jokenpo.escolha == 'tesoura':
            self.resposta.setText("Computador venceu!")
        elif self.escolha == 'papel' and Jokenpo.escolha == 'pedra':
            self.resposta.setText("Você venceu!")
        elif self.escolha == 'pedra' and Jokenpo.escolha == 'papel':
            self.resposta.setText("Computador venceu!")    
            
        elif self.escolha == 'papel' and Jokenpo.escolha == 'papel':
            self.resposta.setText("EMPATE!")
        elif self.escolha == 'pedra' and Jokenpo.escolha == 'pedra':
            self.resposta.setText("EMPATE!")
        elif self.escolha == 'tesoura' and Jokenpo.escolha == 'tesoura':
            self.resposta.setText("EMPATE!")
        
        self.btn_pedra.setEnabled(False)
        self.btn_papel.setEnabled(False)
        self.btn_tesoura.setEnabled(False)
    
    def pedra_click(self):
        self.escolha = 'pedra'
        self.verificar_vitoria()
        
    def papel_click(self):
        self.escolha = 'papel'
        self.verificar_vitoria()
        
    def tesoura_click(self):
        self.escolha = 'tesoura'
        self.verificar_vitoria()
    
    def reset(self):
        self.btn_pedra.setEnabled(True)
        self.btn_papel.setEnabled(True)
        self.btn_tesoura.setEnabled(True)
        __class__.__sortear()
        self.resposta.setText("Jogue novamente...")
        
    @staticmethod
    def __sortear():
        __class__.escolha = random.choice(Jokenpo.escolhas)
        print(Jokenpo.escolha)   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
