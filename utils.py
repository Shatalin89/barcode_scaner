import requests


class TikcetLibs():

    def __init__(self, url, file=None):
        self.db = 'connsql'
        self.url_ticket_list = url
        self.path_file = file

    def get_tickets(self, method='URL'):
        if method == 'URL':
            pass
        elif method == "FILE":
            pass
        else:
            return {'ERROR':'INVALIT METHOD'}

    def __get_ticket_by_url(self, url):
        pass

    def __get_ticket_by_file(self, path):
        pass

    def check_ticket(self, barcode=None):
        pass