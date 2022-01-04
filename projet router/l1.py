# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import welcome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 454)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 151, 81))
        self.label.setStyleSheet("color: rgb(85, 170, 255);\n"
"font: 8pt \"Segoe Print\";\n"
"font-size : 30pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 101, 31))
        self.label_2.setStyleSheet("color: rgb(245, 245, 245); font-size: 15pt;")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(200, 190, 141, 31))
        self.username.setStyleSheet("color: rgb(255, 255, 255); \n"
"font-size:14pt;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(200, 260, 141, 31))
        self.password.setStyleSheet("color: rgb(255, 255, 255); \n"
"font-size:14pt;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        
        
        
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 260, 101, 31))
        self.label_3.setStyleSheet("color: rgb(245, 245, 245); font-size:15pt;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 400, 141, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Script MT Bold\";")
        self.label_4.setObjectName("label_4")
        self.loginbut = QtWidgets.QPushButton(self.centralwidget)
        self.loginbut.setGeometry(QtCore.QRect(160, 340, 91, 31))
        self.loginbut.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.loginbut.setObjectName("loginbut")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 0, 61, 61))
        self.label_6.setStyleSheet("background-image: url(:/testt/UPEC - Logo - Noir - 200x200.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/testt/UPEC - Logo - Noir - 200x200.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", " Login"))
        self.label_2.setText(_translate("MainWindow", "UserName"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Designed By Youssef SASSi"))
        self.loginbut.setText(_translate("MainWindow", "Login"))

        self.loginbut.clicked.connect(self.loginfunction)
        
    
    
    def loginfunction(self):
        a=self.username.text()
        b=self.password.text()
        host = "etudiant"
        mdp= "vitrygtr"
        
        if a == host and b == mdp:
            print("connected")
            user = self.username.text()
            mdp = self.password.text()
             
            print(user,mdp)
            MainWindow2.show()
            MainWindow.hide()
            
#            self.OpenForm = QtWidgets.QWidget()
#            self.Openui = welcome.Ui_Form()
#            self.Openui.setupUi(self.OpenForm)
#            self.OpenForm.show()
        else:
            print("Resseyer mdp ou identifant incorect")
            user = self.username.text()
            mdp = self.password.text()
            print(user,mdp)


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    #configuration de la fenetre L1 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #configuration de la fenetre welcome
    MainWindow2 = QtWidgets.QMainWindow() 
    welcome = welcome.Ui_MainWindow()
    welcome.setupUi(MainWindow2)
    sys.exit(app.exec_())

