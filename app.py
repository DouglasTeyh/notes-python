from app import create_app
from app.routes.routes import note_bp
from config import Config
import init_db

app = create_app()
app.config.from_object(Config)

init_db.init_db(app)

app.register_blueprint(note_bp, url_prefix='/notes')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)