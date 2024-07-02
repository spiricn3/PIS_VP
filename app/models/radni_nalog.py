from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from db.base_class import Base

class RadniNalog(Base):
    __tablename__ = 'radni_nalozi'

    id = Column(Integer, primary_key=True, index=True)
    vozilo_id = Column(Integer, ForeignKey('vozila.id'), nullable=False)
    vozac_id = Column(Integer, ForeignKey('vozaci.id'), nullable=False)
    opis_zadatka = Column(String(100), nullable=False)
    datum_i_vrijeme_izdavanja = Column(DateTime)
    rok_zavrsavanja = Column(DateTime)
    status = Column(Enum('otvoren', 'u toku', 'zavrsen', name='status_radnog_naloga'), default='otvoren')

    vozilo = relationship('Vozilo', back_populates='radni_nalozi')
    vozac = relationship('Vozac', back_populates='radni_nalozi')
