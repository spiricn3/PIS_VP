from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.vozilo import Vozilo
from schemas.vozilo import VoziloCreate, VoziloOut
from db import get_db

router = APIRouter()

@router.post("/", response_model=VoziloOut)
def create_vozilo(vozilo: VoziloCreate, db: Session = Depends(get_db)):
    db_vozilo = Vozilo(**vozilo.dict())
    db.add(db_vozilo)
    db.commit()
    db.refresh(db_vozilo)
    return db_vozilo

@router.get("/", response_model=List[VoziloOut])
def get_vozila(db: Session = Depends(get_db)):
    vozila = db.query(Vozilo).all()
    if not vozila:
        raise HTTPException(status_code=404, detail="Nema dostupnih vozila")
    return vozila

@router.get("/{vozilo_id}", response_model=VoziloOut)
def get_vozilo(vozilo_id: int, db: Session = Depends(get_db)):
    vozilo = db.query(Vozilo).filter(Vozilo.id == vozilo_id).first()
    if not vozilo:
        raise HTTPException(status_code=404, detail="Vozilo nije pronađeno")
    return vozilo

@router.put("/{vozilo_id}", response_model=VoziloOut)
def update_vozilo(vozilo_id: int, vozilo: VoziloCreate, db: Session = Depends(get_db)):
    db_vozilo = db.query(Vozilo).filter(Vozilo.id == vozilo_id).first()
    if not db_vozilo:
        raise HTTPException(status_code=404, detail="Vozilo nije pronađeno")
    for key, value in vozilo.dict().items():
        setattr(db_vozilo, key, value)
    db.commit()
    db.refresh(db_vozilo)
    return db_vozilo

@router.delete("/{vozilo_id}")
def delete_vozilo(vozilo_id: int, db: Session = Depends(get_db)):
    db_vozilo = db.query(Vozilo).filter(Vozilo.id == vozilo_id).first()
    if not db_vozilo:
        raise HTTPException(status_code=404, detail="Vozilo nije pronađeno")
    db.delete(db_vozilo)
    db.commit()
    return {"detail": "Vozilo je uspešno obrisano"}
