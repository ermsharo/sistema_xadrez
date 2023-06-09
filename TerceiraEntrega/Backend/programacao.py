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

programacao = Blueprint("programacao", __name__)


def pegar_campeonatos():
    Campeonato = create_campeonato_model()
    Campeonato_records = Campeonato.query.all()
    # print("Campeonato", Campeonato_records)
    record_list = [campeonato.__dict__ for campeonato in Campeonato_records]
    print("Aqui esta", record_list)
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    print(" \n \n  new rocrd list", new_record_list)
    return new_record_list


def pegar_paises():
    Paises = create_nacao_model()
    paises_records = Paises.query.all()
    record_list = [paises.__dict__ for paises in paises_records]
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    return new_record_list


def pegar_partidas():
    Partida = create_partida_model()
    partidas_records = Partida.query.all()
    participantes = pegar_participantes()
    paises = pegar_paises()
    # print(" \n \n Paises ", paises)
    saloes = pegar_saloes()
    # print(" \n \n Saloes -> ", saloes)

    campeonatos = pegar_campeonatos()
    # print("\n \n Campeonato", campeonatos)
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
            "arbitro_nome": query_participantes(
                participantes, d["arbitro"]
            ),
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": d["vencedor"],
            "chave_campeonato": d["chave_campeonato"],
            "campeonato": query_campeonato(campeonatos, d["chave_campeonato"]),
            "chave_salao": d["chave_salao"],
            "salao": query_salao(saloes, d["chave_salao"]),
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in record_list
    ]
    print("Partida records:", new_record_list)
    return json.dumps(new_record_list)

def pegar_participantes():
    Participantes = create_participantes_model()
    participantes_records = Participantes.query.all()
    # print("Partida records:", participantes_records)
    record_list = [participantes.__dict__ for participantes in participantes_records]
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    # print("new record list", new_record_list)
    return new_record_list


def pegar_saloes():
    Salao = create_salao_model()
    Salao_records = Salao.query.all()
    hospedagens = pegar_hospedagens()
    # print("Partida records:", Salao_records)
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
    # print("new record list", new_record_list)
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


@programacao.route("/programacao")
def partidas():
    try:
        return pegar_partidas()
    except Exception as e:
        # Handle the error or return an appropriate response
        return str(e)
