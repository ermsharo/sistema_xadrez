from models import (
    create_participantes_campeonato_model,
    create_partida_model,
    create_registro_hospedagem_model,
    create_salao_model,
    db,
    create_nacao_model,
    create_participantes_model,
    create_campeonato_model,
    create_hospedagem_model,
)
import csv
from random import randint, random
from datetime import datetime, timedelta
import random


def add_campeonato(data_inicio, nome, nacao, jornada):
    Campeonato = create_campeonato_model()
    novo_campeonato = Campeonato(
        data_inicio=data_inicio,
        nome=nome,
        jornada=jornada,
        nacao=nacao,
    )
    db.session.add(novo_campeonato)
    db.session.commit()



def add_hospedagem(nome, cod_postal, endereco, nacao):
    Hospedagem = create_hospedagem_model()
    novo_hospedagem = Hospedagem(
        cod_postal=cod_postal,
        nome=nome,
        endereco=endereco,
        nacao=nacao,
    )
    db.session.add(novo_hospedagem)
    db.session.commit()


def add_based_in_csv_hospedagem():
    df = pd.read_csv("HOSPEDAGEM.csv")
    for index, row in df.iterrows():
        # Access the values of each column in the current row
        nome = row["nome"]
        cod_postal = row["cod_postal"]
        endereco = row["endereco"]
        nacao = row["nacao"]
        add_hospedagem(nome, cod_postal, endereco, nacao)



def add_based_in_csv_participantes():
    df = pd.read_csv("PARTICIPANTES.csv")
    for index, row in df.iterrows():
        # Access the values of each column in the current row
        nome = row["nome"]
        endereco = row["endereco"]
        telefone = row["telefone"]
        nivel_jogo = row["nivel_jogo"]
        chave_nacao = row["chave_nacao"]
        arbitro = row["arbitro"]
        chave_nacao = findIdByCountry(chave_nacao)
        numero_associado = generate_random_number()
        # print(" \n nome: ", nome)
        # print(" \n endereco: ", endereco)
        # print(" \n telefone: ", telefone)
        # print(" \n nivel_jogo: ", nivel_jogo)
        # print(" \n arbitro: ", arbitro)
        # print(" \n chave_nacao: ", chave_nacao)
        # print(" \n numero_associado", numero_associado)
        add_participant(
            numero_associado, nome, endereco, telefone, nivel_jogo, chave_nacao, arbitro
        )

        # add_nation(nome)
        # Perform operations or computations on the row data
        # ...
        # Your code here

def add_based_in_csv_campeonato():
    df = pd.read_csv("CAMPEONATO.csv")
    for index, row in df.iterrows():
        # Access the values of each column in the current row
        nome = row["nome"]
        data_inicio = row["data_inicio"]
        jornada = row["jornada"]
        nacao = generate_random_number(1, 33)
        add_campeonato(data_inicio, nome, nacao, jornada)


def add_nation(nation):
    Nacao = create_nacao_model()
    nova_nacao = Nacao(nome=nation)
    db.session.add(nova_nacao)
    db.session.commit()

def add_nation(nation):
    Nacao = create_nacao_model()
    nova_nacao = Nacao(nome=nation)
    db.session.add(nova_nacao)
    db.session.commit()

def add_participant(
    numero_associado, nome, endereco, telefone, nivel_jogo, chave_nacao, arbitro
):
    Participante = create_participantes_model()
    novo_participante = Participante(
        numero_associado=numero_associado,
        nome=nome,
        endereco=endereco,
        telefone=telefone,
        nivel_jogo=nivel_jogo,
        chave_nacao=chave_nacao,
        arbitro=arbitro,
    )
    db.session.add(novo_participante)
    db.session.commit()


def add_participant(
    numero_associado, nome, endereco, telefone, nivel_jogo, chave_nacao, arbitro
):
    Participante = create_participantes_model()
    novo_participante = Participante(
        numero_associado=numero_associado,
        nome=nome,
        endereco=endereco,
        telefone=telefone,
        nivel_jogo=nivel_jogo,
        chave_nacao=chave_nacao,
        arbitro=arbitro,
    )
    db.session.add(novo_participante)
    db.session.commit()