import requests
from dbwork import *


class TikcetsLibs:

    URL_SEANS = 'http://185.60.133.130:3370/api/events/all/{sity}/'
    URL_TICKETS = 'http://185.60.133.130:3370/api/event/place/{sity}/{nombilkn}/'
    TOKEN = '8bf0c515e9dd08d02e6ab0211d8996b371b7fcab'
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {token}'.format(token=TOKEN)}

    def __init__(self, name_base, file=None):
        self.db = 'connsql'
        self.url_ticket_list = ''
        self.path_file = file
        self.db = data_storage(name_base)

    def get_tickets(self, sity, nombilkn, method='URL'):
        if method == 'URL':
            self.__get_ticket_by_url(sity, nombilkn)
        elif method == "FILE":
            pass
        else:
            return {'ERROR': 'INVALIT METHOD'}

    def is_valid_ticket(self, ticket, event):
        if self.__check_ticket_in_event(ticket, event):
            return True

    def check_ticket(self, cod_hs, nombilkn):
        ticket = self.db.get_ticket(cod_hs)
        event = self.db.get_event(nombilkn)
        print(ticket)
        print(event)
        if not ticket:
            return {'status': 'not_ticket'}
        elif self.is_valid_ticket(ticket, event) and not self.__check_ticket_in_within(ticket):
            return {'status': 'good', 'ticket': ticket, 'event': self.db.get_event(ticket['nom_bill_kn'])}
        elif ticket['status'] != 'SOL':
            return {'status': 'status_not', 'ticket': ticket, 'event': self.db.get_event(ticket['nom_bill_kn'])}
        elif not self.__check_ticket_in_event(ticket, event):
            return {'status': 'not_event', 'ticket': ticket, 'event': self.db.get_event(ticket['nom_bill_kn'])}
        elif self.__check_ticket_in_within(ticket):
            return {'status': 'within', 'ticket': ticket, 'event': self.db.get_event(ticket['nom_bill_kn'])}
        else:
            return False



    def __check_ticket_in_event(self, ticket, current_event):
        if ticket['nom_bill_kn'] == current_event['nom_bill_kn'] and ticket['status'] == 'SOL':
            return True
        else:
            return False

    def __check_ticket_in_within(self, ticket):
        if ticket['flag_check']:
            return True
        else:
            return False

    def get_seans(self, sity, method='URL'):
        if method == 'URL':
            return self.__get_seans_by_url(sity)

    def __get_ticket_by_url(self, name_base, nom_bill_kn):
        res = self.get_data(self.URL_TICKETS.format(sity=name_base, nombilkn=nom_bill_kn)).json()
        self.db.set_tickets(nom_bill_kn, res[name_base])
        return True

    def get_data(self, url):
        return requests.get(url, headers=self.headers)

    def __get_seans_by_url(self, name_base):
        try:
            print(self.URL_SEANS.format(sity=name_base))
            res = self.get_data(self.URL_SEANS.format(sity=name_base)).json()
            print('res-------', res)
            print(res[name_base])
            return self.db.set_events(res[name_base])
        except Exception as er:
            print(er)
            return []

    def __get_ticket_by_file(self, name_base, nom_bill_kn):
        pass


