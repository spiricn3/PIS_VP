from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from db.base_class import Base

class Vozilo(Base):
    __tablename__ = 'vozila'

    id = Column(Integer, primary_key=True, index=True)
    marka = Column(String(50), index=True)
    model = Column(String(50), index=True)
    registracijski_broj = Column(String(15), unique=True, index=True)
    datum_isteka_registracije = Column(Date)
    godina_proizvodnje = Column(Integer)
    tip_goriva = Column(Enum('dizel', 'benzin', 'plin', name='vrsta_goriva'), default='dizel')
    status = Column(Enum('dostupno', 'u servisu', 'rezervisano', name='status_vozila'), default='dostupno')
    
    radni_nalozi = relationship('RadniNalog', back_populates='vozilo')
