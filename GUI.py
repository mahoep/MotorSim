# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MotorSim(object):
    def setupUi(self, MotorSim):
        MotorSim.setObjectName("MotorSim")
        MotorSim.resize(707, 545)
        self.centralwidget = QtWidgets.QWidget(MotorSim)
        self.centralwidget.setObjectName("centralwidget")
        self.grainNum = QtWidgets.QLabel(self.centralwidget)
        self.grainNum.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.grainNum.setObjectName("grainNum")
        self.grainType = QtWidgets.QLabel(self.centralwidget)
        self.grainType.setGeometry(QtCore.QRect(60, 20, 51, 21))
        self.grainType.setObjectName("grainType")
        self.grainDiam = QtWidgets.QLabel(self.centralwidget)
        self.grainDiam.setGeometry(QtCore.QRect(240, 20, 81, 21))
        self.grainDiam.setObjectName("grainDiam")
        self.grainLeng = QtWidgets.QLabel(self.centralwidget)
        self.grainLeng.setGeometry(QtCore.QRect(330, 20, 61, 21))
        self.grainLeng.setObjectName("grainLeng")
        self.CoreDiam = QtWidgets.QLabel(self.centralwidget)
        self.CoreDiam.setGeometry(QtCore.QRect(410, 20, 81, 21))
        self.CoreDiam.setObjectName("CoreDiam")
        self.runSim = QtWidgets.QPushButton(self.centralwidget)
        self.runSim.setGeometry(QtCore.QRect(10, 200, 91, 23))
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
        self.grainDiam1.setGeometry(QtCore.QRect(240, 40, 51, 20))
        self.grainDiam1.setObjectName("grainDiam1")
        self.grainDiam2 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam2.setGeometry(QtCore.QRect(240, 70, 51, 20))
        self.grainDiam2.setObjectName("grainDiam2")
        self.grainDiam3 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam3.setGeometry(QtCore.QRect(240, 100, 51, 20))
        self.grainDiam3.setObjectName("grainDiam3")
        self.grainDiam4 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam4.setGeometry(QtCore.QRect(240, 130, 51, 20))
        self.grainDiam4.setObjectName("grainDiam4")
        self.grainDiam5 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainDiam5.setGeometry(QtCore.QRect(240, 160, 51, 20))
        self.grainDiam5.setObjectName("grainDiam5")
        self.grainLeng1 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng1.setGeometry(QtCore.QRect(330, 40, 51, 20))
        self.grainLeng1.setObjectName("grainLeng1")
        self.grainLeng2 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng2.setGeometry(QtCore.QRect(330, 70, 51, 20))
        self.grainLeng2.setObjectName("grainLeng2")
        self.grainLeng3 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng3.setGeometry(QtCore.QRect(330, 100, 51, 20))
        self.grainLeng3.setObjectName("grainLeng3")
        self.grainLeng4 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng4.setGeometry(QtCore.QRect(330, 130, 51, 20))
        self.grainLeng4.setObjectName("grainLeng4")
        self.grainLeng5 = QtWidgets.QLineEdit(self.centralwidget)
        self.grainLeng5.setGeometry(QtCore.QRect(330, 160, 51, 20))
        self.grainLeng5.setObjectName("grainLeng5")
        self.coreDiam1 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam1.setGeometry(QtCore.QRect(410, 40, 51, 20))
        self.coreDiam1.setObjectName("coreDiam1")
        self.coreDiam2 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam2.setGeometry(QtCore.QRect(410, 70, 51, 20))
        self.coreDiam2.setObjectName("coreDiam2")
        self.coreDiam3 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam3.setGeometry(QtCore.QRect(410, 100, 51, 20))
        self.coreDiam3.setObjectName("coreDiam3")
        self.coreDiam4 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam4.setGeometry(QtCore.QRect(410, 130, 51, 20))
        self.coreDiam4.setObjectName("coreDiam4")
        self.coreDiam5 = QtWidgets.QLineEdit(self.centralwidget)
        self.coreDiam5.setGeometry(QtCore.QRect(410, 160, 51, 20))
        self.coreDiam5.setObjectName("coreDiam5")
        self.grainType2 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType2.setGeometry(QtCore.QRect(60, 70, 69, 22))
        self.grainType2.setToolTipDuration(5)
        self.grainType2.setCurrentText("")
        self.grainType2.setObjectName("grainType2")
        self.grainType2.addItem("")
        self.grainType2.setItemText(0, "")
        self.grainType2.addItem("")
        self.grainType2.addItem("")
        self.grainType2.addItem("")
        self.grainType3 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType3.setGeometry(QtCore.QRect(60, 100, 69, 22))
        self.grainType3.setToolTipDuration(5)
        self.grainType3.setCurrentText("")
        self.grainType3.setObjectName("grainType3")
        self.grainType3.addItem("")
        self.grainType3.setItemText(0, "")
        self.grainType3.addItem("")
        self.grainType3.addItem("")
        self.grainType3.addItem("")
        self.grainType4 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType4.setGeometry(QtCore.QRect(60, 130, 69, 22))
        self.grainType4.setToolTipDuration(5)
        self.grainType4.setCurrentText("")
        self.grainType4.setObjectName("grainType4")
        self.grainType4.addItem("")
        self.grainType4.setItemText(0, "")
        self.grainType4.addItem("")
        self.grainType4.addItem("")
        self.grainType4.addItem("")
        self.grainType5 = QtWidgets.QComboBox(self.centralwidget)
        self.grainType5.setGeometry(QtCore.QRect(60, 160, 69, 22))
        self.grainType5.setToolTipDuration(5)
        self.grainType5.setCurrentText("")
        self.grainType5.setObjectName("grainType5")
        self.grainType5.addItem("")
        self.grainType5.setItemText(0, "")
        self.grainType5.addItem("")
        self.grainType5.addItem("")
        self.grainType5.addItem("")
        self.Propellant = QtWidgets.QLabel(self.centralwidget)
        self.Propellant.setGeometry(QtCore.QRect(150, 20, 61, 21))
        self.Propellant.setObjectName("Propellant")
        self.propellant1 = QtWidgets.QComboBox(self.centralwidget)
        self.propellant1.setGeometry(QtCore.QRect(150, 40, 69, 22))
        self.propellant1.setToolTipDuration(5)
        self.propellant1.setCurrentText("")
        self.propellant1.setObjectName("propellant1")
        self.propellant1.addItem("")
        self.propellant1.setItemText(0, "")
        self.propellant1.addItem("")
        self.propellant1.addItem("")
        self.propellant1.addItem("")
        self.propellant2 = QtWidgets.QComboBox(self.centralwidget)
        self.propellant2.setGeometry(QtCore.QRect(150, 70, 69, 22))
        self.propellant2.setToolTipDuration(5)
        self.propellant2.setCurrentText("")
        self.propellant2.setObjectName("propellant2")
        self.propellant2.addItem("")
        self.propellant2.setItemText(0, "")
        self.propellant2.addItem("")
        self.propellant2.addItem("")
        self.propellant2.addItem("")
        self.propellant3 = QtWidgets.QComboBox(self.centralwidget)
        self.propellant3.setGeometry(QtCore.QRect(150, 100, 69, 22))
        self.propellant3.setToolTipDuration(5)
        self.propellant3.setCurrentText("")
        self.propellant3.setObjectName("propellant3")
        self.propellant3.addItem("")
        self.propellant3.setItemText(0, "")
        self.propellant3.addItem("")
        self.propellant3.addItem("")
        self.propellant3.addItem("")
        self.propellant4 = QtWidgets.QComboBox(self.centralwidget)
        self.propellant4.setGeometry(QtCore.QRect(150, 130, 69, 22))
        self.propellant4.setToolTipDuration(5)
        self.propellant4.setCurrentText("")
        self.propellant4.setObjectName("propellant4")
        self.propellant4.addItem("")
        self.propellant4.setItemText(0, "")
        self.propellant4.addItem("")
        self.propellant4.addItem("")
        self.propellant4.addItem("")
        self.propellant5 = QtWidgets.QComboBox(self.centralwidget)
        self.propellant5.setGeometry(QtCore.QRect(150, 160, 69, 22))
        self.propellant5.setToolTipDuration(5)
        self.propellant5.setCurrentText("")
        self.propellant5.setObjectName("propellant5")
        self.propellant5.addItem("")
        self.propellant5.setItemText(0, "")
        self.propellant5.addItem("")
        self.propellant5.addItem("")
        self.propellant5.addItem("")
        #MotorSim.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MotorSim)
        self.statusbar.setObjectName("statusbar")
        #MotorSim.setStatusBar(self.statusbar)

        self.retranslateUi(MotorSim)
        QtCore.QMetaObject.connectSlotsByName(MotorSim)

    def retranslateUi(self, MotorSim):
        _translate = QtCore.QCoreApplication.translate
        MotorSim.setWindowTitle(_translate("MotorSim", "MotorSim v0.01"))
        self.grainNum.setText(_translate("MotorSim", "Grain #"))
        self.grainType.setText(_translate("MotorSim", "Grain Type"))
        self.grainDiam.setText(_translate("MotorSim", "Grain Diameter"))
        self.grainLeng.setText(_translate("MotorSim", "Grain Length"))
        self.CoreDiam.setText(_translate("MotorSim", "Core Diameter"))
        self.runSim.setText(_translate("MotorSim", "Run Simulation"))
        self.grainType1.setItemText(1, _translate("MotorSim", "BATES"))
        self.grainType1.setItemText(2, _translate("MotorSim", "STAR"))
        self.grainType1.setItemText(3, _translate("MotorSim", "SQUARE"))
        self.grainType2.setItemText(1, _translate("MotorSim", "BATES"))
        self.grainType2.setItemText(2, _translate("MotorSim", "STAR"))
        self.grainType2.setItemText(3, _translate("MotorSim", "SQUARE"))
        self.grainType3.setItemText(1, _translate("MotorSim", "BATES"))
        self.grainType3.setItemText(2, _translate("MotorSim", "STAR"))
        self.grainType3.setItemText(3, _translate("MotorSim", "SQUARE"))
        self.grainType4.setItemText(1, _translate("MotorSim", "BATES"))
        self.grainType4.setItemText(2, _translate("MotorSim", "STAR"))
        self.grainType4.setItemText(3, _translate("MotorSim", "SQUARE"))
        self.grainType5.setItemText(1, _translate("MotorSim", "BATES"))
        self.grainType5.setItemText(2, _translate("MotorSim", "STAR"))
        self.grainType5.setItemText(3, _translate("MotorSim", "SQUARE"))
        self.Propellant.setText(_translate("MotorSim", "Propellant"))
        self.propellant1.setItemText(1, _translate("MotorSim", "OK"))
        self.propellant1.setItemText(2, _translate("MotorSim", "RIO"))
        self.propellant1.setItemText(3, _translate("MotorSim", "SOS"))
        self.propellant2.setItemText(1, _translate("MotorSim", "OK"))
        self.propellant2.setItemText(2, _translate("MotorSim", "RIO"))
        self.propellant2.setItemText(3, _translate("MotorSim", "SOS"))
        self.propellant3.setItemText(1, _translate("MotorSim", "OK"))
        self.propellant3.setItemText(2, _translate("MotorSim", "RIO"))
        self.propellant3.setItemText(3, _translate("MotorSim", "SOS"))
        self.propellant4.setItemText(1, _translate("MotorSim", "OK"))
        self.propellant4.setItemText(2, _translate("MotorSim", "RIO"))
        self.propellant4.setItemText(3, _translate("MotorSim", "SOS"))
        self.propellant5.setItemText(1, _translate("MotorSim", "OK"))
        self.propellant5.setItemText(2, _translate("MotorSim", "RIO"))
        self.propellant5.setItemText(3, _translate("MotorSim", "SOS"))

