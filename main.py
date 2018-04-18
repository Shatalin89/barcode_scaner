import sys
# Импортируем наш интерфейс из файла
from barcode import *
from dbwork import *
from utils import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.yesLabel.setText('')
        self.ui.noLabel.setText('')
        self.ui.lineEdit.setFocus()
        self.db = data_storage()
        self.tl = TikcetsLibs('')
        self.ui.comboBoxSity.addItems(['test', 'Irkutsk'])
        self.ui.pushButton.clicked.connect(self.sync_data)
        self.ui.comboBoxSity.currentIndexChanged.connect(self.set_focus)
        self.ui.comboBoxEvent.currentIndexChanged.connect(self.set_focus)
        self.ui.tableView.clicked.connect(self.set_focus)
        self.ui.tableView.horizontalScrollBar().valueChanged.connect(self.set_focus)
        self.ui.tableView.verticalScrollBar().valueChanged.connect(self.set_focus)

        self.current_sity = 'test'
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        for event in self.db.get_all_event():
            self.ui.comboBoxEvent.addItem(event['text'])

    def set_focus(self):
        self.current_sity = self.ui.comboBoxSity.currentText()
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        self.set_table_ticket(self.current_event, self.current_sity)
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText('')
        # self.set_table_ticket(self.current_event, self.current_sity)


    def set_table_ticket(self, nombilkn, sity):
        print('start set ticket table')
        dict_ticket = self.db.get_tickets(sity, nombilkn)
        i = 0
        self.ui.tableView.setRowCount(len(dict_ticket))
        for ticket in dict_ticket:
            # self.ui.tableView.horizontalHeaderItem(i).setText(str(ticket['id']) if ticket['id'] else str('None'))
            self.ui.tableView.setItem(i, 0, QTableWidgetItem(str(ticket['cod_hs'])))
            self.ui.tableView.setItem(i, 1, QTableWidgetItem(str(ticket['nombilkn'])))
            self.ui.tableView.setItem(i, 2, QTableWidgetItem(str(ticket['row'])))
            self.ui.tableView.setItem(i, 3, QTableWidgetItem(str(ticket['place'])))
            self.ui.tableView.setItem(i, 4, QTableWidgetItem(str(ticket['sector'])))
            self.ui.tableView.setItem(i, 5, QTableWidgetItem(str(ticket['nom_res'])))
            self.ui.tableView.setItem(i, 6, QTableWidgetItem(str(ticket['flag_check'])))
            if ticket['flag_check'] == True:
                self.ui.tableView.item(i, 0).setBackground(QtGui.QColor(0,128,0))
            i += 1

    def keyPressEvent(self, qKeyEvent):
        self.ui.yesLabel.setText('')
        self.ui.noLabel.setText('')
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            try:
                ticket_templ = 'Штрих-код: {cod_hs}\n' \
                               'Мероприятие: {name_event}\n' \
                               'Сектор: {sector}\n' \
                               'Ряд: {row} Место: {place}'
                cod_hs = int(self.ui.lineEdit.text())
                print(self.current_event)
                check = self.tl.check_ticket(cod_hs, int(self.current_event))
                if check['status'] == 'good':
                    self.ui.yesLabel.setText('Пропуск')
                    self.ui.noLabel.setText(ticket_templ.format(cod_hs=check['ticket']['cod_hs'],
                                                                ))
                    self.db.set_check_ticket(cod_hs)
                elif check['status'] == 'not_event':
                    self.ui.noLabel.setText('Не корректное \nмероприятие')
                elif check['status'] == 'not_ticket':
                    self.ui.noLabel.setText('Билет не найден')
                elif check['status'] == 'within':
                    self.ui.noLabel.setText('Билет уже \nпросканирован')
                else:
                    self.ui.noLabel.setText('Билет не \nдействителен')
                self.set_focus()
            except Exception as er:
                print(er)
                self.ui.yesLabel.setText('Ошибка ввода')
        else:
            super().keyPressEvent(qKeyEvent)
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText('')

    def sync_data(self):
        print('clicked')
        list_event = self.tl.get_seans()
        print(list_event)
        for i in list_event:
            print(i)
            self.tl.get_tickets(self.current_sity, i)
        self.ui.label_2.setText('Синхронизация завершена')
        self.set_focus()

        return True




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())