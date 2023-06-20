from flask import Blueprint

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/chess')
def my_route():
    # Create your object
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object