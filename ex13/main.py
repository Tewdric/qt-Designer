import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex13 import Ui_MainWindow

class ex13(QMainWindow):
    def __init__(self):
        super(ex13, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.saudacao)
        
    def saudacao(self):
        try:
            if self.ui.radioButton_M.isChecked():
                self.ui.label_resultado.setText(f"Olá, Bom dia!")
            elif self.ui.radioButton_V.isChecked():
                self.ui.label_resultado.setText(f"Olá, Boa tarde!")
            elif self.ui.radioButton_N.isChecked():
                self.ui.label_resultado.setText(f"Olá, Boa noite!")
                    
        except ValueError:
            self.ui.label_resultado.setText(f"Erro, digite um valor válido")      
       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex13()
    window.show()
    sys.exit(app.exec_())