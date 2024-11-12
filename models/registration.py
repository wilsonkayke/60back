from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Registration(Base):
    __tablename__ = "inscricoes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    evento_id = Column(Integer, ForeignKey('eventos.id'))
