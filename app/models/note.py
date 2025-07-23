from app.db import db
from datetime import datetime
import pytz
def horario_sao_paulo():
    return datetime.now(pytz.timezone("America/Sao_Paulo"))


class Note(db.Model):
    __tablename__ = 'Notes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    message = db.Column(db.String(2048), nullable=False)
    created_at = db.Column(db.DateTime, default=horario_sao_paulo, nullable=False)
    updated_at = db.Column(db.DateTime, default=horario_sao_paulo, nullable=False)
    deleted_at = db.Column(db.DateTime)
    # user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
            # "user_id": self.user_id
        }