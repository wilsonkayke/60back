from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventBase(BaseModel):
    titulo: str
    descricao: str
    data_inicio: datetime
    data_fim: datetime
    responsavel_nome: str  # Obrigatório
    responsavel_cpf: str   # Obrigatório
    responsavel_email: str # Obrigatório
    vagas_disponiveis: int
    data_limite_inscricao: datetime


class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int

    class Config:
        orm_mode = True

