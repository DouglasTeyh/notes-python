from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from config import Config

db = SQLAlchemy()

# Verifica se o banco de dados já existe
def init_db(app):
    load_dotenv()

    # Se o arquivo do banco de dados não existir, ele será criado
    if not os.path.exists(Config.SQLALCHEMY_DATABASE_URI):
        print("Creating database...")
    with app.app_context():
        db.create_all()
        print("Database created!")

if __name__ == '__main__':
    init_db()