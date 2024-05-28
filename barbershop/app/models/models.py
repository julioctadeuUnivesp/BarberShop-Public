import sqlalchemy as db

class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

class Produto(db.Model):
    __tablename__ = 'Produtos'
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.String(50), nullable=False)

class Agendamento(db.Model):
    __tablename__ = 'Agendamentos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.String(50), nullable=False)
    servico = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(50), nullable=False)

class DataHora(db.Model):
    __tablename__ = 'Horario'
    id = db.Column(db.Integer, primary_key=True)
    datahora = db.Column(db.String(50), nullable=False)
