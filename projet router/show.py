# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

rout="ip route"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 514)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 30, 101, 31))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 70, 181, 21))
        self.label.setStyleSheet("color: rgb(239, 255, 89);\n"
"\n"
"font: 16pt \"MV Boli\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 70, 181, 21))
        self.label_2.setStyleSheet("color: rgb(239, 255, 89);\n"
"\n"
"font: 16pt \"MV Boli\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 10, 81, 61))
        self.label_3.setStyleSheet("image: url(:/image upec/UPEC - Logo - Noir - 200x200.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 30, 91, 31))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 170, 255);\n"
"\n"
"font: 8pt \"Segoe Print\";\n"
"font-size:15pt;\n"
"background-color: rgb(167, 168, 167);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 460, 141, 16))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Script MT Bold\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 442, 81, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(234, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 100, 301, 331))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(320, 100, 401, 331))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show"))
        self.pushButton.setText(_translate("MainWindow", "Afficher"))
        self.label.setText(_translate("MainWindow", "Table de routage"))
        self.label_2.setText(_translate("MainWindow", "Interface réseau"))
        self.pushButton_2.setText(_translate("MainWindow", "Afficher"))
        self.label_5.setText(_translate("MainWindow", "Designed By Youssef SASSi"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
#        self.pushButton.clicked.connect(self.aff_Routage)
        
#    def aff_Routage(self):
#        self.plainTextEdit.setText(command.afficherRoutage1(rout))
#        print(command.afficherRoutage1(rout))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

