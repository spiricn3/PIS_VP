from pydantic import BaseModel
from datetime import date
from enum import Enum

class TipGorivaEnum(str, Enum):
    dizel = 'dizel'
    benzin = 'benzin'
    plin = 'plin'

class StatusVozilaEnum(str, Enum):
    dostupno = 'dostupno'
    u_servisu = 'u servisu'
    rezervisano = 'rezervisano'

class VoziloBase(BaseModel):
    marka: str
    model: str
    registracijski_broj: str
    datum_isteka_registracije: date
    godina_proizvodnje: int
    tip_goriva: TipGorivaEnum
    status: StatusVozilaEnum

class VoziloCreate(VoziloBase):
    pass

class VoziloOut(VoziloBase):
    id: int

    class Config:
       from_attributes = True
