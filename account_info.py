# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AccountInfoDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 289)
        MainWindow.setStyleSheet("background-color: #19072c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 301, 41))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(87)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFC200;\n"
                                "font-weight: 700;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 301, 41))
        self.label_2.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFC200;\n"
                                    "font-weight: 700;\n"
                                    "border-right: 1px solid #FFC200;\n"
                                    "border-left: 1px solid #FFC200;\n"
                                    "padding-left: 2px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 301, 41))
        self.label_3.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #FFC200;\n"
                                    "font-weight: 700;\n"
                                    "border-top: 1px solid #FFC200;\n"
                                    "border-left: 1px solid #FFC200;\n"
                                    "border-right: 1px solid #FFC200;\n"
                                    "padding-left: 2px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 301, 41))
        self.label_4.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FFC200;\n"
                                    "font-weight: 700;\n"
                                    "border-right: 1px solid #FFC200;\n"
                                    "border-left: 1px solid #FFC200;\n"
                                    "padding-left: 2px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 190, 301, 41))
        self.label_5.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #FFC200;\n"
                                    "font-weight: 700;\n"
                                    "border-right: 1px solid #FFC200;\n"
                                    "border-left: 1px solid #FFC200;\n"
                                    "border-bottom: 1px solid #FFC200;\n"
                                    "padding-left: 2px;\n"
                                    "")
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: #19072c;\n"
                                        "color: #FFC200;\n"
                                        "font-weight: 700;\n"
                                        "border: 0;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 200, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border: 0;\n"
                                        "background-color: #19072c;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: #19072c;\n"
                                        "color: #FFC200;\n"
                                        "font-weight: 700;\n"
                                        "border: 1px solid #FFC200;\n"
                                        "border-radius: 2px;\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
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
        self.label.setText(_translate("MainWindow", "Информация об аккаунте"))
        self.label_2.setText(_translate("MainWindow", "Баланс: "))
        self.label_3.setText(_translate("MainWindow", "Тип аккаунта: "))
        self.label_4.setText(_translate("MainWindow", "Логин:"))
        self.label_5.setText(_translate("MainWindow", "Пароль:"))
        self.pushButton_6.setText(_translate("MainWindow", "◀"))
        self.pushButton_7.setText(_translate("MainWindow", "👁️"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
