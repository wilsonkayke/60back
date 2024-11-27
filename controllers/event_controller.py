from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal  # Importação absoluta
from models.event import Event  # Importação absoluta
from schemas.event_schema import EventCreate, EventResponse  # Importação dos modelos Pydantic
from services.event_service import EventService  # Serviço para manipulação dos dados

router = APIRouter()

# Função para obter o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de criação de evento
@router.post("/events/", response_model=EventResponse)  # Use o modelo Pydantic EventResponse
def create_event(event: EventCreate, db: Session = Depends(get_db)):  # Use o modelo Pydantic EventCreate
    event_service = EventService(db)
    new_event = event_service.create_event(event)
    return new_event
