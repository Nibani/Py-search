# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '123.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-100, -30, 1441, 860))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Фон.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 30, 671, 741))
        self.label_2.setStyleSheet("background-color: rgb(34,34,34);\n"
"border-radius: 20;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 40, 101, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Users/USER/Downloads/DE9hh_WYz9ro5Pn3O6WoN5Wk4yeHHq97rv6K0_TYxqa6dOmTPaco9OXIrgPOeiCu8G3CUgR_YSgy8ZWZQsXNNnwU__1_-removebg-preview.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 60, 611, 81))
        self.label_4.setStyleSheet("background-color: rgb(16, 16, 16);\n"
"border-radius: 13\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 290, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(78,78,78);\n"
"border: 10px;\n"
"color: rgb(94, 94, 94);\n"
"")
        self.lineEdit.setCursorPosition(7)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 380, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(78,78,78);\n"
"border: 0px;\n"
"color: rgb(94, 94, 94);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 620, 531, 71))
        font = QtGui.QFont()
        font.setFamily("Intro Demo Black CAPS")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(194, 103, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(420, 490, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(144, 144, 144);\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 230, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Intro Demo Black CAPS")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 460, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(34,34,34);\n"
"color: rgb(144, 144, 144);\n"
"border: 0px\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(830, 460, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(34,34,34);\n"
"color: rgb(144, 144, 144);\n"
"border: 0px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(830, 480, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(94, 94, 94);")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.checkBox.raise_()
        self.label_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit.setText(_translate("MainWindow", "  Логин"))
        self.lineEdit_2.setText(_translate("MainWindow", "  Пароль"))
        self.pushButton.setText(_translate("MainWindow", "Войти прямо сейчас"))
        self.checkBox.setText(_translate("MainWindow", "Запомнить меня"))
        self.label_5.setText(_translate("MainWindow", "ВОЙТИ С ПОМОЩЬЮ УЧЁТНОЙ ЗАПИСИ LYNX:"))
        self.pushButton_2.setText(_translate("MainWindow", "Забыли пароль"))
        self.pushButton_3.setText(_translate("MainWindow", "Зарегестрироваться"))
        self.label_6.setText(_translate("MainWindow", "или войти с помощью"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

