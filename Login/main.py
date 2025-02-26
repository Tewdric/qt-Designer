import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5 import QtWidgets, uic
from tela_login import Ui_Form
from tela_cadastro import Ui_Form

class tela_cadastro(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        

        self.pushButton_entrar.clicked.connect(self.entrar)

    def entrar(self):
        uic.loadUi("tela_login.py", self) 
        self.tela_login.show()
        self.hide()

            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = tela_cadastro()
    window.show()
    sys.exit(app.exec_())
