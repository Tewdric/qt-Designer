# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex13.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-110, 370, 47, 13))
        self.label.setObjectName("label")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(210, 150, 361, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_resultado.setFont(font)
        self.label_resultado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_resultado.setAutoFillBackground(False)
        self.label_resultado.setText("")
        self.label_resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resultado.setWordWrap(True)
        self.label_resultado.setObjectName("label_resultado")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(340, 40, 86, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_M = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_M.setFont(font)
        self.radioButton_M.setObjectName("radioButton_M")
        self.verticalLayout.addWidget(self.radioButton_M)
        self.radioButton_V = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_V.setFont(font)
        self.radioButton_V.setObjectName("radioButton_V")
        self.verticalLayout.addWidget(self.radioButton_V)
        self.radioButton_N = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_N.setFont(font)
        self.radioButton_N.setObjectName("radioButton_N")
        self.verticalLayout.addWidget(self.radioButton_N)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Resultado"))
        self.radioButton_M.setText(_translate("MainWindow", "Matutino"))
        self.radioButton_V.setText(_translate("MainWindow", "Vespertino"))
        self.radioButton_N.setText(_translate("MainWindow", "Noturno"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
