# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'router.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import config
import config2
import ReadME

class Ui_Routeur(object):
    def setupUi(self, Routeur):
        Routeur.setObjectName("Routeur")
        Routeur.resize(445, 401)
        Routeur.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Routeur)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 311, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 25pt;")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 340, 141, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Script MT Bold\";")
        self.label_4.setObjectName("label_4")
        self.ME_but = QtWidgets.QPushButton(self.centralwidget)
        self.ME_but.setGeometry(QtCore.QRect(360, 10, 71, 31))
        self.ME_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:8pt;\n"
"background-color: rgb(167, 168, 167);")
        self.ME_but.setObjectName("ME_but")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 300, 71, 61))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/C:/Users/youssef/Desktop/UPEC - Logo - Noir - 200x200.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/C:/Users/youssef/Desktop/UPEC - Logo - Noir - 200x200.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.R1_but = QtWidgets.QPushButton(self.centralwidget)
        self.R1_but.setGeometry(QtCore.QRect(160, 160, 121, 51))
        self.R1_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.R1_but.setObjectName("R1_but")
        self.R2_but = QtWidgets.QPushButton(self.centralwidget)
        self.R2_but.setGeometry(QtCore.QRect(160, 250, 121, 51))
        self.R2_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.R2_but.setObjectName("R2_but")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 40, 71, 20))
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        Routeur.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Routeur)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 21))
        self.menubar.setObjectName("menubar")
        Routeur.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Routeur)
        self.statusbar.setObjectName("statusbar")
        Routeur.setStatusBar(self.statusbar)

        self.retranslateUi(Routeur)
        QtCore.QMetaObject.connectSlotsByName(Routeur)

    def retranslateUi(self, Routeur):
        _translate = QtCore.QCoreApplication.translate
        Routeur.setWindowTitle(_translate("Routeur", "Router"))
        self.label.setText(_translate("Routeur", "Choisissez le routeur"))
        self.label_4.setText(_translate("Routeur", "Designed By Youssef SASSi"))
        self.ME_but.setText(_translate("Routeur", "READ ME"))
        self.R1_but.setText(_translate("Routeur", "Routeur 1"))
        self.R2_but.setText(_translate("Routeur", "Routeur 2"))
        self.label_3.setText(_translate("Routeur", "Important"))
   
   #donner les action aux bouttons    
        self.R1_but.clicked.connect(self.consfunc)
        self.R2_but.clicked.connect(self.consfunc2)
        self.ME_but.clicked.connect(self.RM1)
    # afficher la fenetre  config     
    def consfunc(self):
        
        MainWindow4 = QtWidgets.QMainWindow() 
        conf = config.Ui_MainWindow()
        conf.setupUi(MainWindow4)
        MainWindow4.show()
        Routeur.hide()
     # afficher la fenetre  config2       
    def consfunc2(self):
        
        MainWindow41 = QtWidgets.QMainWindow() 
        conf = config2.Ui_MainWindow()
        conf.setupUi(MainWindow41)
        MainWindow41.show()
        Routeur.hide()
     # afficher la fenetre  de READ ME    
    def RM1(self):
        
        MainWindow5 = QtWidgets.QMainWindow() 
        conf = ReadME.Ui_RM()
        conf.setupUi(MainWindow5)
        MainWindow5.show()
        Routeur.hide()
    # Connexion sur les routeurs ( les virtuelles machine ) Routeur 1  
    def id_R1(self):
        hostname="192.168.1.39"
        username="etudiant"
        password="vitrygtr"
        port=22
       
        
        return hostname , port , username ,password

    # Connexion sur les routeurs ( les virtuelles machine )   Routeur 2 
    def id_R2(self):
        hostname="192.168.1.40"
        username="etudiant"
        password="vitrygtr"
        port=22
        
        return hostname , port , username ,password
    
        
    

        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Routeur = QtWidgets.QMainWindow()
    ui = Ui_Routeur()
    ui.setupUi(Routeur)
    Routeur.show()
    sys.exit(app.exec_())
    
    
    

