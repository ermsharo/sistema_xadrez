from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from models import (
    create_jogadas_model,
    create_participantes_campeonato_model,
    create_partida_model,
    create_registro_hospedagem_model,
    create_salao_model,
    db,
    create_jogada_model,
    create_nacao_model,
    create_participantes_model,
    create_campeonato_model,
    create_hospedagem_model,
)
import csv
from search_parameters import my_parameters
from players_by_country import players_by_country
import pandas as pd
from flask_cors import CORS
from random import randint, random
from datetime import datetime, timedelta
import random
from sqlalchemy.orm import joinedload

# Create a Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BD_2.db"
db.init_app(app)
app.register_blueprint(my_parameters)
app.register_blueprint(players_by_country)
CORS(app)


# Define a route and its corresponding handler
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.errorhandler(500)
def internal_server_error(error):
    return f"Error {error} ", 500


def generate_non_concurrent_intervals(n, start_date, end_date):
    intervals = []
    start_moment = start_date

    for _ in range(n):
        end_moment = start_moment + timedelta(minutes=30)
        if end_moment > end_date:
            break
        intervals.append({"start_moment": start_moment, "end_moment": end_moment})
        start_moment = end_moment

    return intervals


def generate_rand_hospedagem():
    Hospedagem = create_hospedagem_model()
    query = Hospedagem.query.filter_by().all()
    random_query = random.choice(query)
    random_id = random_query.id
    print("Rand_id", random_id)
    print("Rand_id", random_query.nome)
    return {"id": random_id, "nome": random_query.nome}


def subcribe_player_hotel(champeonato_id, start, end, hospedagem_id, participante):
    Registro_hospedagem = create_registro_hospedagem_model()
    novo_registro_hospedagem = Registro_hospedagem(
        chave_campeonato=champeonato_id,
        momento_entrada=start,
        momento_saida=end,
        chave_hospedagem=hospedagem_id,
        chave_participante=participante,
    )
    db.session.add(novo_registro_hospedagem)
    db.session.commit()


# def create_salao_model(champeonato_id, start, end, hospedagem_id, participante):
#     Registro_hospedagem = create_registro_hospedagem_model()
#     novo_registro_hospedagem = Registro_hospedagem(
#         chave_campeonato=champeonato_id,
#         momento_entrada=start,
#         momento_saida=end,
#         chave_hospedagem=hospedagem_id,
#         chave_participante=participante,
#     )
#     db.session.add(novo_registro_hospedagem)
#     db.session.commit()


def subcribe_salao(n, start_date, end_date):
    intervals = []
    start_moment = start_date

    for _ in range(n):
        end_moment = start_moment + timedelta(minutes=30)
        if end_moment > end_date:
            break
        intervals.append({"start_moment": start_moment, "end_moment": end_moment})
        start_moment = end_moment

    return intervals


def simulate_championship(
    players, arbrito, chave_campeonato, start_date, end_date, rand_hospedagem
):
    num_players = len(players)
    num_games = 4

    game_times = generate_non_concurrent_intervals(num_games, start_date, end_date)
    # Pegando os players que foram selecionados
    print("Game times", game_times)

    print("start date ", start_date)
    print("end date", end_date)

    fieldnames = [
        "jogador_primario",
        "jogador_secundario",
        "arbitro",
        "pecas_pretas",
        "pecas_brancas",
        "data_inicio",
        "data_fim",
        "vencedor",
        "id",
        "chave_campeonato",
        "chave_salao",
        "numero_jogadas",
    ]

    with open("championship.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        index = 0
        for game_id in range(num_games):
            print(" \n \n Index aqui ", index)
            game_time = game_times[index]
            print(" \n Dates here", game_time)
            index += 1
            jogador_primario = players[game_id % num_players]
            jogador_secundario = players[(game_id + 1) % num_players]
            arbitro = arbrito
            data_inicio = game_time["start_moment"]
            data_fim = game_time["end_moment"]
            vencedor = jogador_primario if randint(0, 1) == 0 else jogador_secundario
            hosp_id = rand_hospedagem["id"]
            hosp_name = rand_hospedagem["nome"]
            print("Hosp_id", hosp_id)
            chave_salao = subscribe_game_place(
                hosp_id, hosp_name, chave_campeonato, data_inicio, data_fim
            )
            numeros_jogadas = randint(6, 35)
            writer.writerow(
                {
                    "jogador_primario": jogador_primario,
                    "jogador_secundario": jogador_secundario,
                    "arbitro": arbitro,
                    "pecas_pretas": jogador_primario,
                    "pecas_brancas": jogador_secundario,
                    "data_inicio": data_inicio,
                    "data_fim": data_fim,
                    "vencedor": vencedor,
                    "id": game_id + 1,
                    "chave_campeonato": chave_campeonato,
                    "chave_salao": chave_salao,
                    "numero_jogadas": numeros_jogadas,
                }
            )

            subscribe_game(
                jogador_primario,
                jogador_secundario,
                arbitro,
                jogador_primario,
                jogador_secundario,
                data_inicio,
                data_fim,
                vencedor,
                chave_campeonato,
                chave_salao,
                numeros_jogadas,
            )

    print(
        f"Championship with {num_games} games simulated and saved to championship.csv."
    )


def pegar_campeonatos():
    Campeonato = create_campeonato_model()
    Campeonato_records = Campeonato.query.all()
    # print("Campeonato", Campeonato_records)
    record_list = [campeonato.__dict__ for campeonato in Campeonato_records]
    print("Aqui esta", record_list)
    new_record_list = [
        {"id": d["id"], "nome": d["nome"], "data_inicio": d["data_inicio"]}
        for d in record_list
    ]
    print(" \n \n  new rocrd list", new_record_list)
    return new_record_list


def findIdByCountry(nation):
    Nacao = create_nacao_model()
    query = Nacao.query.filter_by(nome=nation).first()
    # print(" \n Query result here ", query.id)
    return query.id


def generate_random_number(min, max):
    random_number = random.randint(min, max)
    return


def generate_nacoes():
    random_numbers = random.sample(range(1, 33), 5)
    print(random_numbers)
    return random_numbers


def get_rand_player_by_nation(nationID):
    Participantes = create_participantes_model()
    # Modify the query to retrieve all records
    query = Participantes.query.filter_by(chave_nacao=nationID).all()
    # Select a random query result
    random_query = random.choice(query)
    # Access the 'id' attribute of the random query result
    random_id = random_query.id
    return random_id


def subscribe_championship(person, function, championship, nation):
    Participantes_campeonato = create_participantes_campeonato_model()
    novo_participante_campeonato = Participantes_campeonato(
        funcao=function,
        chave_nacao=nation,
        chave_campeonato=championship,
        chave_participante=person,
    )
    db.session.add(novo_participante_campeonato)
    db.session.commit()


def get_rand_judge_by_nation(nacao):
    Participantes = create_participantes_model()
    # Modify the query to retrieve all records
    query = Participantes.query.filter_by(chave_nacao=nacao, arbitro=1).first()
    # Select a random query result

    # Access the 'id' attribute of the random query result
    random_id = query.id
    return random_id


def add_days(start_date_str, days_to_add):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    new_date = start_date + timedelta(days=days_to_add)
    return new_date


def get_matches(campeonato_id, start_date):
    # Precisamos aleatorizar 5 paises
    nacoes = generate_nacoes()
    arbitro = nacoes[4]
    nacoes.pop()
    print("nacoes", nacoes)
    start = add_days(start_date, 0)
    end = add_days(start_date, 5)

    randPlayersList = []
    ## pegando o lugar do jogo
    rand_hospedagem = generate_rand_hospedagem()

    # Após isso pegamos 4 jogadorer destes paises
    for nacao in nacoes:
        print("item ->", nacao)
        randp = get_rand_player_by_nation(nacao)
        randPlayersList.append(randp)
        print(" \n \n rand p id", randp)
        subscribe_championship(randp, "PLAYER", campeonato_id, nacao)
        subscribe_player_host(campeonato_id, start, end, rand_hospedagem["id"], randp)

    # Pegamos um arbitro deste pais
    randJudge = get_rand_judge_by_nation(arbitro)
    subscribe_championship(randJudge, "JUDGE", campeonato_id, arbitro)
    subscribe_player_host(campeonato_id, start, end, rand_hospedagem["id"], randJudge)
    # Cadastramos essas pessoas no campeonato
    player_list = randPlayersList
    arbrito = randJudge
    chave_campeonato = campeonato_id

    # Gerar os jogos
    simulate_championship(
        player_list, arbrito, chave_campeonato, start, end, rand_hospedagem
    )
    # pegar_campeonatos(player_list,arbrito,chave_campeonato)


def montar_chaves_campeonato():
    campeonatos = pegar_campeonatos()

    for campeonato in campeonatos:
        print("\n ", campeonato["nome"])
        print("\n ", campeonato["id"])


def subscribe_game_place(host_place, host_name, championship, start, end):
    Registro_salao = create_salao_model()
    posibles_names = ["Big room A", "Big room B", "Big room C", "Big room D"]
    place_name = f"{host_name}  -  {random.choice(posibles_names)}"

    novo_registro_salao = Registro_salao(
        capacidade=random.randrange(5, 101),
        radio=random.choice([True, False]),
        televisao=random.choice([True, False]),
        video=random.choice([True, False]),
        internet=random.choice([True, False]),
        nome=place_name,
        chave_campeonato=championship,
        inicio_uso=start,
        fim_uso=end,
        chave_hospedagem=host_place,
    )
    db.session.add(novo_registro_salao)
    db.session.commit()

    new_record_id = novo_registro_salao.id
    return new_record_id


def subscribe_player_host(championship, start, end, place, player):
    Registro_Hospedagem = create_registro_hospedagem_model()

    novo_registro_hospedagem = Registro_Hospedagem(
        chave_campeonato=championship,
        momento_entrada=start,
        momento_saida=end,
        chave_hospedagem=place,
        chave_participante=player,
    )
    db.session.add(novo_registro_hospedagem)
    db.session.commit()

    new_record_id = novo_registro_hospedagem.id
    return new_record_id


def subscribe_game(
    jogador_primario,
    jogador_secundario,
    arbitro,
    pecas_pretas,
    pecas_brancas,
    data_inicio,
    data_fim,
    vencedor,
    chave_campeonato,
    chave_salao,
    numero_jogadas,
):
    Registro_partida = create_partida_model()

    novo_registro_partida = Registro_partida(
        jogador_primario=jogador_primario,
        jogador_secundario=jogador_secundario,
        arbitro=arbitro,
        pecas_pretas=pecas_brancas,
        pecas_brancas=pecas_pretas,
        data_inicio=data_inicio,
        data_fim=data_fim,
        vencedor=vencedor,
        chave_campeonato=chave_campeonato,
        chave_salao=chave_salao,
        numero_jogadas=numero_jogadas,
    )
    db.session.add(novo_registro_partida)
    db.session.commit()

    new_record_id = novo_registro_partida.id
    return new_record_id


def pegar_partidas():
    Partida = create_partida_model()
    partidas_records = Partida.query.all()
    participantes = pegar_participantes()
    record_list = [partida.__dict__ for partida in partidas_records]
    new_record_list = [
        {
            "jogador_primario": d["jogador_primario"],
            "jogador_secundario": d["jogador_secundario"],
            "jogador_primario_nome": query_participantes(participantes,d["jogador_primario"]),
            "jogador_secundario_nome": query_participantes(participantes,d["jogador_secundario"]),
            "arbitro": d["arbitro"],
            "pecas_pretas": d["pecas_pretas"],
            "pecas_brancas": d["pecas_brancas"],
            "data_inicio": d["data_inicio"],
            "data_fim": d["data_fim"],
            "vencedor": d["vencedor"],
            "chave_campeonato": d["chave_campeonato"],
            "chave_salao": d["chave_salao"],
            "numero_jogadas": d["numero_jogadas"],
        }
        for d in record_list
    ]
    print("Partida records:", new_record_list)

   


def pegar_participantes():
    Participantes = create_participantes_model()
    participantes_records = Participantes.query.all()
    print("Partida records:", participantes_records)
    record_list = [participantes.__dict__ for participantes in participantes_records]
    new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    print("new record list", new_record_list)
    return new_record_list


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

def main():
    # Usage example:
    with app.app_context():
        # add_based_in_csv_hospedagem()
        # for nacao in nacoes:
        #     print(nacao.nome)
        # get_matches(2, "2023-06-06")
        # campeonatos = pegar_campeonatos()
        # for campeonato in campeonatos:
        #     print("\n ", campeonato["nome"])
        #     print("\n ", campeonato["id"])
        #     print("\n ", campeonato["data_inicio"])
        #     get_matches(campeonato["id"],campeonato["data_inicio"])

        pegar_partidas()
       

    app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
