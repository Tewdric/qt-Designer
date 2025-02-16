import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from ex4 import Ui_MainWindow

class ex4(QMainWindow):
    def __init__(self):
        super(ex4, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.pushButton_Result.clicked.connect(self.fatorial)
        
    def fatorial(self):
        num = int(self.ui.lineEdit_First.text())
        fat = 1
        lista = []
        for i in range(1, num + 1):
            fat *= i
            lista.append(str(i))
        self.ui.label_Result.setText(f'Fatorial de {num} = {fat} = {"".join(lista)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex4()
    window.show()
    sys.exit(app.exec_())