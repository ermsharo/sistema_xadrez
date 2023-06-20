from flask import Blueprint

my_parameters = Blueprint('parameters', __name__)


# Retornar em um endpoint 

# Hoteis

@my_parameters.route('/hotel')
def my_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object

# Paises

@my_parameters.route('/paises')
def my_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object

# Arbitros

@my_parameters.route('/arbitros')
def my_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object

# Jogadores 

@my_parameters.route('/jogadores')
def my_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object