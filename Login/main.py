import sys
import os
from datetime import datetime


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

        login_sucesso = False  # Variável para verificar se o login foi bem-sucedido

        for usuario in dados:  # Percorre todos os registros do banco de dados
            if login == usuario[0] and senha == usuario[1]:
                print("Login realizado com sucesso")
                self.hide()
                self.cadastro = uic.loadUi("tela_cadastro.ui")
                self.cadastro.show()
                self.cadastro.pushButton_cadastrar.clicked.connect(self.cadastrar)
                login_sucesso = True  # Indica que o login foi bem-sucedido
                break  # Sai do loop após encontrar um login válido

        if not login_sucesso:  # Só exibe o erro se nenhum login for bem-sucedido
            QMessageBox.critical(self, "Erro", "Login ou senha incorretos.")

               
    def cadastrar(self):
        db = DataBasse()
        dados = db.selecionar_usuario()
        print(dados)

        nome = self.cadastro.lineEdit_nome.text()
        senha = self.cadastro.lineEdit_senha.text()
        email = self.cadastro.lineEdit_email.text()
        cpf = self.cadastro.lineEdit_cpf.text()
        nascimento = self.cadastro.dateEdit.text()
        nascimento_formatado = nascimento.replace("/", "-")

        # Convertendo para o formato desejado (YYYY-MM-DD)
        data_formatada = datetime.strptime(nascimento_formatado, "%d-%m-%Y").strftime("%Y-%m-%d")

        print(nome,senha,email, cpf, data_formatada)


        if(nome == "" and senha == "" and email == "" and cpf == "" and nascimento == ""):
            QMessageBox.critical(self, "Erro", "Cadastro não realizado.")
        else:
            db = DataBasse()
            db.cadastrar_usuario(nome, senha, email, cpf, nascimento)
            
            QMessageBox.information(self, "Sucesso", "Cadastro realizado com sucesso.")
            self.cadastro.hide()

        

if __name__ == "__main__":
    app = QApplication([])
    janela = tela_login()
    janela.show()
    app.exec_()