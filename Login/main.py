import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5 import QtWidgets, uic
from tela_home import Ui_Form
from tela_cadastro import Ui_Form
from tela_login import Ui_Form
from BD import DataBasse

class tela_login(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login = uic.loadUi("tela_login.ui")
        
        self.pushButton_entrar.clicked.connect(self.validar_login)
        
        db = DataBasse()
        dados = db.carregar_dados()
        

    def validar_login(self):
        login = self.lineEdit_login.text()
        senha = self.lineEdit_senha.text()

        db = DataBasse()
        dados = db.carregar_dados()


        for i in range(len(dados)):
            print(dados[i][0],dados[i][1])
            if login == dados[i][0] and senha == dados[i][1]:
                print("Login realizado com sucesso")
                self.hide()
                self.cadastro = uic.loadUi("tela_cadastro.ui")
                self.cadastro.show()
                
                self.cadastro.pushButton_cadastrar.clicked.connect(self.cadastrar)

               
    def cadastrar(self):
        nome = self.cadastro.lineEdit_nome.text()
        senha = self.cadastro.lineEdit_senha.text()
        email = self.cadastro.lineEdit_email.text()
        print(nome,senha,email)


        if(nome == "" and senha == "" and email == ""):
            QMessageBox.critical(self, "Erro", "Cadastro não realizado.")
        else:
            db = DataBasse()
            db.cadastrar_usuario(nome, senha, email)
            
            QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso.")
            self.cadastro.hide()

        

if __name__ == "__main__":
    app = QApplication([])
    janela = tela_login()
    janela.show()
    app.exec_()