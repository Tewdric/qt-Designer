import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from tela_login import Ui_Form
from PyQt5 import QtWidgets, uic

class tela_login(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cadastro = uic.loadUi("tela_cadastro.ui")
        
        self.ui.pushButton_entrar.clicked.connect(self.mostrar_telaCadastro)
    
    def mostrar_telaCadastro(self):
        self.cadastro.show()
        self.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())