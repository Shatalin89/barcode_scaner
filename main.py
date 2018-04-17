import sys
# Импортируем наш интерфейс из файла
from barcode import *
from dbwork import *
from utils import *
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
        self.db = data_storage()
        self.tl = TikcetsLibs('')
        self.ui.comboBoxSity.addItems(['test', 'Irkutsk'])
        for event in self.db.get_all_event():
            self.ui.comboBoxEvent.addItem(event['text'])





    def keyPressEvent(self, qKeyEvent):
        print(qKeyEvent.key())
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            cod_hs = int(self.ui.lineEdit.text())
            nmk = self.ui.comboBoxEvent.currentText().split(':')[0]
            print(cod_hs)
            print(nmk)
            self.tl.check_ticket(cod_hs, int(nmk))
        else:
            super().keyPressEvent(qKeyEvent)
        self.ui.lineEdit.setText('')


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())