from pydantic import BaseModel
from datetime import date
from enum import Enum

class StatusVozacaEnum(str, Enum):
    aktivno = 'aktivno'
    neaktivno = 'neaktivno'

class VozacBase(BaseModel):
    ime: str
    prezime: str
    broj_vozacke_dozvole: str
    datum_isteka_dozvole: date
    kategorije_vozacke_dozvole: str
    kontakt_informacije: str
    ogranicenja_za_voznju: str
    status: StatusVozacaEnum

class VozacCreate(VozacBase):
    pass

class VozacOut(VozacBase):
    id: int

    class Config:
        from_attributes = True
