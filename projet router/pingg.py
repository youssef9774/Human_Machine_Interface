# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pingg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import command
import router
ping = " ping "

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 280)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 200, 81, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 12pt \"Lucida Handwriting\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.ping1 = QtWidgets.QLineEdit(self.centralwidget)
        self.ping1.setGeometry(QtCore.QRect(160, 40, 141, 20))
        self.ping1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.ping1.setObjectName("ping1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 70, 391, 121))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(76, 40, 71, 20))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 220, 151, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Script MT Bold\";")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 261, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 81 14pt \"Rockwell Extra Bold\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 0, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 12pt \"Lucida Handwriting\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ping"))
        self.pushButton.setText(_translate("MainWindow", "Ping ME"))
        self.label.setText(_translate("MainWindow", "Adresse IP"))
        self.label_5.setText(_translate("MainWindow", "Designed By Youssef SASSi"))
        self.label_2.setText(_translate("MainWindow", "Test de la Connexion"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        
        self.pushButton.clicked.connect(self.aff_ping)
        self.pushButton_2.clicked.connect(self.exit)

    
    
    def aff_ping(self):
        b1 = self.ping1.text()
        self.textEdit.setText(command.afficherRoutage1(ping + b1))
        print(command.afficherRoutage1(ping + b1))
        
    def exit(self):
        MainWindow.close()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

