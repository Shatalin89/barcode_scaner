# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barcode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.sityLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sityLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sityLabel.setObjectName("sityLabel")
        self.verticalLayout.addWidget(self.sityLabel)
        self.comboBoxSity = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxSity.setObjectName("comboBoxSity")
        self.verticalLayout.addWidget(self.comboBoxSity)
        self.eventLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.eventLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.eventLabel.setObjectName("eventLabel")
        self.verticalLayout.addWidget(self.eventLabel)
        self.comboBoxEvent = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxEvent.setObjectName("comboBoxEvent")
        self.verticalLayout.addWidget(self.comboBoxEvent)
        self.yesLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.yesLabel.setObjectName("yesLabel")
        self.verticalLayout.addWidget(self.yesLabel)
        self.noLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.noLabel.setObjectName("noLabel")
        self.verticalLayout.addWidget(self.noLabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.sityLabel.setText(_translate("MainWindow", "Город"))
        self.eventLabel.setText(_translate("MainWindow", "Мероприятие"))
        self.yesLabel.setText(_translate("MainWindow", "TextLabel"))
        self.noLabel.setText(_translate("MainWindow", "TextLabel"))

