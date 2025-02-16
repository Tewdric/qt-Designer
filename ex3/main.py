import sys

from ex3 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class ex3(QMainWindow):
    def __init__(self):
        super(ex3,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_Result.clicked.connect(self.result)

    def result(self):
        try:
            num = int(self.ui.lineEdit_First.text())
            if num % 2 == 0:
                self.ui.label_Result.setText(f'O Número {num} é Par')
            else:
                self.ui.label_Result.setText(f'O Número {num} é Impar')
        except:
            self.ui.label_Result.setText('Erro')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex3()
    window.show()
    sys.exit(app.exec_())