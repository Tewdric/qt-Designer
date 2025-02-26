
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys

import MySQLdb

class DataBasse:
    def __init__(self):
        self.conexao = None
        self.cursor = None

    def carregar_dados(self):
                # Conectando ao banco de dados MySQL usando MySQLdb
                conn = MySQLdb.connect(
                    host="localhost",
                    user="root",
                    passwd="",
                    db="qt_atividade",
                    charset="utf8"
                )

                cursor = conn.cursor()
                cursor.execute("SELECT  nome, senha FROM usuario")  # Ajuste a consulta conforme necessário
                resultados = cursor.fetchall()
                
                return resultados
    
    def cadastrar_usuario(self, nome, senha, email):
        try:
            conn = MySQLdb.connect(
                host="localhost",
                user="root",
                passwd="",
                db="qt_atividade",
                charset="utf8"
            )

            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (nome, senha, email) VALUES (%s, %s, %s)", (nome, senha, email))
            conn.commit()
            print("Usuário cadastrado com sucesso!")
        except MySQLdb.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")


teste = DataBasse()
print(teste.carregar_dados())


        