from init_db import db
from datetime import datetime
import pytz

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now(pytz.timezone("America/Sao_Paulo"), nullable=False))
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now(pytz.timezone("America/Sao_Paulo"), nullable=False))
    deleted_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
            "user_id": self.user_id
        }