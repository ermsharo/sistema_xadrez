from flask import Blueprint

games_routes = Blueprint('parameters', __name__)

@games_routes.route('/hotel')
def hotel_route():
    # Create your object
    
    my_object = {'name': 'John', 'age': 25}

    # Return the object as JSON response
    return my_object

