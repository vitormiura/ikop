from PyQt5 import QtWidgets, uic 
import sys
from misc import velha as vl
from misc import menu as mn
from misc import jokenpo as jk
from misc import forca as frc

class Menu(mn.Ui_MainWindow):
    def __init__(self, menu_principal):
        self.setupUi(menu_principal)
        self.velhaButton.clicked.connect(self.openVelha)
        self.jokenpoButton.clicked.connect(self.openJokenpo)
        self.forcaButton.clicked.connect(self.openForca)
        
    def openVelha(self):
        self.game = QtWidgets.QMainWindow()
        self.j = vl.velhinha(self.game)
        self.game.show()
    
    def openForca(self):
        self.game = QtWidgets.QMainWindow()
        self.j = frc.Forca(self.game)
        self.game.show()
    
    def openJokenpo(self):
        self.game = QtWidgets.QWidget()
        self.j = jk.Jokenpo(self.game)
        self.game.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    menu_principal = QtWidgets.QMainWindow()
    m = Menu(menu_principal)
    menu_principal.show()
    sys.exit(app.exec_())
