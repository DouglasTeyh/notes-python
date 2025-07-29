from flask import Flask
from dotenv import load_dotenv
import os
from app.routes.routes import note_bp
from app.db import db  #SQLAlchemy()

load_dotenv()

# Configurações do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Iniciando Banco de dados
db.init_app(app)

# Registrando rotas
app.register_blueprint(note_bp, url_prefix='/notes')

# Criando tabelas do banco de dados
with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso")

# Iniciando o app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
