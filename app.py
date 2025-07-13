from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

app = Flask(__name__)

@app.route('/')
def index():
        return "Bem vindo a API de NOTAS com FLASK!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)