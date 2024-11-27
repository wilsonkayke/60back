from models.event import Event  # Modelo SQLAlchemy
from sqlalchemy.orm import Session
from schemas.event_schema import EventCreate  # Modelo Pydantic para entrada de dados

class EventService:
    def __init__(self, db: Session):
        self.db = db

    def create_event(self, event_create: EventCreate) -> Event:
        # Criação do evento com base no modelo Pydantic
        db_event = Event(
            nome=event_create.nome,
            descricao=event_create.descricao,
            data_inicio=event_create.data_inicio,
            data_fim=event_create.data_fim,
            responsavel_nome=event_create.responsavel_nome,
            responsavel_cpf=event_create.responsavel_cpf,
            responsavel_email=event_create.responsavel_email,
            vagas_disponiveis=event_create.vagas_disponiveis,
            data_limite_inscricao=event_create.data_limite_inscricao,
        )
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        return db_event
