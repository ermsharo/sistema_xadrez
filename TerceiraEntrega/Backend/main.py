from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import (
    create_participantes_campeonato_model,
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


def subcribe_player_hotel(person, function, championship, nation):
    Participantes_campeonato = create_participantes_campeonato_model()
    novo_participante_campeonato = Participantes_campeonato(
        funcao=function,
        chave_nacao=nation,
        chave_campeonato=championship,
        chave_participante=person,
    )
    db.session.add(novo_participante_campeonato)
    db.session.commit()



def subcribe_player_hotel(n, start_date, end_date):
    intervals = []
    start_moment = start_date

    for _ in range(n):
        end_moment = start_moment + timedelta(minutes=30)
        if end_moment > end_date:
            break
        intervals.append({"start_moment": start_moment, "end_moment": end_moment})
        start_moment = end_moment

    return intervals

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



def simulate_championship(players, arbrito, chave_campeonato, start_date, end_date):
    num_players = len(players)
    num_games = 4

    game_times = generate_non_concurrent_intervals(num_games, start_date, end_date)
    print("Game times", game_times)
    # Shuffle the player names to randomize the pairings
    # shuffle(player_names)
    print("start date ", start_date)
    print("end date", end_date)
    game_i = 0
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

            chave_salao = f"Venue 1"

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
                    "numero_jogadas": randint(6, 35),
                }
            )

    print(
        f"Championship with {num_games} games simulated and saved to championship.csv."
    )


def pegar_campeonatos():
    Campeonato = create_campeonato_model()
    Campeonato_records = Campeonato.query.all()
    print("Campeonato", Campeonato_records)
    record_list = [campeonato.__dict__ for campeonato in Campeonato_records]
    print("Aqui esta", record_list)
    return record_list


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

    # Após isso pegamos 4 jogadorer destes paises
    for nacao in nacoes:
        print("item ->", nacao)
        randp = get_rand_player_by_nation(nacao)
        randPlayersList.append(randp)
        print(" \n \n rand p id", randp)
        subscribe_championship(randp, "PLAYER", campeonato_id, nacao)

    # Pegamos um arbitro deste pais
    randJudge = get_rand_judge_by_nation(arbitro)
    subscribe_championship(randJudge, "JUDGE", campeonato_id, arbitro)

    # Cadastramos essas pessoas no campeonato
    player_list = randPlayersList
    arbrito = randJudge
    chave_campeonato = campeonato_id

    # Gerar os jogos

    simulate_championship(player_list, arbrito, chave_campeonato, start, end)
    # pegar_campeonatos(player_list,arbrito,chave_campeonato)


def montar_chaves_campeonato():
    campeonatos = pegar_campeonatos()

    for campeonato in campeonatos:
        print("\n ", campeonato["nome"])
        print("\n ", campeonato["id"])


def main():
    # Usage example:
    with app.app_context():
        # add_based_in_csv_hospedagem()
        # for nacao in nacoes:
        #     print(nacao.nome)
        get_matches(2, "2023-06-06")
        app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
