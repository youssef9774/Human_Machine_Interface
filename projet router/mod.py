# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 416)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.liree = QtWidgets.QPushButton(self.centralwidget)
        self.liree.setGeometry(QtCore.QRect(240, 310, 75, 23))
        self.liree.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Ravie\";")
        self.liree.setObjectName("liree")
        self.textLire = QtWidgets.QTextEdit(self.centralwidget)
        self.textLire.setGeometry(QtCore.QRect(90, 50, 391, 241))
        self.textLire.setStyleSheet("color: rgb(255, 255, 255);")
        self.textLire.setObjectName("textLire")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 310, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 371, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Showcard Gothic\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 340, 371, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Showcard Gothic\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modification"))
        self.liree.setText(_translate("MainWindow", "Lire"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Modification par l\'utilisateur"))
        self.label_2.setText(_translate("MainWindow", "Copy Right Youssef SASSI "))
        
        self.liree.clicked.connect(self.lire)
        self.pushButton.clicked.connect(self.exit)
    #fonction pour lire le ficher data1 et le mettre dans une variable s 
    #apres j'ai le mit dans une zone de text avec l'objectname (textlire)  pour l'affciher utilisant la setteur   
    def lire(self):
        f = open("data1.txt","r")
        s = f.read()
        print(s)
        f.close()
        self.textLire.setText(s)
        
        
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

