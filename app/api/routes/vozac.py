from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.vozac import Vozac
from schemas.vozac import VozacCreate, VozacOut
from db import get_db

router = APIRouter()

@router.post("/", response_model=VozacOut)
def create_vozac(vozac: VozacCreate, db: Session = Depends(get_db)):
    db_vozac = Vozac(**vozac.dict())
    db.add(db_vozac)
    db.commit()
    db.refresh(db_vozac)
    return db_vozac

@router.get("/", response_model=List[VozacOut])
def get_vozaci(db: Session = Depends(get_db)):
    vozaci = db.query(Vozac).all()
    if not vozaci:
        raise HTTPException(status_code=404, detail="Nema dostupnih vozača")
    return vozaci

@router.get("/{vozac_id}", response_model=VozacOut)
def get_vozac(vozac_id: int, db: Session = Depends(get_db)):
    vozac = db.query(Vozac).filter(Vozac.id == vozac_id).first()
    if not vozac:
        raise HTTPException(status_code=404, detail="Vozač nije pronađen")
    return vozac

@router.put("/{vozac_id}", response_model=VozacOut)
def update_vozac(vozac_id: int, vozac: VozacCreate, db: Session = Depends(get_db)):
    db_vozac = db.query(Vozac).filter(Vozac.id == vozac_id).first()
    if not db_vozac:
        raise HTTPException(status_code=404, detail="Vozač nije pronađen")
    for key, value in vozac.dict().items():
        setattr(db_vozac, key, value)
    db.commit()
    db.refresh(db_vozac)
    return db_vozac

@router.delete("/{vozac_id}")
def delete_vozac(vozac_id: int, db: Session = Depends(get_db)):
    db_vozac = db.query(Vozac).filter(Vozac.id == vozac_id).first()
    if not db_vozac:
        raise HTTPException(status_code=404, detail="Vozač nije pronađen")
    db.delete(db_vozac)
    db.commit()
    return {"detail": "Vozač je uspešno obrisan"}
