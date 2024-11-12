from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.user import User  # Importa o modelo User do SQLAlchemy
from schemas.user_schema import UserCreate, UserResponse
from services.auth_service import Hash

router = APIRouter()

# Função de dependência para conexão com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Checa se o email já existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado.")
    # Cria e adiciona o usuário ao banco de dados
    hashed_password = Hash.bcrypt(user.senha)
    new_user = User(nome=user.nome, email=user.email, senha=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
