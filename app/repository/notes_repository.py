from app.db import db
from app.models.note import Note

class NotesRepository:
    
    @staticmethod
    def criar_nota(data: object):
        try:
            db.session.add(data)
            db.session.commit()
            return data
        except Exception as e:
            db.session.rollback() # Caso ocorra algum erro, desfaz a alteração no banco de dados.
            raise e
        
    @staticmethod
    def buscar_nota_por_id(id_nota: int):
        return Note.query.filter_by(id=id_nota).first()

    @staticmethod
    def editar_nota(data: object):
        try:
            db.session.add(data)
            db.session.commit()
            return data
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def excluir_nota(data: object):
        nota = Note.query.filter_by(id=data.id).first()
        try:
            db.session.delete(nota)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    