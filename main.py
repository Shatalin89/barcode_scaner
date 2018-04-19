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
        self.ui.comboBoxSity.addItems(['irkutsk','ulanude','bratsk','chita','test'])
        self.ui.pushButton.clicked.connect(self.sync_data)
        self.ui.syncTicketButton.clicked.connect(self.sync_tickets_one_event)
        self.ui.comboBoxSity.currentIndexChanged.connect(self.set_combobox_event)
        self.ui.comboBoxEvent.currentIndexChanged.connect(self.change_combobox)
        self.ui.tableView.clicked.connect(self.set_focus)
        self.ui.tableView.horizontalScrollBar().valueChanged.connect(self.set_focus_after_scroll)
        self.ui.tableView.verticalScrollBar().valueChanged.connect(self.set_focus_after_scroll)
        self.current_sity = self.ui.comboBoxSity.currentText()
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        self.tl = TikcetsLibs(self.current_sity)
        self.db = data_storage(self.current_sity)
        self.set_combobox_event()

    def set_combobox_event(self):
        del self.tl
        del self.db
        self.current_sity = self.ui.comboBoxSity.currentText()
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        self.ui.comboBoxEvent.clear()
        self.tl = TikcetsLibs(self.current_sity)
        self.db = data_storage(self.current_sity)
        for event in self.db.get_all_event():
            self.ui.comboBoxEvent.addItem(event['text'])
        self.set_table_ticket(self.current_event, self.current_sity)

        self.set_focus()

    def change_combobox(self):
        self.current_sity = self.ui.comboBoxSity.currentText()
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        self.set_table_ticket(self.current_event, self.current_sity)
        self.set_focus()


    def set_focus(self):
        self.current_sity = self.ui.comboBoxSity.currentText()
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        self.set_table_ticket(self.current_event, self.current_sity)
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText('')

    def set_focus_after_scroll(self):
        self.current_sity = self.ui.comboBoxSity.currentText()
        self.current_event = self.ui.comboBoxEvent.currentText().split(':')[0]
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText('')

    def set_table_ticket(self, nombilkn, sity):
        print('start set ticket table')
        dict_ticket = self.db.get_tickets(sity, nombilkn)
        i = 0
        self.ui.tableView.setRowCount(len(dict_ticket))
        for ticket in dict_ticket:
            self.ui.tableView.setItem(i, 0, QTableWidgetItem(str(ticket['cod_hs'])))
            self.ui.tableView.setItem(i, 1, QTableWidgetItem(str(ticket['nombilkn'])))
            self.ui.tableView.setItem(i, 2, QTableWidgetItem(str(ticket['status'])))
            self.ui.tableView.setItem(i, 3, QTableWidgetItem(str(ticket['row'])))
            self.ui.tableView.setItem(i, 4, QTableWidgetItem(str(ticket['place'])))
            self.ui.tableView.setItem(i, 5, QTableWidgetItem(str(ticket['sector'])))
            self.ui.tableView.setItem(i, 6, QTableWidgetItem(str(ticket['nom_res'])))
            self.ui.tableView.setItem(i, 7, QTableWidgetItem(str(ticket['flag_check'])))
            if ticket['flag_check'] == True:
                self.ui.tableView.item(i, 0).setBackground(QtGui.QColor(0,115,0))
            i += 1

    def sync_tickets_one_event(self):
        self.ui.label_2.setText('Синхронизация мероприятия: {event}\nначата'.format(event=self.current_event))
        self.tl.get_tickets(self.current_sity, self.current_event)
        self.set_table_ticket(self.current_event, self.current_sity)
        self.ui.label_2.setText('Синхронизация мероприятия: {event}\nзакончена'.format(event=self.current_event))

    def keyPressEvent(self, qKeyEvent):
        self.ui.yesLabel.setText('')
        self.ui.noLabel.setText('')
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            try:
                ticket_templ = 'Штрих-код: {cod_hs}\n' \
                               'Мероприятие: {name_event}\n' \
                               'Сектор: {sector}\n' \
                               'Ряд: {row} Место: {place}\n' \
                               'Cтоимость: {price}\n' \
                               'Касса: {kassa}'
                cod_hs = int(self.ui.lineEdit.text())
                check = self.tl.check_ticket(cod_hs, int(self.current_event))
                print(check['status'])
                if check['status'] == 'good':
                    self.ui.yesLabel.setText('Пропуск')
                    self.ui.yesLabel.setStyleSheet('color: green')
                    self.ui.noLabel.setText(ticket_templ.format(cod_hs=check['ticket']['cod_hs'],
                                                                name_event=check['event']['name_event'],
                                                                sector=check['ticket']['name_sec'],
                                                                row=check['ticket']['row'],
                                                                place=check['ticket']['place'],
                                                                price=check['ticket']['price'],
                                                                kassa=check['ticket']['nom_kassa'] if check['ticket']['nom_kassa'] > -300 else 'Интернет',
                                                                ))
                    self.db.set_check_ticket(cod_hs)
                elif check['status'] == 'not_event':
                    self.ui.yesLabel.setText('Не корректное \nмероприятие')
                    self.ui.yesLabel.setStyleSheet('color: red')
                    self.ui.noLabel.setText(ticket_templ.format(cod_hs=check['ticket']['cod_hs'],
                                                                name_event=check['event']['name_event'],
                                                                sector=check['ticket']['name_sec'],
                                                                row=check['ticket']['row'],
                                                                place=check['ticket']['place'],
                                                                price=check['ticket']['price'],
                                                                kassa=check['ticket']['nom_kassa'] if check['ticket'][
                                                                                                          'nom_kassa'] > -300 else 'Интернет',
                                                                ))
                elif check['status'] == 'not_ticket':
                    self.ui.yesLabel.setText('Билет не найден')
                    self.ui.yesLabel.setStyleSheet('color: red')
                elif check['status'] == 'within':
                    self.ui.yesLabel.setText('Билет уже \nпросканирован')
                    self.ui.yesLabel.setStyleSheet('color: red')
                    self.ui.noLabel.setText(ticket_templ.format(cod_hs=check['ticket']['cod_hs'],
                                                                name_event=check['event']['name_event'],
                                                                sector=check['ticket']['name_sec'],
                                                                row=check['ticket']['row'],
                                                                place=check['ticket']['place'],
                                                                price=check['ticket']['price'],
                                                                kassa=check['ticket']['nom_kassa'] if check['ticket'][
                                                                                                          'nom_kassa'] > -300 else 'Интернет',
                                                                ))
                elif check['status'] == 'status_not':
                    self.ui.yesLabel.setText('Не корректный статус\nбилета')
                    self.ui.yesLabel.setStyleSheet('color: red')
                    self.ui.noLabel.setText(ticket_templ.format(cod_hs=check['ticket']['cod_hs'],
                                                                name_event=check['event']['name_event'],
                                                                sector=check['ticket']['name_sec'],
                                                                row=check['ticket']['row'],
                                                                place=check['ticket']['place'],
                                                                price=check['ticket']['price'],
                                                                kassa=check['ticket']['nom_kassa'] if check['ticket'][
                                                                                                          'nom_kassa'] > -300 else 'Интернет',
                                                                ))
                else:
                    self.ui.yesLabel.setText('Билет не \nдействителен')
                    self.ui.yesLabel.setStyleSheet('color: red')
                self.set_focus()
            except Exception as er:
                print(er)
                self.ui.yesLabel.setText('Ошибка ввода')
                self.ui.yesLabel.setStyleSheet('color: red')
        else:
            super().keyPressEvent(qKeyEvent)
        self.ui.lineEdit.setFocus()
        self.ui.lineEdit.setText('')

    def sync_data(self):
        try:
            print('clicked')
            self.ui.label_2.setText('Синхронизация списка\n мероприятий начата')
            list_event = self.tl.get_seans(self.current_sity)
            self.set_combobox_event()
            self.set_table_ticket(self.current_event, self.current_sity)
            self.ui.label_2.setText('Синхронизация списка\n мероприятий завершена')
            self.set_focus()
        except Exception as er:
            print(er)
            self.ui.label_2.setText('Ошибка синхронизации')
        return True


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())