from flask import Blueprint
import json
from models import create_campeonato_model, create_nacao_model

my_parameters = Blueprint('parameters', __name__)

def pegar_paises():
    Paises = create_nacao_model()
    paises_records = Paises.query.all()
    #print("Campeonato", Paises)
    record_list = [paises.__dict__ for paises in paises_records]
    print(" \n Record_list", record_list)
    print(" \n Record_list type:", type(record_list))

    new_record_list = [{'id': d['id'], 'nome': d['nome']} for d in record_list]
    print(json.dumps(new_record_list))
    return json.dumps(new_record_list)

@my_parameters.route('/hotel')
def hotel_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return pegar_paises()

@my_parameters.route('/paises')
def paises_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}
 
    # Return the object as JSON response
    return pegar_paises()

@my_parameters.route('/arbitros')
def arbitros_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object

@my_parameters.route('/jogadores')
def jogadores_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object
