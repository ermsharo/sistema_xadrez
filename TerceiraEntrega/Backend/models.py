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

def create_hospedagem_model():
    HOSPEGADEM = db.Table('HOSPEGADEM', db.metadata, autoload=True, autoload_with=db.engine)

    class Hopedagem(db.Model):
        __table__ = HOSPEGADEM

        # Define any additional columns or methods here

    return Hopedagem

def create_jogadas_model():
    JOGADAS = db.Table('JOGADAS', db.metadata, autoload=True, autoload_with=db.engine)

    class Jogadas(db.Model):
        __table__ = JOGADAS

        # Define any additional columns or methods here

    return Jogadas

def create_campeonato_model():
    CAMPEONATO = db.Table('CAMPEONATO', db.metadata, autoload=True, autoload_with=db.engine)

    class Campeonato(db.Model):
        __table__ = CAMPEONATO

        # Define any additional columns or methods here

    return Campeonato


def create_participantes_model():
    PARTICIPANTES = db.Table('PARTICIPANTES', db.metadata, autoload=True, autoload_with=db.engine)

    class Participantes(db.Model):
        __table__ = PARTICIPANTES

        # Define any additional columns or methods here

    return Participantes

def create_participantes_campeonato_model():
    PARTICIPANTE_CAMPEONATO = db.Table('PARTICIPANTE_CAMPEONATO', db.metadata, autoload=True, autoload_with=db.engine)

    class Participante_campeonato(db.Model):
        __table__ = PARTICIPANTE_CAMPEONATO

        # Define any additional columns or methods here

    return Participante_campeonato

def create_partida_model():
    PARTIDA = db.Table('PARTIDA', db.metadata, autoload=True, autoload_with=db.engine)

    class Partida(db.Model):
        __table__ = PARTIDA

        # Define any additional columns or methods here

    return Partida


def create_ranking_geral_model():
    RANKING_GERAL = db.Table('RANKING_GERAL', db.metadata, autoload=True, autoload_with=db.engine)

    class Ranking_geral(db.Model):
        __table__ = RANKING_GERAL

        # Define any additional columns or methods here

    return Ranking_geral

def create_ranking_campeonato_model():
    RANKING_CAMPEONATO = db.Table('RANKING_CAMPEONATO', db.metadata, autoload=True, autoload_with=db.engine)

    class Ranking_campeonato(db.Model):
        __table__ = RANKING_CAMPEONATO

        # Define any additional columns or methods here

    return Ranking_campeonato

def create_registro_hospedagem_model():
    REGISTRO_HOSPEDAGEM = db.Table('REGISTRO_HOSPEDAGEM', db.metadata, autoload=True, autoload_with=db.engine)

    class Registro_hospedagem(db.Model):
        __table__ = REGISTRO_HOSPEDAGEM

        # Define any additional columns or methods here

    return Registro_hospedagem


def create_salao_model():
    SALAO = db.Table('SALAO', db.metadata, autoload=True, autoload_with=db.engine)

    class Salao(db.Model):
        __table__ = SALAO

        # Define any additional columns or methods here

    return Salao