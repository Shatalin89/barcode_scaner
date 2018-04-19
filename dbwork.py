import sqlalchemy
import datetime
from model import Base, Event, Ticket
from sqlalchemy.orm import sessionmaker


class data_storage():

    def __init__(self, name_sity='test'):
        print('create_engine:', 'sqlite:///{name_sity}.db'.format(name_sity=name_sity))
        engine = sqlalchemy.create_engine('sqlite:///{name_sity}.db'.format(name_sity=name_sity))
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self.conn = session()

    def set_events(self, list_event):
        events = []
        for event in list_event:
            print(event)
            #вот тут проверка наличия мероприятия
            event_add = self.conn.query(Event).filter_by(nom_bill_kn=event['NomBilKn']).first()
            if not event_add:
                event_add =  Event(event['NomBilKn'])
            events.append(event['NomBilKn'])
            event_add.id = event['NomBilKn']
            event_add.name_event = event['Name_Spekt']
            print(event['DataSpekt'])
            if event['DataSpekt']:
                data_event = datetime.datetime.strptime(event['DataSpekt'], "%Y-%m-%dT%H:%M:%S")
                event_add.date_event = data_event
            self.conn.add(event_add)
        self.conn.commit()
        print(events)
        return events

    def set_tickets(self, nombilkn, list_tickets):
        for ticket in list_tickets:
            print(ticket)
            #вот тут добавить проверку наличия билета
            ticket_add = self.conn.query(Ticket).filter_by(nom_bill_kn=nombilkn, cod_hs=ticket['cod_hs']).first()
            if not ticket_add:
                ticket_add = Ticket(ticket['cod_hs'], nombilkn)
            ticket_add.status = ticket['status']
            ticket_add.place = ticket['SEAT']
            ticket_add.row = ticket['raw']
            ticket_add.sector = ticket['cod_zone']
            ticket_add.sector_name = ticket['NAME_sec']
            ticket_add.nom_kassa = ticket['NomKassa']
            ticket_add.nom_res = ticket['NOMRes']
            ticket_add.price = ticket['price']
            self.conn.add(ticket_add)
        self.conn.commit()

    def get_ticket(self, cod_hs):
        ticket = self.conn.query(Ticket).filter_by(cod_hs=cod_hs).first()
        data_res = None
        if ticket:
            data_res = {
                'cod_hs': ticket.cod_hs,
                'flag_check': ticket.flag_check,
                'nom_bill_kn': ticket.nom_bill_kn,
                'row': ticket.row,
                'price': ticket.price,
                'nom_kassa': ticket.nom_kassa,
                'name_sec': ticket.sector_name,
                'place': ticket.place,
                'nom_res': ticket.nom_res,
                'name': ticket.name,
                'status': ticket.status,

            }
        return data_res

    def get_tickets(self, sity, nombilkn):
        tickets = self.conn.query(Ticket).filter_by(nom_bill_kn=nombilkn).order_by(Ticket.flag_check).all()
        result = [{'id': ticket.id, 'cod_hs': ticket.cod_hs, 'nombilkn': ticket.nom_bill_kn, 'row': ticket.row, 'place': ticket.place, 'sector': ticket.sector, 'status': ticket.status, 'nom_res': ticket.nom_res, 'flag_check': ticket.flag_check} for ticket in tickets]
        return result

    def get_event(self, nom_bill_kn):
        event = self.conn.query(Event).filter_by(nom_bill_kn=nom_bill_kn).first()
        data_res = {
            'nom_bill_kn': event.nom_bill_kn,
            'date_event': event.date_event,
            'name_event': event.name_event,

        }
        return data_res

    def get_all_event(self):
        events = self.conn.query(Event).all()
        return [{'id': x.nom_bill_kn, 'text': str(x)} for x in events]

    def set_check_ticket(self, cod_hs):
        ticket = self.conn.query(Ticket).filter_by(cod_hs=cod_hs).first()
        ticket.flag_check = True
        self.conn.commit()

