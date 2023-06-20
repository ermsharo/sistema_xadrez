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
import pandas as pd
import random

# Create a Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BD_2.db"
db.init_app(app)


# Define a route and its corresponding handler
@app.route("/")
def hello_world():
    return "Hello, World!"


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
        add_based_in_csv_hospedagem()
        # for nacao in nacoes:
        #     print(nacao.nome)
    app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
