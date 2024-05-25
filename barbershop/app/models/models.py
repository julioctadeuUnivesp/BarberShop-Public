from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Column, Integer, String

Base = declarative_base()

class Usuarios(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    telefone = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False)

class Produtos(Base):
    id = Column(Integer, primary_key=True)
    produto = Column(String(50), nullable=False)
    preco = Column(String(50), nullable=False)

class Agendamento(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    telefone = Column(String(50), nullable=False)
    servico = Column(String(50), nullable=False)
    data = Column(String(50), nullable=False)

class DataHora(Base):
    id = Column(Integer, primary_key=True)
    datahora = Column(String(50), nullable=False)
