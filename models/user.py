from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from .base import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    data_criacao = Column(TIMESTAMP, nullable=False, default=func.now())

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.senha)

    @staticmethod
    def hash_password(password):
        return pwd_context.hash(password)
