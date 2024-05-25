from flask import Flask
from app import create_app, db
from models.models import Usuarios, Produtos, Agendamento, DataHora

application = create_app()

with application.app_context():
    db.create_all()

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
