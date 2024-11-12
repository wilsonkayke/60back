from db.session import SessionLocal
from sqlalchemy import text

def testar_conexao():
    try:
        # Inicia uma sessão
        session = SessionLocal()
        
        # Testa uma operação simples usando text()
        resultado = session.execute(text("SHOW TABLES;"))
        print("Conexão bem-sucedida! Tabelas no banco de dados:")
        for row in resultado:
            print(row)
        
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        # Encerra a sessão
        session.close()

if __name__ == "__main__":
    testar_conexao()
