from flask import Blueprint
from models import (
 create_partida_model
)

games_routes = Blueprint('parameters', __name__)


def pegar_partidas():
    Partidas = create_partida_model()
    partidas_records = Partidas.query.all()
    # print("Campeonato", Paises)
    # record_list = [partidas.__dict__ for partidas in partidas_records]
    # #print(" \n Record_list", record_list)
    # #print(" \n Record_list type:", type(record_list))

    # new_record_list = [{"id": d["id"], "nome": d["nome"]} for d in record_list]
    return partidas_records

@games_routes.route('/games')
def hotel_route():
    # Create your object
    
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object

