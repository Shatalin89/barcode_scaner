# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
#
# import sys
# from PyQt5.QtGui import QKeyEvent
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import (QWidget, QLabel,
#     QLineEdit, QApplication)
# import datetime
#
# class Example(QWidget):
#
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#
#     def initUI(self):
#         self.lbl = QLabel(self)
#         qle = QLineEdit(self)
#         qle.move(60, 100)
#         self.lbl.move(60, 40)
#         self.qle = qle
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('barcode scanner')
#         self.show()
#
#
#     def keyPressEvent(self, qKeyEvent):
#         print(qKeyEvent.key())
#         if qKeyEvent.key() == QtCore.Qt.Key_Return:
#
#
#             if self.qle.text() == self.dict_check['code']:
#                 self.lbl.setText(self.qle.text())
#                 print(True)
#             else:
#                 self.lbl.setText(self.qle.text())
#                 print(False)
#
#         else:
#             super().keyPressEvent(qKeyEvent)
#
#         self.qle.clear()
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())



import sys
# Импортируем наш интерфейс из файла
from barcode import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dict_check = {'code':'111'}
        self.ui.yesLabel.setText('')
        self.ui.noLabel.setText('')
        self.ui.lineEdit.setFocus()





    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_Return:


            if self.ui.lineEdit.text() == self.dict_check['code']:
                self.ui.yesLabel.setText(self.ui.lineEdit.text())
                print(True)
            else:
                self.ui.noLabel.setText(self.ui.lineEdit.text())
                print(False)
        else:
            super().keyPressEvent(qKeyEvent)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())