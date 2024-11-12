from passlib.context import CryptContext

class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def bcrypt(cls, senha: str):
        return cls.pwd_context.hash(senha)
