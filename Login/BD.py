
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
    
    def cadastrar_usuario(self, nome, senha, email, cpf, nascimento):
        try:
            conn = MySQLdb.connect(
                host="localhost",
                user="root",
                passwd="",
                db="qt_atividade",
                charset="utf8"
            )

            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (nome, senha, email, cpf, nascimento) VALUES (%s, %s, %s,%s,%s)", (nome, senha, email, cpf, nascimento))
            conn.commit()
            return 'Sucess'
        except MySQLdb.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
    
    def selecionar_usuario(self):
        try:
            conn = MySQLdb.connect(
                host="localhost",
                user="root",
                passwd="",
                db="qt_atividade",
                charset="utf8"
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            dados = cursor.fetchall()  # Obtém todos os registros da tabela

            return dados  # Retorna os dados obtidos

        except MySQLdb.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()


     



teste = DataBasse()
print(teste.carregar_dados())


        