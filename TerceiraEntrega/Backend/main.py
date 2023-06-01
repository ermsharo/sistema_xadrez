from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Create a Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BD_2.db'
db = SQLAlchemy(app)

# Lets add the nations

def add_nation():
    print("add nation")

# Define a route and its corresponding handler
@app.route('/')
def hello_world():
    return 'Hello, World!'


def main():
    print('running main')
    app.run()

# Run the Flask application
if __name__ == '__main__':
    main()
