from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, create_jogada_model,create_nacao_model

# Create a Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///BD_2.db'
db.init_app(app)

# Define a route and its corresponding handler
@app.route('/')
def hello_world():
    return 'Hello, World!'




def main():
  # Usage example:
    with app.app_context():
        Nacao = create_nacao_model()

        nacoes = Nacao.query.all()

        print("Aqui estão as nações:\n")
        for nacao in nacoes:
            print(nacao.nome)
    app.run()

# Run the Flask application
if __name__ == '__main__':
    main()
