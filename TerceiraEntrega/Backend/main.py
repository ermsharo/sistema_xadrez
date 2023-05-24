from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Create a Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)
# Define a route and its corresponding handler
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()
