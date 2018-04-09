import requests
from dbwork import *


class TikcetsLibs:


    URL_SEANS = 'http://185.60.133.130:3370/api/events/all/'
    URL_TICKETS = 'http://185.60.133.130:3370/api/event/place/{nombilkn}/'
    TOKEN = 'token'
    headers = {'Content-type': 'application/json',
               'Authorization': 'Token {token}'.format(token=TOKEN)}

    def __init__(self, url, file=None):
        self.db = 'connsql'
        self.url_ticket_list = url
        self.path_file = file
        self.db = data_storage()

    def get_tickets(self, method='URL'):
        if method == 'URL':
            self.__get_ticket_by_url('test', 20)
        elif method == "FILE":
            pass
        else:
            return {'ERROR':'INVALIT METHOD'}


    def get_seans(self, method='URL'):
        if method == 'URL':
            self.__get_seans_by_url('test')

    def __get_ticket_by_url(self, name_base, nom_bill_kn):
        res = self.get_data(self.URL_TICKETS.format(nombilkn=nom_bill_kn)).json()
        self.db.set_tickets(nom_bill_kn, res[name_base])
        return True

    def get_data(self, url):
        return requests.get(url, headers=self.headers)

    def __get_seans_by_url(self, name_base):
        res = self.get_data(self.URL_SEANS).json()
        print(res[name_base])
        self.db.set_events(res[name_base])
        return True

    def __get_ticket_by_file(self, name_base, nom_bill_kn):
        pass

    def check_ticket(self, barcode=None):
        pass
