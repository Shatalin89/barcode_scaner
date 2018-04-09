import sqlalchemy
import datetime
from model import *
from sqlalchemy.orm import sessionmaker


class data_storage():

    def __init__(self):
        session = sessionmaker(bind=engine)
        self.conn = session()

    def set_events(self, list_event):
        for event in list_event:
            event_add =  Event(event['NomBilKn'])
            event_add.id = event['NomBilKn']
            event_add.name_event = event['Name_Spekt']
            print(event['DataSpekt'])
            if event['DataSpekt']:
                data_event = datetime.datetime.strptime(event['DataSpekt'], "%Y-%m-%dT%H:%M:%S")
                event_add.date_event = data_event
            self.conn.add(event_add)
        self.conn.commit()

    def set_tickets(self, nombilkn, list_tickets):
        for ticket in list_tickets:
            ticket_add = Ticket(ticket['cod_hs'], nombilkn)
            ticket_add.status = ticket['STATUS']
            ticket_add.place = ticket['SEAT']
            ticket_add.row = ticket['RAW']
            ticket_add.sector = ticket['cod_zone']
            self.conn.add(ticket_add)
        self.conn.commit()
