import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex12 import Ui_MainWindow

class ex12(QMainWindow):
    def __init__(self):
        super(ex12, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.numeros)
        
    def numeros(self):
        try:
            num1 = int(self.ui.lineEdit_1.text())
            num2 = int(self.ui.lineEdit_2.text())
            num3 = int(self.ui.lineEdit_3.text())
            
            num = [num1, num2, num3]
            num.sort(reverse=False)
            
            self.ui.label_resultado.setText(f"{num}")
                    
        except ValueError:
            self.ui.label_resultado.setText(f"Erro, digite um valor válido")      
       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex12()
    window.show()
    sys.exit(app.exec_())