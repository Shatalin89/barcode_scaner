#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import QKeyEvent
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)
import datetime

class Example(QWidget):

    TEST_DICT = {
        'nombilk': 1517,
        'name': 'Lazarev',
        'date':datetime.datetime.now(),
        'ticket':[
            {
                'barcode': '039442030528',
                'name': 'ololo',
                'state': False
            },
            {
                'barcode': '5060255351406',
                'name': 'ololo2',
                'state': False
            }
        ]
}

    def __init__(self):
        super().__init__()
        self.dict_check = {'code': '039442030528'}

        self.initUI()


    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lbl.move(60, 40)
        self.qle = qle
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('barcode scanner')
        self.show()


    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_Return:

            print(self.dict_check['code'])
            print(self.qle.text())
            if self.qle.text() == self.dict_check['code']:
                self.lbl.setText(self.qle.text())
                print(True)
            else:
                self.lbl.setText(self.qle.text())
                print(False)

        else:
            super().keyPressEvent(qKeyEvent)

        self.qle.clear()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())