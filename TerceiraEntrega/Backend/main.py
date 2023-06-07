from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, create_jogada_model, create_nacao_model, create_participantes_model
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


def findIdByCountry(nation):
    Nacao = create_nacao_model()
    query = Nacao.query.filter_by(nome=nation).first()
    # print(" \n Query result here ", query.id)
    return query.id


def generate_random_number():
    random_number = random.randint(1000, 9999)
    return random_number


def add_based_in_csv():
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
        print(" \n nome: ", nome)
        print(" \n endereco: ", endereco)
        print(" \n telefone: ", telefone)
        print(" \n nivel_jogo: ", nivel_jogo)
        print(" \n arbitro: ", arbitro)
        print(" \n chave_nacao: ", chave_nacao)
        print(" \n numero_associado", numero_associado)
        add_participant(
            numero_associado, nome, endereco, telefone, nivel_jogo, chave_nacao, arbitro
        )

        # add_nation(nome)
        # Perform operations or computations on the row data
        # ...
        # Your code here


def main():
    # Usage example:
    with app.app_context():
        add_based_in_csv()
        # for nacao in nacoes:
        #     print(nacao.nome)
    app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
