import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from ex21 import Ui_MainWindow

class ex21(QMainWindow):
    def __init__(self):
        super(ex21, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # self.carregar_produtos()
        
        self.ui.pushButton.clicked.connect(self.adicionar_item)
        self.ui.pushButton_selecionarItem.clicked.connect(self.selecionar_item)
        self.ui.pushButton_comprar.clicked.connect(self.comprar)


    def selecionar_item(self):
        item = self.ui.tabelaProdutos.item(self.ui.tabelaProdutos.currentRow(), 0).text()
        preco = self.ui.tabelaProdutos.item(self.ui.tabelaProdutos.currentRow(), 1).text()
        
        self.adicionar_lista_compra(item, preco)
    

    def adicionar_lista_compra(self, item, preco):
        slice = preco.split('R$')
        preco = slice[1]
        
        soma = 0
        soma += float(preco)
        
        self.ui.tabelaCarrinho.insertRow(0)
        self.ui.tabelaCarrinho.setItem(0, 0, QTableWidgetItem(item))
        self.ui.tabelaCarrinho.setItem(0, 1, QTableWidgetItem(preco))
    

    def comprar(self):
        total = 0
        for i in range(self.ui.tabelaCarrinho.rowCount()):
            total += (float(self.ui.tabelaCarrinho.item(i, 2).text())*float(self.ui.tabelaCarrinho.item(i, 1).text()))
        
        self.ui.label_total.setText("Total: R$ "+str(total))
        self.ui.tabelaCarrinho.clearContents()

        
    def adicionar_item(self):
        item = self.ui.lineEdit_item.text()
        preco = self.ui.lineEdit_preco.text()

        self.ui.tabelaProdutos.insertRow(0)
        self.ui.tabelaProdutos.setItem(0, 0, QTableWidgetItem(item))
        self.ui.tabelaProdutos.setItem(0, 1, QTableWidgetItem('R$ '+preco))
        
        self.ui.lineEdit_item.clear()
        self.ui.lineEdit_preco.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex21()
    window.show()
    sys.exit(app.exec_())