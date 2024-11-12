from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Event(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime, nullable=False)
    responsavel_nome = Column(String(100), nullable=False)
    responsavel_cpf = Column(String(11), nullable=False)
    responsavel_email = Column(String(100), nullable=False)
    vagas_disponiveis = Column(Integer, nullable=False)
    data_limite_inscricao = Column(DateTime, nullable=False)
