# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReadME.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RM(object):
    def setupUi(self, RM):
        RM.setObjectName("RM")
        RM.resize(594, 346)
        RM.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(RM)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 571, 241))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 270, 75, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font-size:15pt;")
        self.pushButton.setObjectName("pushButton")
        RM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        RM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RM)
        self.statusbar.setObjectName("statusbar")
        RM.setStatusBar(self.statusbar)

        self.retranslateUi(RM)
        QtCore.QMetaObject.connectSlotsByName(RM)

    def retranslateUi(self, RM):
        _translate = QtCore.QCoreApplication.translate
        RM.setWindowTitle(_translate("RM", "HELP"))
        self.textEdit.setHtml(_translate("RM","."))
        self.pushButton.setText(_translate("RM", "EXIT"))

        self.pushButton.clicked.connect(self.exitt)
    def exitt(self):
        RM.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RM = QtWidgets.QMainWindow()
    ui = Ui_RM()
    ui.setupUi(RM)
    RM.show()
    sys.exit(app.exec_())

