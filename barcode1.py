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
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.yesLabel.setFont(font)
        self.yesLabel.setObjectName("yesLabel")
        self.verticalLayout.addWidget(self.yesLabel)
        self.noLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.noLabel.setFont(font)
        self.noLabel.setAutoFillBackground(False)
        self.noLabel.setObjectName("noLabel")
        self.verticalLayout.addWidget(self.noLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(379, 9, 401, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Синхронизировать"))
