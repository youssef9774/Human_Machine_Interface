# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import command
import router
import mod
rout="ip route"
Inter_R="ip a"
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 429)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 121, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 61, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_3.setObjectName("label_3")
        self.nom_line = QtWidgets.QLineEdit(self.centralwidget)
        self.nom_line.setGeometry(QtCore.QRect(150, 30, 141, 20))
        self.nom_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.nom_line.setObjectName("nom_line")
        self.inter_line = QtWidgets.QLineEdit(self.centralwidget)
        self.inter_line.setGeometry(QtCore.QRect(150, 170, 141, 20))
        self.inter_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.inter_line.setObjectName("inter_line")
        self.ip_line = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_line.setGeometry(QtCore.QRect(150, 120, 141, 20))
        self.ip_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.ip_line.setObjectName("ip_line")
        self.change1_but = QtWidgets.QPushButton(self.centralwidget)
        self.change1_but.setGeometry(QtCore.QRect(420, 20, 111, 31))
        self.change1_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.change1_but.setObjectName("change1_but")
        self.up_but = QtWidgets.QPushButton(self.centralwidget)
        self.up_but.setGeometry(QtCore.QRect(340, 170, 121, 31))
        self.up_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.up_but.setObjectName("up_but")
        self.down_but = QtWidgets.QPushButton(self.centralwidget)
        self.down_but.setGeometry(QtCore.QRect(490, 170, 121, 31))
        self.down_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.down_but.setObjectName("down_but")
        self.add_but = QtWidgets.QPushButton(self.centralwidget)
        self.add_but.setGeometry(QtCore.QRect(340, 110, 121, 31))
        self.add_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.add_but.setObjectName("add_but")
        self.afficher_TR = QtWidgets.QPushButton(self.centralwidget)
        self.afficher_TR.setGeometry(QtCore.QRect(170, 270, 101, 41))
        self.afficher_TR.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.afficher_TR.setObjectName("afficher_TR")
        self.del_but = QtWidgets.QPushButton(self.centralwidget)
        self.del_but.setGeometry(QtCore.QRect(490, 110, 121, 31))
        self.del_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.del_but.setObjectName("del_but")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(850, 370, 141, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Script MT Bold\";")
        self.label_5.setObjectName("label_5")
        self.exit_but = QtWidgets.QPushButton(self.centralwidget)
        self.exit_but.setGeometry(QtCore.QRect(870, 320, 81, 51))
        self.exit_but.setStyleSheet("color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 170, 255);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.exit_but.setObjectName("exit_but")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_7.setObjectName("label_7")
        self.pass_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_line.setGeometry(QtCore.QRect(150, 80, 141, 20))
        self.pass_line.setStyleSheet("color: rgb(255, 255, 255);")
        self.pass_line.setObjectName("pass_line")
        self.change2_but = QtWidgets.QPushButton(self.centralwidget)
        self.change2_but.setGeometry(QtCore.QRect(420, 70, 111, 31))
        self.change2_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.change2_but.setObjectName("change2_but")
        self.save_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_but.setGeometry(QtCore.QRect(180, 210, 75, 23))
        self.save_but.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:12pt;\n"
"background-color: rgb(255, 0, 0);")
        self.save_but.setObjectName("save_but")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 320, 301, 61))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 50pt;")
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 370, 141, 20))
        self.label_4.setStyleSheet("color: rgb(239, 255, 89);\n"
"\n"
"font: 13pt \"MV Boli\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 310, 131, 16))
        self.label_6.setStyleSheet("color: rgb(239, 255, 89);\n"
"\n"
"font: 12pt \"MV Boli\";")
        self.label_6.setObjectName("label_6")
        self.afficher_IR = QtWidgets.QPushButton(self.centralwidget)
        self.afficher_IR.setGeometry(QtCore.QRect(740, 340, 81, 31))
        self.afficher_IR.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.afficher_IR.setObjectName("afficher_IR")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 210, 291, 151))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(630, 0, 351, 301))
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 280, 101, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_9.setObjectName("label_9")
        self.l1 = QtWidgets.QPushButton(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(190, 240, 51, 21))
        self.l1.setStyleSheet("\n"
"background-color: rgb(85, 170, 255);\n"
"font: 10pt \"Segoe Print\";\n"
"color: rgb(36, 29, 29);")
        self.l1.setObjectName("l1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
        self.menubar.setObjectName("menubar")
        self.menudddddd = QtWidgets.QMenu(self.menubar)
        self.menudddddd.setObjectName("menudddddd")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.menudddddd.addAction(self.actionSave)
        self.menudddddd.addAction(self.actionImport)
        self.menubar.addAction(self.menudddddd.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuration"))
        self.label.setText(_translate("MainWindow", "Nom Routeur"))
        self.label_2.setText(_translate("MainWindow", "Adresse IP / Masque "))
        self.label_3.setText(_translate("MainWindow", "Interface"))
        self.change1_but.setText(_translate("MainWindow", "Changer"))
        self.up_but.setText(_translate("MainWindow", "Activer"))
        self.down_but.setText(_translate("MainWindow", "Desactiver"))
        self.add_but.setText(_translate("MainWindow", "Ajouter"))
        self.afficher_TR.setText(_translate("MainWindow", "Afficher"))
        self.del_but.setText(_translate("MainWindow", "Supprimer"))
        self.label_5.setText(_translate("MainWindow", "Designed By Youssef SASSi"))
        self.exit_but.setText(_translate("MainWindow", "Exit"))
        self.label_7.setText(_translate("MainWindow", "Passerelle par defaut"))
        self.change2_but.setText(_translate("MainWindow", "Ajouter"))
        self.save_but.setText(_translate("MainWindow", "Save"))
        self.label_8.setText(_translate("MainWindow", "Routeur 1"))
        self.label_4.setText(_translate("MainWindow", "Table de Routage"))
        self.label_6.setText(_translate("MainWindow", "Interface réseau"))
        self.afficher_IR.setText(_translate("MainWindow", "Afficher"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Table de Routage"))
        self.l1.setText(_translate("MainWindow", "Lire "))
        self.menudddddd.setTitle(_translate("MainWindow", "File"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        
        # ajouter des action sur les bouttons 
        self.save_but.clicked.connect(self.save)
        self.exit_but.clicked.connect(self.exit)
        self.change1_but.clicked.connect(self.hn)
        self.change2_but.clicked.connect(self.default)
        
        self.add_but.clicked.connect(self.confR1)
        self.del_but.clicked.connect(self.dellip1)
        self.down_but.clicked.connect(self.shut1)
        self.up_but.clicked.connect(self.up1)
        self.afficher_TR.clicked.connect(self.aff_Routage)
        self.afficher_IR.clicked.connect(self.aff_Interface)
        self.l1.clicked.connect(self.show1)
        
        
 # Fonction callback pour appeler la commande de changement de nom du routeur
 
    def hn(self):
        a1 = self.nom_line.text()     
        router1 = router.Ui_Routeur()   # connecter sur le VM et apres apelle la fonction pour l'executer 
        hostname, port , username,password = router1.id_R1()
        
        command.hn1(a1,hostname,port , username,password)
 # Fonction callback pour appeler la commande de changement d'adresse ip et aussi le masque    
    def confR1(self):
        a3 = self.ip_line.text()
        a4 = self.inter_line.text()

        router1 = router.Ui_Routeur()
        hostname, port , username,password = router1.id_R1()   # connecter sur le VM et apres apelle la fonction pour l'executer 
        
        command.confR(a3,a4,hostname,port , username,password)
 
    # Fonction callback pour appeler la commande pour supprimer d'adresse ip et aussi le masque    
      
    def dellip1(self):
        a3 = self.ip_line.text()
        a4 = self.inter_line.text()

        router1 = router.Ui_Routeur()
        hostname, port , username,password = router1.id_R1()  # connecter sur le VM et apres apelle la fonction pour l'executer 
        
        command.dellip(a3,a4,hostname,port , username,password)
     # Fonction callback pour appeler la commande  (fonction) pour desactiver l'interface      
    def shut1(self):
        a4 = self.inter_line.text()
        router1 = router.Ui_Routeur()
        hostname, port , username,password = router1.id_R1()  # connecter sur le VM et apres apelle la fonction pour l'executer 
        
        command.shut(a4,hostname,port , username,password)
    # Fonction callback pour appeler la commande  (fonction) pour activer l'interface  
    def up1(self):
        a4 = self.inter_line.text()
        router1 = router.Ui_Routeur()
        hostname, port , username,password = router1.id_R1()  # connecter sur le VM et apres apelle la fonction pour l'executer 
        
        command.up(a4,hostname,port , username,password)
     # Fonction callback pour appeler la commande  (fonction) pour ajouter une passrelle par defaut     
#    def passrelle1(self):
#        a2 = self.pass_line.text()
#        router1 = router.Ui_Routeur()
#        hostname, port , username,password = router1.id_R1()  # connecter sur le VM et apres apelle la fonction pour l'executer 
#        command.Defaut(a2,hostname,port , username,password)
    # Fonction callback pour appeler la commande  (fonction) pour ajouter une passrelle par defaut 
    def default(self):
        a2 = self.pass_line.text()
        router1 = router.Ui_Routeur()
        hostname, port , username,password = router1.id_R1() # connecter sur le VM et apres apelle la fonction pour l'executer

        command.add_default_R1(a2, hostname, port, username, password)
    

    # Fonction callback pour appeler la commande  (fonction) pour afficher table de routage
    def aff_Routage(self):
        self.textEdit.setText(command.afficherRoutage1(rout))
        print(command.afficherRoutage1(rout))
    # Fonction callback pour appeler la commande  (fonction) pour afficher les interfaces Reseaux 
    def aff_Interface(self):
        self.textEdit_2.setText(command.afficherInterface(Inter_R))
        print(command.afficherInterface(Inter_R))
        
        
#    def afficherRoutage(self):
#        self.inter_line.setText(command.afficherRoutage(rout))
#        print(command.afficherRoutage(rout))
        
#    def si(self):
#        
#        router1 = router.Ui_Routeur()
#        hostname, port , username,password = router1.id_R1()  # connecter sur le VM et apres apelle la fonction pour l'executer 
#        command.shw_ip(hostname,port , username,password)
        
    # Fonction callback pour sauvgarder les configuration par l'utilisateur      
    def save(self):
        
       with open('data1.txt', 'a') as f:    
           # des variables pour ajouter les getter de tous les edit text 
           a1 = self.nom_line.text()     
           a2 = self.pass_line.text()
           a3 = self.ip_line.text()
           a4 = self.inter_line.text()
           
           
           f.write("le nom de routeur : "+ a1+ "\n" + " le passerelle par defaut : " + a2 + " \n " + " @ IP / Masque : " + a3 + " \n" + " l'interface  : "+a4 +"\n" + "==================="+"\n")
  # Fonction pour acceder à la page de modification de l'utilisateur 
    def show1(self):
        
        MainWindow6 = QtWidgets.QMainWindow() 
        sh = mod.Ui_MainWindow()
        sh.setupUi(MainWindow6)
        MainWindow6.show()
        MainWindow.hide()
    # Fonction pour quitter le programme  
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

