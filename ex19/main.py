import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex19 import Ui_MainWindow

class ex19(QMainWindow):
    def __init__(self):
        super(ex19, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.vertical)
        
    def vertical(self):
        palavra = self.ui.lineEdit.text()
        texto = ''
        
        if palavra:
            
            for letra in palavra:
                texto += letra + '\n'
                
            self.ui.label.setText(texto)
            
          
                
        else:
            QMessageBox.warning(self, "Aviso", "Digite uma palavra")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex19()
    window.show()
    sys.exit(app.exec_())