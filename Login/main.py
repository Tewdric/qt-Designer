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
        self.pushButton_cadastro.clicked.connect(self.cadastrar_usuario)
        
        db = DataBasse()
        dados = db.carregar_dados()
        

    def validar_login(self):
        login = self.lineEdit_login.text()
        senha = self.lineEdit_senha.text()
        
        db = DataBasse()
        dados = db.carregar_dados()
        
        for nome, senha in dados:
            if login == nome and senha == senha:
                print("Login realizado com sucesso")
                self.home = uic.loadUi("tela_home.ui")
                self.home.show()
                self.hide()
                
                self.home.label_saudacao.setText(f"Olá {nome}")
                break
            else:
                QMessageBox.critical(self, "Erro", "Login ou senha inválidos")
                break
        
    def cadastrar_usuario(self):
        self.cadastro = uic.loadUi("tela_cadastro.ui")
        self.cadastro.show()
        self.hide()
        
        self.cadastro.pushButton_cadastrar.clicked.connect(self.cadastrar)
        
    def cadastrar(self):
        nome = self.cadastro.lineEdit_nome.text()
        senha = self.cadastro.lineEdit_senha.text()
        email = self.cadastro.lineEdit_email.text()
        
        db = DataBasse()
        db.cadastrar_usuario(nome, senha, email)
        
        self.login.show()
        self.cadastro.hide()
        

if __name__ == "__main__":
    app = QApplication([])
    janela = tela_login()
    janela.show()
    app.exec_()