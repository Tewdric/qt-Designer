import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex18 import Ui_MainWindow

class ex18(QMainWindow):
    def __init__(self):
        super(ex18, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.reverso)
        
    def reverso(self):
        palavra = self.ui.lineEdit.text()
        if palavra:
            palavra = palavra[::-1]
            self.ui.label.setText(palavra)
        else:
            QMessageBox.warning(self, "Aviso", "Digite uma palavra")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ex18()
    window.show()
    sys.exit(app.exec_())