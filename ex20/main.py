import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex20 import Ui_MainWindow

class ex20(QMainWindow):
    def __init__(self):
        super(ex20, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.vertical)
        
    def vertical(self):
        letrinhas = {
            'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0,
            ' ':0
        }
        
        espaco = ''
        
        palavra = self.ui.lineEdit.text()
        
        if palavra:
            
            for letra in palavra:
                if letra in letrinhas:
                    letrinhas[letra] += 1
                
                    
            self.ui.lineEdit.clear()
            self.ui.label.setText("Quantidade de vogais\nA: {}\nE: {}\nI: {}\nO: {}\nU: {}\nEspaço: {}".format(letrinhas['a'], letrinhas['e'], letrinhas['i'], letrinhas['o'], letrinhas['u'], letrinhas[' ']))
            
          
                
        else:
            QMessageBox.warning(self, "Aviso", "Digite uma palavra")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex20()
    window.show()
    sys.exit(app.exec_())