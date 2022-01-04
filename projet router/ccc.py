# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import command
import router
import show
rout="ip a"


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 427)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"border-top-color: rgb(116, 188, 255);")
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
        self.label_3.setGeometry(QtCore.QRect(30, 170, 111, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 111, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_4.setObjectName("label_4")
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
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 330, 101, 41))
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.pushButton_5.setObjectName("pushButton_5")
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
        self.label_5.setGeometry(QtCore.QRect(620, 370, 141, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Script MT Bold\";")
        self.label_5.setObjectName("label_5")
        self.exit_but = QtWidgets.QPushButton(self.centralwidget)
        self.exit_but.setGeometry(QtCore.QRect(650, 320, 81, 51))
        self.exit_but.setStyleSheet("color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 170, 255);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.exit_but.setObjectName("exit_but")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 10, 61, 61))
        self.label_6.setStyleSheet("background-image: url(:/testt/UPEC - Logo - Noir - 200x200.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/testt/UPEC - Logo - Noir - 200x200.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 80, 121, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 10pt;")
        self.label_7.setObjectName("label_7")
        self.pass_line = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_line.setGeometry(QtCore.QRect(150, 80, 141, 20))
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
"font-size:10pt;\n"
"background-color: rgb(167, 168, 167);")
        self.save_but.setObjectName("save_but")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 300, 331, 61))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size: 50pt;")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
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
        self.label_4.setText(_translate("MainWindow", "Click me :)"))
        self.change1_but.setText(_translate("MainWindow", "Changer"))
        self.up_but.setText(_translate("MainWindow", "Activer"))
        self.down_but.setText(_translate("MainWindow", "Desactiver"))
        self.add_but.setText(_translate("MainWindow", "Ajouter"))
        self.pushButton_5.setText(_translate("MainWindow", "Suivant"))
        self.del_but.setText(_translate("MainWindow", "Supprimer"))
        self.label_5.setText(_translate("MainWindow", "Designed By Youssef SASSi"))
        self.exit_but.setText(_translate("MainWindow", "Exit"))
        self.label_7.setText(_translate("MainWindow", "Passerelle par defaut"))
        self.change2_but.setText(_translate("MainWindow", "Ajouter"))
        self.save_but.setText(_translate("MainWindow", "Save"))
        self.label_8.setText(_translate("MainWindow", "Routeur 1"))
        self.menudddddd.setTitle(_translate("MainWindow", "File"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionImport.setText(_translate("MainWindow", "Import"))

 # ajouter des action sur les bouttons 
        self.save_but.clicked.connect(self.save)
        self.exit_but.clicked.connect(self.exit)
        self.change1_but.clicked.connect(self.hn)
        self.change2_but.clicked.connect(self.aff_Routage)
        self.add_but.clicked.connect(self.confR1)
        self.del_but.clicked.connect(self.dellip1)
        self.down_but.clicked.connect(self.shut1)
        self.up_but.clicked.connect(self.up1)
        self.pushButton_5.clicked.connect(self.show1)
        
        
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
    def passrelle1(self):
        a2 = self.pass_line.text()
        router1 = router.Ui_Routeur()
        hostname, port , username,password = router1.id_R1()  # connecter sur le VM et apres apelle la fonction pour l'executer 
        command.Adress_Defaut(a2,hostname,port , username,password)
    
    def show1(self):
        
        MainWindow6 = QtWidgets.QMainWindow() 
        sh = show.Ui_MainWindow()
        sh.setupUi(MainWindow6)
        MainWindow6.show()
        MainWindow.hide()
    
    def aff_Routage(self):
        self.pass_line.setText(command.afficherRoutage1(rout))
        print(command.afficherRoutage1(rout))
        
        
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
        
       with open('data1.txt', 'w') as f:    
           # des variables pour ajouter les getter de tous les edit text 
           a1 = self.nom_line.text()     
           a2 = self.pass_line.text()
           a3 = self.ip_line.text()
           a4 = self.inter_line.text()
           
           f.write("le nom de routeur : "+ a1+ "\n" + " le passerelle par defaut : " + a2 + " \n " + " @ IP / Masque : " + a3 + " \n" + " l'interface  : "+a4)
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

