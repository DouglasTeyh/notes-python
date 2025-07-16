from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
                                                            # Substituir depois pelos reais do PostgreSQL
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://seu_usuario:sua_senha@seu_host:sua_porta/seu_banco_de_dados"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    CORS(app)

    with app.app_context():
        from .models.model import Note

    from .routes.routes import note_bp
    app.register_blueprint(note_bp, url_prefix='/notes')

    return app