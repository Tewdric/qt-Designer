import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex15 import Ui_MainWindow

class ex15(QMainWindow):
    def __init__(self):
        super(ex15, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnAdicionar.clicked.connect(self.adicionar_preco)
        self.ui.btnCalcularMedia.clicked.connect(self.calcular_media)
        
    def adicionar_preco(self):
        """Adiciona o preço digitado na lista."""
        quantidade = int(self.ui.lineEdit_qtd.text())
        texto = self.ui.lineEditPreco.text()

        try:
            preco = float(texto)  # Converte para número
            self.ui.listWidgetPrecos.addItem(f"{preco:.2f}")  # Adiciona formatado
            self.ui.lineEditPreco.clear()  # Limpa o campo
            
            if self.ui.listWidgetPrecos.count() == int(quantidade):
                self.calcular_media()
                
        except ValueError:
            QMessageBox.warning(self, "Erro", "Digite um número válido!")

    def calcular_media(self):
        """Calcula e exibe a média dos preços."""
        total = 0
        count = self.ui.listWidgetPrecos.count()

        if count == 0:
            QMessageBox.information(self, "Aviso", "Adicione preços antes de calcular a média.")
            return

        for i in range(count):
            item = self.ui.listWidgetPrecos.item(i).text()
            total += float(item)

        media = total / count
        self.ui.labelMedia.setText(f"Média: R$ {media:.2f}")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex15()
    window.show()
    sys.exit(app.exec_())