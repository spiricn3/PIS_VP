from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.radni_nalog import RadniNalog
from schemas.radni_nalog import RadniNalogCreate, RadniNalogOut
from db import get_db

router = APIRouter()

@router.post("/", response_model=RadniNalogOut)
def create_radni_nalog(radni_nalog: RadniNalogCreate, db: Session = Depends(get_db)):
    db_radni_nalog = RadniNalog(**radni_nalog.dict())
    db.add(db_radni_nalog)
    db.commit()
    db.refresh(db_radni_nalog)
    return db_radni_nalog

@router.get("/", response_model=List[RadniNalogOut])
def get_radni_nalozi(db: Session = Depends(get_db)):
    radni_nalozi = db.query(RadniNalog).all()
    if not radni_nalozi:
        raise HTTPException(status_code=404, detail="Nema dostupnih radnih naloga")
    return radni_nalozi

@router.get("/{radni_nalog_id}", response_model=RadniNalogOut)
def get_radni_nalog(radni_nalog_id: int, db: Session = Depends(get_db)):
    radni_nalog = db.query(RadniNalog).filter(RadniNalog.id == radni_nalog_id).first()
    if not radni_nalog:
        raise HTTPException(status_code=404, detail="Radni nalog nije pronađen")
    return radni_nalog

@router.put("/{radni_nalog_id}", response_model=RadniNalogOut)
def update_radni_nalog(radni_nalog_id: int, radni_nalog: RadniNalogCreate, db: Session = Depends(get_db)):
    db_radni_nalog = db.query(RadniNalog).filter(RadniNalog.id == radni_nalog_id).first()
    if not db_radni_nalog:
        raise HTTPException(status_code=404, detail="Radni nalog nije pronađen")
    for key, value in radni_nalog.dict().items():
        setattr(db_radni_nalog, key, value)
    db.commit()
    db.refresh(db_radni_nalog)
    return db_radni_nalog

@router.delete("/{radni_nalog_id}")
def delete_radni_nalog(radni_nalog_id: int, db: Session = Depends(get_db)):
    db_radni_nalog = db.query(RadniNalog).filter(RadniNalog.id == radni_nalog_id).first()
    if not db_radni_nalog:
        raise HTTPException(status_code=404, detail="Radni nalog nije pronađen")
    db.delete(db_radni_nalog)
    db.commit()
    return {"detail": "Radni nalog je uspešno obrisan"}
