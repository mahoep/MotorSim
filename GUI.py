# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MotorSim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 545)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 20, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 20, 81, 21))
        self.label_5.setObjectName("label_5")
        self.runSim = QtWidgets.QPushButton(self.centralwidget)
        self.runSim.setGeometry(QtCore.QRect(90, 400, 91, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.runSim.setFont(font)
        self.runSim.setObjectName("runSim")
        self.grainNumber1 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainNumber1.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.grainNumber1.setObjectName("grainNumber1")
        self.grainNumber2 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainNumber2.setGeometry(QtCore.QRect(10, 70, 31, 20))
        self.grainNumber2.setObjectName("grainNumber2")
        self.grainNumber3 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainNumber3.setGeometry(QtCore.QRect(10, 100, 31, 20))
        self.grainNumber3.setObjectName("grainNumber3")
        self.grainNumber4 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainNumber4.setGeometry(QtCore.QRect(10, 130, 31, 20))
        self.grainNumber4.setObjectName("grainNumber4")
        self.grainNumber5 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainNumber5.setGeometry(QtCore.QRect(10, 160, 31, 20))
        self.grainNumber5.setObjectName("grainNumber5")
        self.grainType1 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType1.setGeometry(QtCore.QRect(60, 40, 69, 22))
        self.grainType1.setToolTipDuration(5)
        self.grainType1.setCurrentText("")
        self.grainType1.setObjectName("grainType1")
        self.grainType1.addItem("")
        self.grainType1.setItemText(0, "")
        self.grainType1.addItem("")
        self.grainType1.addItem("")
        self.grainType1.addItem("")
        self.grainDiam1 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam1.setGeometry(QtCore.QRect(150, 40, 51, 20))
        self.grainDiam1.setObjectName("grainDiam1")
        self.grainDiam2 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam2.setGeometry(QtCore.QRect(150, 70, 51, 20))
        self.grainDiam2.setObjectName("grainDiam2")
        self.grainDiam3 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam3.setGeometry(QtCore.QRect(150, 100, 51, 20))
        self.grainDiam3.setObjectName("grainDiam3")
        self.grainDiam4 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam4.setGeometry(QtCore.QRect(150, 130, 51, 20))
        self.grainDiam4.setObjectName("grainDiam4")
        self.grainDiam5 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam5.setGeometry(QtCore.QRect(150, 160, 51, 20))
        self.grainDiam5.setObjectName("grainDiam5")
        self.grainLeng1 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng1.setGeometry(QtCore.QRect(240, 40, 51, 20))
        self.grainLeng1.setObjectName("grainLeng1")
        self.grainLeng2 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng2.setGeometry(QtCore.QRect(240, 70, 51, 20))
        self.grainLeng2.setObjectName("grainLeng2")
        self.grainLeng3 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng3.setGeometry(QtCore.QRect(240, 100, 51, 20))
        self.grainLeng3.setObjectName("grainLeng3")
        self.grainLeng4 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng4.setGeometry(QtCore.QRect(240, 130, 51, 20))
        self.grainLeng4.setObjectName("grainLeng4")
        self.grainLeng5 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng5.setGeometry(QtCore.QRect(240, 160, 51, 20))
        self.grainLeng5.setObjectName("grainLeng5")
        self.coreDiam1 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam1.setGeometry(QtCore.QRect(320, 40, 51, 20))
        self.coreDiam1.setObjectName("coreDiam1")
        self.coreDiam2 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam2.setGeometry(QtCore.QRect(320, 70, 51, 20))
        self.coreDiam2.setObjectName("coreDiam2")
        self.coreDiam3 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam3.setGeometry(QtCore.QRect(320, 100, 51, 20))
        self.coreDiam3.setObjectName("coreDiam3")
        self.coreDiam4 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam4.setGeometry(QtCore.QRect(320, 130, 51, 20))
        self.coreDiam4.setObjectName("coreDiam4")
        self.coreDiam5 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam5.setGeometry(QtCore.QRect(320, 160, 51, 20))
        self.coreDiam5.setObjectName("coreDiam5")
        self.grainType1_2 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType1_2.setGeometry(QtCore.QRect(60, 70, 69, 22))
        self.grainType1_2.setToolTipDuration(5)
        self.grainType1_2.setCurrentText("")
        self.grainType1_2.setObjectName("grainType1_2")
        self.grainType1_2.addItem("")
        self.grainType1_2.setItemText(0, "")
        self.grainType1_2.addItem("")
        self.grainType1_2.addItem("")
        self.grainType1_2.addItem("")
        self.grainType1_3 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType1_3.setGeometry(QtCore.QRect(60, 100, 69, 22))
        self.grainType1_3.setToolTipDuration(5)
        self.grainType1_3.setCurrentText("")
        self.grainType1_3.setObjectName("grainType1_3")
        self.grainType1_3.addItem("")
        self.grainType1_3.setItemText(0, "")
        self.grainType1_3.addItem("")
        self.grainType1_3.addItem("")
        self.grainType1_3.addItem("")
        self.grainType1_4 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType1_4.setGeometry(QtCore.QRect(60, 130, 69, 22))
        self.grainType1_4.setToolTipDuration(5)
        self.grainType1_4.setCurrentText("")
        self.grainType1_4.setObjectName("grainType1_4")
        self.grainType1_4.addItem("")
        self.grainType1_4.setItemText(0, "")
        self.grainType1_4.addItem("")
        self.grainType1_4.addItem("")
        self.grainType1_4.addItem("")
        self.grainType1_5 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType1_5.setGeometry(QtCore.QRect(60, 160, 69, 22))
        self.grainType1_5.setToolTipDuration(5)
        self.grainType1_5.setCurrentText("")
        self.grainType1_5.setObjectName("grainType1_5")
        self.grainType1_5.addItem("")
        self.grainType1_5.setItemText(0, "")
        self.grainType1_5.addItem("")
        self.grainType1_5.addItem("")
        self.grainType1_5.addItem("")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MotorSim v0.01"))
        self.label.setText(_translate("MainWindow", "Grain #"))
        self.label_2.setText(_translate("MainWindow", "Grain Type"))
        self.label_3.setText(_translate("MainWindow", "Grain Diameter"))
        self.label_4.setText(_translate("MainWindow", "Grain Length"))
        self.label_5.setText(_translate("MainWindow", "Core Diameter"))
        self.runSim.setText(_translate("MainWindow", "Run Simulation"))
        self.grainType1.setItemText(1, _translate("MainWindow", "BATES"))
        self.grainType1.setItemText(2, _translate("MainWindow", "STAR"))
        self.grainType1.setItemText(3, _translate("MainWindow", "SQUARE"))
        self.grainType1_2.setItemText(1, _translate("MainWindow", "BATES"))
        self.grainType1_2.setItemText(2, _translate("MainWindow", "STAR"))
        self.grainType1_2.setItemText(3, _translate("MainWindow", "SQUARE"))
        self.grainType1_3.setItemText(1, _translate("MainWindow", "BATES"))
        self.grainType1_3.setItemText(2, _translate("MainWindow", "STAR"))
        self.grainType1_3.setItemText(3, _translate("MainWindow", "SQUARE"))
        self.grainType1_4.setItemText(1, _translate("MainWindow", "BATES"))
        self.grainType1_4.setItemText(2, _translate("MainWindow", "STAR"))
        self.grainType1_4.setItemText(3, _translate("MainWindow", "SQUARE"))
        self.grainType1_5.setItemText(1, _translate("MainWindow", "BATES"))
        self.grainType1_5.setItemText(2, _translate("MainWindow", "STAR"))
        self.grainType1_5.setItemText(3, _translate("MainWindow", "SQUARE"))

