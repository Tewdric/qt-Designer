import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex11 import Ui_MainWindow

class ex11(QMainWindow):
    def __init__(self):
        super(ex11, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.numeros)
        
    def numeros(self):
        try:
            num1 = int(self.ui.lineEdit_1.text())
            num2 = int(self.ui.lineEdit_2.text())
            num3 = int(self.ui.lineEdit_3.text())
            
            maior = max(num1, num2, num3)
            menor = min(num1, num2, num3)
            
            self.ui.label_resultado.setText(f"O maior número é {maior} e o menor número é {menor}")
                    
        except ValueError:
            self.ui.label_resultado.setText(f"Erro, digite um valor válido")      
       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex11()
    window.show()
    sys.exit(app.exec_())