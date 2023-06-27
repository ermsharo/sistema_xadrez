from flask import Blueprint
import json
from models import (
    create_campeonato_model,
    create_hospedagem_model,
    create_nacao_model,
    create_participantes_model,
)

games_number_rounds = Blueprint("games_number_rounds", __name__)



def count_nome_nacao(data):
    result = {}
    for item in data:
        nome_nacao = item["nome_nacao"]
        if nome_nacao not in result:
            result[nome_nacao] = 0
        result[nome_nacao] += 1
    return result


def get_players_by_country():
    Jogadores = create_participantes_model()
    jogadores_records = Jogadores.query.all()

    paises = pegar_paises()
    print("Campeonato", paises)

    record_list = [jogadores.__dict__ for jogadores in jogadores_records]
    # print(" \n Record_list", record_list)
    # print(" \n Record_list type:", type(record_list))

    new_record_list = [
        {           
            "id": d["id"],
            "nome": d["nome"],
            "chave_nacao": d["chave_nacao"],
            "numero_associado": d["numero_associado"],
            'nome_nacao' : filterCountryByID(paises, d["chave_nacao"])
        }
        for d in record_list
    ]

    counter_nome_nacao = count_nome_nacao(new_record_list)
    sorted_data = sorted(counter_nome_nacao.items(), key=lambda x: x[1], reverse=True)

    # Generate the transformed object
    result = [{"name": country, "value": value} for country, value in sorted_data]



    players_by_country_data = {'count_by_country': result, 'relative_data':new_record_list }
    # print(json.dumps(new_record_list))
    return json.dumps(players_by_country_data)


@games_number_rounds.route("/number_of_rounds")
def number_of_rounds():
    # Create your object

    # Return the object as JSON response
    return get_players_by_country()
