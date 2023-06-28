from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from models import (
    db,
)
import csv
from search_parameters import my_parameters
from players_by_country import players_by_country
from games_number_of_rounds import  games_number_rounds
from find_by_parameter import programacao_parametro
from programacao import programacao

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
app.register_blueprint(programacao)
app.register_blueprint(programacao_parametro)
app.register_blueprint(games_number_rounds)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.errorhandler(500)
def internal_server_error(error):
    return f"Error {error} ", 500


def main():
    # Usage example:
    # with app.app_context():
    app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
