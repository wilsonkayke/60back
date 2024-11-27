from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Event(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(Text, nullable=True)
    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime, nullable=False)
    localizacao = Column(String(255), nullable=True)
    organizador_id = Column(Integer, ForeignKey('usuarios.id'), nullable=True)
    vagas_disponiveis = Column(Integer, nullable=False)
    data_limite_inscricao = Column(DateTime, nullable=False)

    organizador = relationship("User", back_populates="eventos")


