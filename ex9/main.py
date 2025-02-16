import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex9 import Ui_MainWindow

class ex9(QMainWindow):
    def __init__(self):
        super(ex9, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.tinta)
        
    def tinta(self):
        metros = int(self.ui.lineEdit_ganho.text())
        
        lata = 54
        preco = 80
        
        if metros > lata:
            latas = 0
            i= 0
            
            while latas < metros:
                latas += lata
                i += 1
            self.ui.label_resultado.setText(f"Você vai precisar de {i} lata(s) de tinta\nR${i*preco:.2f}")
        else:
            self.ui.label_resultado.setText(f"Você vai precisar de 1 lata de tinta")
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex9()
    window.show()
    sys.exit(app.exec_())