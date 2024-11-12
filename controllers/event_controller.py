from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal  # Importação absoluta
from models.event import Event  # Importação absoluta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/events/", response_model=Event)
def create_event(event: Event, db: Session = Depends(get_db)):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event
