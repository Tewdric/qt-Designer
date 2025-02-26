import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from tela_inicial import Ui_MainWindow
from PyQt5 import QtWidgets, uic

class tela_inicial(QMainWindow):
    def __init__(self):
        super(tela_inicial, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tela_cadastro = uic.loadUi("tela_cadastro.ui")  # Carrega a segunda tela

        self.ui.pushButton_cadastro.clicked.connect(self.mostrar_telaCadastro)
        self.ui.pushButton_comprar.clicked.connect(self.mostrar_telaCompra)
        

    def mostrar_telaCadastro(self):
        self.tela_cadastro.show()  # Mostra a segunda tela
        self.hide()  # Oculta a primeira tela
        
        self.tela_cadastro.pushButton_home.clicked.connect(self.voltar_tela_inicial)
        self.tela_cadastro.pushButton_cadastrarProduto.clicked.connect(self.cadastrando_produto)
    
    def mostrar_telaCompra(self):
        self.tela_compra.show()  # Mostra a segunda tela
        self.hide()  # Oculta a primeira tela
        
        self.tela_compra.pushButton_voltar.clicked.connect(self.voltar_tela_inicial)
        self.tela_compra.pushButton_selecionar.clicked.connect(self.selecionar_produto)
        self.tela_compra.pushButton_FinalizarCompra.clicked.connect(self.FinalizarCompra)
    
    def selecionar_produto(self):
        self.tela_compra.tableWidget_2.setRowCount(self.tela_compra.tableWidget_2.rowCount()+1)#linha
        self.tela_compra.tableWidget_2.setItem(self.tela_compra.tableWidget_2.rowCount()-1, 0, QTableWidgetItem(self.tela_compra.tableWidget.item(self.tela_compra.tableWidget.currentRow(), 0).text()))#coluna 0 = nome
        self.tela_compra.tableWidget_2.setItem(self.tela_compra.tableWidget_2.rowCount()-1, 1, QTableWidgetItem(self.tela_compra.tableWidget.item(self.tela_compra.tableWidget.currentRow(), 1).text()))#coluna 1 = preço
        self.tela_compra.tableWidget_2.setItem(self.tela_compra.tableWidget_2.rowCount()-1, 2, QTableWidgetItem("1"))#coluna 2 = quantidade

     

    def FinalizarCompra(self):
        total = 0
        for i in range(self.tela_compra.tableWidget_2.rowCount()):
            total += float(self.tela_compra.tableWidget_2.item(i, 1).text())
            quantidade = int(self.tela_compra.tableWidget_2.item(i, 2).text())
            resultado = total * quantidade
            
            
            
        QMessageBox.about(self, "Total da compra", f"O total da compra é de R${resultado:.2f}")
        
    def voltar_tela_inicial(self):
        self.tela_cadastro.hide()  # Oculta a segunda tela
        self.tela_compra.hide()  # Oculta a terceira tela
        self.show()  # Mostra a primeira tela
        
    def cadastrando_produto(self):
        nome_produto = self.tela_cadastro.lineEdit.text()
        valor_produto = self.tela_cadastro.lineEdit_2.text()
        
        self.tela_cadastro.tableWidget.setRowCount(self.tela_cadastro.tableWidget.rowCount() + 1)
        self.tela_cadastro.tableWidget.setItem(self.tela_cadastro.tableWidget.rowCount() - 1, 0, QTableWidgetItem(nome_produto))
        self.tela_cadastro.tableWidget.setItem(self.tela_cadastro.tableWidget.rowCount() - 1, 1, QTableWidgetItem(valor_produto))
        
        self.tela_compra.tableWidget.setRowCount(self.tela_compra.tableWidget.rowCount() + 1)
        self.tela_compra.tableWidget.setItem(self.tela_compra.tableWidget.rowCount() - 1, 0, QTableWidgetItem(nome_produto))
        self.tela_compra.tableWidget.setItem(self.tela_compra.tableWidget.rowCount() - 1, 1, QTableWidgetItem(valor_produto))
        
        self.tela_cadastro.lineEdit.clear()
        self.tela_cadastro.lineEdit_2.clear()
    
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = tela_inicial()
    window.show()
    sys.exit(app.exec_())