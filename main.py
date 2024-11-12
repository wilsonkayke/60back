from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from controllers.user_controller import router as user_router
from controllers.event_controller import router as event_router
from db.session import SessionLocal
from models.user import User
from schemas.user_schema import UserCreate, UserResponse

app = FastAPI()

# Inclui os routers de eventos e usuários
app.include_router(user_router)
app.include_router(event_router)

# Função de dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint de criação de usuário
@app.post("/usuarios/", response_model=UserResponse)
def criar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado.")
    novo_usuario = User(nome=user.nome, email=user.email, senha=user.senha)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

# Endpoint de listagem de usuários
@app.get("/usuarios/", response_model=list[UserResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(User).all()
    return usuarios

# Endpoint de consulta de usuário por ID
@app.get("/usuarios/{id}", response_model=UserResponse)
def obter_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Endpoint de atualização de usuário
@app.put("/usuarios/{id}", response_model=UserResponse)
def atualizar_usuario(id: int, user: UserCreate, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario.nome = user.nome
    usuario.email = user.email
    usuario.senha = user.senha
    db.commit()
    db.refresh(usuario)
    return usuario

# Endpoint de exclusão de usuário
@app.delete("/usuarios/{id}")
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(User).filter(User.id == id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário deletado com sucesso!"}

# Rota de boas-vindas
@app.get("/")
def read_root():
    return {"Hello": "World"}
