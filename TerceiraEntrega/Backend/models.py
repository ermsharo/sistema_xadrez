from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_jogada_model():
    JOGADAS = db.Table('JOGADAS', db.metadata, autoload=True, autoload_with=db.engine)

    class Jogada(db.Model):
        __table__ = JOGADAS

        # Define any additional columns or methods here

    return Jogada

def create_nacao_model():
    NACAO = db.Table('NACAO', db.metadata, autoload=True, autoload_with=db.engine)

    class Nacao(db.Model):
        __table__ = NACAO

        # Define any additional columns or methods here

    return Nacao