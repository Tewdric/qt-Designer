import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex8 import Ui_MainWindow

class ex8(QMainWindow):
    def __init__(self):
        super(ex8, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton.clicked.connect(self.salario)
        
    def salario(self):
        ganho = float(self.ui.lineEdit_ganho.text())
        mes = float(self.ui.lineEdit_mes.text())

        res = ganho * mes
        self.ui.label_resultado.setText(f'R$ {res:,.2f}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex8()
    window.show()
    sys.exit(app.exec_())