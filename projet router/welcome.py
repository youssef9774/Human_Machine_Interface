# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import router
import pingg

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.label_4.setGeometry(QtCore.QRect(260, 260, 151, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Script MT Bold\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 131, 41))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.pushButton.setObjectName("pushButton")
        self.ping2 = QtWidgets.QPushButton(self.centralwidget)
        self.ping2.setGeometry(QtCore.QRect(330, 20, 61, 31))
        self.ping2.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:12pt;\n"
"background-color: rgb(255, 0, 0);")
        self.ping2.setObjectName("ping2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 61, 23))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:12pt;\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.pushButton.setText(_translate("MainWindow", "Démarrer"))
        self.ping2.setText(_translate("MainWindow", "Ping"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))

        self.pushButton.clicked.connect(self.routerfunction)
        self.ping2.clicked.connect(self.ping_me)
        self.pushButton_3.clicked.connect(self.exit)
    #configuration de la fenetre routeur    
    def routerfunction(self):
        MainWindow3 = QtWidgets.QMainWindow() 
        rout = router.Ui_Routeur()
        rout.setupUi(MainWindow3)
        MainWindow3.show()
        MainWindow.hide()
    
    def ping_me(self):
        pg = QtWidgets.QMainWindow() 
        pg1 = pingg.Ui_MainWindow()
        pg1.setupUi(pg)
        pg.show()
        MainWindow.hide()
        
        
    def exit(self):
        MainWindow.close()
        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

