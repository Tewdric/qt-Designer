import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex14 import Ui_MainWindow

class ex14(QMainWindow):
    def __init__(self):
        super(ex14, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.res)
        
    def res(self):
        try:
            n1 = int(self.ui.lineEdit_1.text())
            n2 = int(self.ui.lineEdit_2.text())
            n3 = int(self.ui.lineEdit_3.text())
            n4 = int(self.ui.lineEdit_4.text())
            n5 = int(self.ui.lineEdit_5.text())
            
            lista = [n1, n2, n3, n4, n5]
            maior = max(lista)
            soma = sum(lista)
            media = sum(lista) / 5
            
            self.ui.label_resultado.setText(f"Maior: {maior} \n Soma: {soma} \n Media: {media}")
                    
        except ValueError:
            self.ui.label_resultado.setText(f"Erro, digite um valor válido")      
       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex14()
    window.show()
    sys.exit(app.exec_())