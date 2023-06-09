from flask import Blueprint
import json
from models import (
    create_campeonato_model,
    create_hospedagem_model,
    create_nacao_model,
    create_participantes_model,
    create_partida_model,
    create_salao_model,
)
from sqlalchemy import or_

programacao_parametro = Blueprint("programacao_parametro", __name__)


def pegar_campeonatos():
    Campeonato = create_campeonato_model()
    Campeonato_records = Campeonato.query.all()

    record_list = [campeonato.__dict__ for campeonato in Campeonato_records]
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    return new_record_list


def pegar_paises():
    Paises = create_nacao_model()
    paises_records = Paises.query.all()
    record_list = [paises.__dict__ for paises in paises_records]
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    return new_record_list


def pegar_partidas(partida_id):
    Partida = create_partida_model()
    partidas_records = Partida.query.all()
    participantes = pegar_participantes()
    paises = pegar_paises()

    saloes = pegar_saloes()

    campeonatos = pegar_campeonatos()

    record_list = [partida.__dict__ for partida in partidas_records]
    new_record_list = [
        {
            "jogador_primario": d["jogador_primario"],
            "jogador_secundario": d["jogador_secundario"],
            "jogador_primario_nome": query_participantes(
                participantes, d["jogador_primario"]
            ),
            "jogador_secundario_nome": query_participantes(
                participantes, d["jogador_secundario"]
            ),
            "arbitro": d["arbitro"],
            "arbitro_nome": query_participantes(participantes, d["arbitro"]),
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": query_participantes(participantes, d["vencedor"]),
            "chave_campeonato": d["chave_campeonato"],
            "campeonato": query_campeonato(campeonatos, d["chave_campeonato"]),
            "chave_salao": d["chave_salao"],
            "salao": query_salao(saloes, d["chave_salao"]),
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in record_list
    ]
    return json.dumps(new_record_list)


def pegar_participantes():
    Participantes = create_participantes_model()
    participantes_records = Participantes.query.all()

    record_list = [participantes.__dict__ for participantes in participantes_records]
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]

    return new_record_list


def pegar_saloes():
    Salao = create_salao_model()
    Salao_records = Salao.query.all()
    hospedagens = pegar_hospedagens()

    record_list = [participantes.__dict__ for participantes in Salao_records]
    new_record_list = [
        {
            "id": d["id"],
            "capacidade": d["capacidade"],
            "radio": d["radio"],
            "televisao": d["televisao"],
            "video": d["video"],
            "internet": d["internet"],
            "inicio_uso": d["inicio_uso"],
            "fim_uso": d["fim_uso"],
            "nome": d["nome"],
            "chave_hospedagem": d["chave_hospedagem"],
            "hospedagem": query_hospedagem(hospedagens, d["chave_hospedagem"]),
        }
        for d in record_list
    ]
    return new_record_list


def pegar_hospedagens():
    Hospedagem = create_hospedagem_model()
    Hospedagem_records = Hospedagem.query.all()
    record_list = [hospedagem.__dict__ for hospedagem in Hospedagem_records]
    paises = pegar_paises()
    new_record_list = [
        {
            "id": d["id"],
            "nome": d["nome"],
            "cod_postal": d["cod_postal"],
            "endereco": d["endereco"],
            "nacao_id": d["nacao"],
            "nacao": query_pais(paises, d["nacao"]),
        }
        for d in record_list
    ]
    return new_record_list


def query_salao(saloes, id):
    for record in saloes:
        if record["id"] == id:
            return record
    return None


def query_salao_by_hotel(saloes, hotel_id):
    saloes_ids = []
    for record in saloes:
        print("Record here -> ", record["chave_hospedagem"])
        print("Hotel id here -> ",hotel_id )
        if str(record["chave_hospedagem"]) == str(hotel_id):
            print("Encontramos")
            saloes_ids.append(record['id'])

    return query_partida_by_salao(saloes_ids)

def query_partida_by_salao(saloes_ids):
    Partidas_id = []
    Partida = create_partida_model()
    partidas_records = Partida.query.all()
    record_list = [partida.__dict__ for partida in partidas_records]
    saloes = pegar_saloes()
    campeonatos = pegar_campeonatos()
    Partida = create_partida_model()
    participantes = pegar_participantes()
    new_record_list = [
        {
            "jogador_primario": d["jogador_primario"],
            "jogador_secundario": d["jogador_secundario"],
            "jogador_primario_nome": query_participantes(
                participantes, d["jogador_primario"]
            ),
            "jogador_secundario_nome": query_participantes(
                participantes, d["jogador_secundario"]
            ),
            "arbitro": d["arbitro"],
            "arbitro_nome": query_participantes(participantes, d["arbitro"]),
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": query_participantes(participantes, d["vencedor"]),
            "chave_campeonato": d["chave_campeonato"],
            "campeonato": query_campeonato(campeonatos, d["chave_campeonato"]),
            "chave_salao": d["chave_salao"],
            "salao": query_salao(saloes, d["chave_salao"]),
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in record_list
    ]


    for record in new_record_list:
        print("Record here -> ", record["chave_salao"])
        for salao_id in saloes_ids:
            if str(record["chave_salao"]) == str(salao_id):
                print("Encontramos")
                Partidas_id.append(record)
    print("Partidas id")
    return Partidas_id




def query_participantes(participantes, id):
    for record in participantes:
        if record["id"] == id:
            return record["nome"]
    return None


def query_pais(pais, id):
    for record in pais:
        if record["id"] == id:
            return record["nome"]
    return None


def query_campeonato(campeonato, id):
    for record in campeonato:
        if record["id"] == id:
            return record["nome"]
    return None


def query_hospedagem(hospedagem, id):
    for record in hospedagem:
        if record["id"] == id:
            return record
    return None


def query_games(saloes):
    Partida = create_partida_model()
    partidas_records = Partida.query.all()
    record_list = [partida.__dict__ for partida in partidas_records]


def CompararSaloes(record_list, saloes, hospedagem_id):
    saloesByHotel = query_salao_by_hotel(saloes, hospedagem_id)

    matching_records = [
        {
            key: record1[key]
            for key in [
                "pecas_pretas",
                "jogador_primario",
                "data_inicio",
                "vencedor",
                "chave_campeonato",
                "chave_salao",
                "arbitro",
                "pecas_brancas",
                "jogador_secundario",
                "data_fim",
                "id",
                "numero_jogadas",
            ]
        }
        for record1 in record_list
        for record2 in saloes
        if record1["chave_salao"] == record2["id"]
    ]

    return matching_records


@programacao_parametro.route("/hospedagem/<hospedagem>")
def programacao_parametros(hospedagem):
    saloes = pegar_saloes()
    saloes_by_hotel = query_salao_by_hotel(saloes, hospedagem)
    Partida = create_partida_model()
    partidas_records = Partida.query.all()
    participantes = pegar_participantes()
    paises = pegar_paises()

    campeonatos = pegar_campeonatos()

    record_list = [partida.__dict__ for partida in partidas_records]
    matchRecords = CompararSaloes(record_list, saloes, hospedagem)

    new_record_list = [
        {
            "jogador_primario": d["jogador_primario"],
            "jogador_secundario": d["jogador_secundario"],
            "jogador_primario_nome": query_participantes(
                participantes, d["jogador_primario"]
            ),
            "jogador_secundario_nome": query_participantes(
                participantes, d["jogador_secundario"]
            ),
            "arbitro": d["arbitro"],
            "arbitro_nome": query_participantes(participantes, d["arbitro"]),
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": query_participantes(participantes, d["vencedor"]),
            "chave_campeonato": d["chave_campeonato"],
            "campeonato": query_campeonato(campeonatos, d["chave_campeonato"]),
            "chave_salao": d["chave_salao"],
            "salao": query_salao(saloes, d["chave_salao"]),
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in matchRecords
    ]

    return json.dumps(saloes_by_hotel)


@programacao_parametro.route("/player/<player>")
def programacao_parametros_player(player):
    saloes = pegar_saloes()

    Partida = create_partida_model()
    partidas_records = Partida.query.filter(
        or_(Partida.jogador_primario == player, Partida.jogador_secundario == player)
    ).all()

    participantes = pegar_participantes()
    paises = pegar_paises()

    campeonatos = pegar_campeonatos()

    record_list = [partida.__dict__ for partida in partidas_records]

    new_record_list = [
        {
            "jogador_primario": d["jogador_primario"],
            "jogador_secundario": d["jogador_secundario"],
            "jogador_primario_nome": query_participantes(
                participantes, d["jogador_primario"]
            ),
            "jogador_secundario_nome": query_participantes(
                participantes, d["jogador_secundario"]
            ),
            "arbitro": d["arbitro"],
            "arbitro_nome": query_participantes(participantes, d["arbitro"]),
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": query_participantes(participantes, d["vencedor"]),
            "chave_campeonato": d["chave_campeonato"],
            "campeonato": query_campeonato(campeonatos, d["chave_campeonato"]),
            "chave_salao": d["chave_salao"],
            "salao": query_salao(saloes, d["chave_salao"]),
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in record_list
    ]

    return json.dumps(new_record_list)


@programacao_parametro.route("/judge/<player>")
def programacao_parametros_judge(player):
    saloes = pegar_saloes()

    Partida = create_partida_model()
    partidas_records = Partida.query.filter(or_(Partida.arbitro == player)).all()
    participantes = pegar_participantes()
    paises = pegar_paises()

    campeonatos = pegar_campeonatos()

    record_list = [partida.__dict__ for partida in partidas_records]

    new_record_list = [
        {
            "jogador_primario": d["jogador_primario"],
            "jogador_secundario": d["jogador_secundario"],
            "jogador_primario_nome": query_participantes(
                participantes, d["jogador_primario"]
            ),
            "jogador_secundario_nome": query_participantes(
                participantes, d["jogador_secundario"]
            ),
            "arbitro": d["arbitro"],
            "arbitro_nome": query_participantes(participantes, d["arbitro"]),
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": query_participantes(participantes, d["vencedor"]),
            "chave_campeonato": d["chave_campeonato"],
            "campeonato": query_campeonato(campeonatos, d["chave_campeonato"]),
            "chave_salao": d["chave_salao"],
            "salao": query_salao(saloes, d["chave_salao"]),
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in record_list
    ]

    return json.dumps(new_record_list)
