import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex10 import Ui_MainWindow

class ex10(QMainWindow):
    def __init__(self):
        super(ex10, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.tempo)
        
    def tempo(self):
        contador = {
            'segundo': 0,
            'minuto': 0,
            'hora': 0
        }
        try:
            mb = int(self.ui.lineEdit_mb.text())
            velocidade = int(self.ui.lineEdit_velocidade.text())
            
            if mb > 0 and velocidade > 0:
                tempo = (mb*8)/velocidade
                
                while tempo >= 3600:
                    contador['hora'] += 1
                    tempo -= 3600
                while tempo >= 60:
                    contador['minuto'] += 1
                    tempo -= 60
                while tempo >= 1:
                    contador['segundo'] += 1
                    tempo -= 1
                    
                self.ui.label_resultado.setText(f"{contador['hora']} horas, {contador['minuto']} minutos e {contador['segundo']} segundos")
                    
        except ValueError:
            self.ui.label_resultado.setText(f"Erro, digite um valor válido")      
       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex10()
    window.show()
    sys.exit(app.exec_())