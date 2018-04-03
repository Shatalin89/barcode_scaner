# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barcode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BarcodeMain(object):
    def setupUi(self, BarcodeMain):
        BarcodeMain.setObjectName("BarcodeMain")
        BarcodeMain.resize(1119, 836)
        self.centralwidget = QtWidgets.QWidget(BarcodeMain)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(560, 10, 541, 401))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(560, 420, 539, 399))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.barcode_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.barcode_input.setEnabled(True)
        self.barcode_input.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.barcode_input.setFont(font)
        self.barcode_input.setObjectName("barcode_input")
        self.verticalLayout.addWidget(self.barcode_input)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 541, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 420, 551, 401))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        BarcodeMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(BarcodeMain)
        QtCore.QMetaObject.connectSlotsByName(BarcodeMain)

    def retranslateUi(self, BarcodeMain):
        _translate = QtCore.QCoreApplication.translate
        BarcodeMain.setWindowTitle(_translate("BarcodeMain", "MainWindow"))
        self.label.setText(_translate("BarcodeMain", "Штрих Код:"))
        self.pushButton.setText(_translate("BarcodeMain", "Синхронизировать базу"))
        self.label_3.setText(_translate("BarcodeMain", "Действителен"))
        self.label_2.setText(_translate("BarcodeMain", "Не действителен"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BarcodeMain = QtWidgets.QMainWindow()
    ui = Ui_BarcodeMain()
    ui.setupUi(BarcodeMain)
    BarcodeMain.show()
    sys.exit(app.exec_())

