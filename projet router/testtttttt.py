# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import router 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 318)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 161, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 381, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25pt;")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 260, 141, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Script MT Bold\";")
        self.label_4.setObjectName("label_4")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(140, 180, 131, 41))
        self.btn1.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.btn1.setObjectName("btn1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 0, 61, 61))
        self.label_6.setStyleSheet("background-image: url(:/testt/UPEC - Logo - Noir - 200x200.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/testt/UPEC - Logo - Noir - 200x200.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bienvenue"))
        self.label.setText(_translate("MainWindow", "Bienvenue"))
        self.label_2.setText(_translate("MainWindow", "Configuration des routeur"))
        self.label_4.setText(_translate("MainWindow", "Designed By Youssef SASSi"))
        self.btn1.setText(_translate("MainWindow", "Démarrer"))
#        
        self.btn1.clicked.connect(self.routerfunction)
    #configuration de la fenetre routeur    
    def routerfunction(self):
        MainWindow3 = QtWidgets.QMainWindow() 
        rout = router.Ui_Routeur()
        rout.setupUi(MainWindow3)
        MainWindow3.show()
        MainWindow.hide()



if __name__ == "__main__":
    
    
    #configuration de page welcome
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    
    
   

