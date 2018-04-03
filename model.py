from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean, \
    ForeignKey, DateTime, create_engine
from sqlalchemy.sql.functions import now
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

metadata = MetaData()
engine = create_engine('sqlite:///base.db')
_SessionFactory = sessionmaker(bind=engine)



class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    nom_bill_kn = Column(Integer, nullable=True)
    date_event = Column(DateTime, default=now())
    name_event = Column(String, nullable=True)

    def __init__(self, nom_bill_kn):
        self.nom_bill_kn = nom_bill_kn


class Ticket(Base):

    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True)
    cod_hs = Column(Integer, nullable=True)
    row = Column(Integer, nullable=True)
    place = Column(Integer, nullable=True)
    sector = Column(Integer)
    nom_res = Column('NomRes', Integer, nullable=True)
    name = Column('Name', String, nullable=True)
    phone = Column('Phone', String, nullable=True)
    date_add = Column('date_add', DateTime, default=now())
    date_edit = Column('date_edit', DateTime, nullable=True)
    flag_check = Column('FlagCheck', Boolean, default=False)

    def __init__(self, cod_hs, nom_res):
        self.cod_hs = cod_hs
        self.nom_res = nom_res

    def __repr__(self):
        return "<Ticket('%s','%s','%s')>" % (self.cod_hs, self.row, self.place)



def session_factory():

    Base.metadata.create_all(engine)
    return _SessionFactory()
session_factory()