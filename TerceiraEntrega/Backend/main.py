from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import (
    db,
    create_jogada_model,
    create_nacao_model,
    create_participantes_model,
    create_campeonato_model,
    create_hospedagem_model
)

from search_parameters import my_parameters
from players_by_country import players_by_country
import pandas as pd
import random
from flask_cors import CORS

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


def pegar_campeonatos():
    Campeonato = create_campeonato_model()
    Campeonato_records = Campeonato.query.all()
    print("Campeonato", Campeonato_records)
    

def findIdByCountry(nation):
    Nacao = create_nacao_model()
    query = Nacao.query.filter_by(nome=nation).first()
    # print(" \n Query result here ", query.id)
    return query.id


def generate_random_number(min, max):
    random_number = random.randint(min, max)
    return random_number


def main():
    # Usage example:
    with app.app_context():
        # add_based_in_csv_hospedagem()
        # for nacao in nacoes:
        #     print(nacao.nome)
        # pegar_campeonatos()
        app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
