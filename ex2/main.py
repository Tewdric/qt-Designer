import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from ex2 import Ui_MainWindow

class ex2(QMainWindow):
    def __init__(self):
        super(ex2, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_Sum.clicked.connect(self.soma)
    
    def soma(self):
        try:
            num1 = int(self.ui.lineEdit_First.text())
            num2 = int(self.ui.lineEdit_Second.text())
            
            self.ui.label_Result.setText(str(num1 + num2))
        except:
            self.ui.label_Result.setText("Erro")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex2()
    window.show()
    sys.exit(app.exec_())