from ssl import SSLSession
from flask import Blueprint, jsonify, request
from app.models.model import Note
from datetime import datetime
from app import db

note_bp = Blueprint('note_bp', __name__)

@note_bp.route('/', methods=['GET'])
def buscar_notas():
    id =  SSLSession.get('id')

    if not id:
        return jsonify({'message': 'ID da nota não fornecido'}), 400

    if  id:
        nota = Note.query.filter_by(id=id).first()
        if nota:
            return jsonify(nota.to_dict()), 200
        else:
            return jsonify({'message': 'Nota não encontrada'}), 404
    
    return jsonify({'message': 'ID da nota não fornecido'}), 400

@note_bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    nota = Note.query.filter_by(id=note_id).first()
    
    if not nota:
        return jsonify({'message': 'Nota não encontrada'}), 404

    data = request.get_json()
    
    if 'message' in data:
        nota.message = data['message']
    
    nota.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify(nota.to_dict()), 200

@note_bp.route('/', methods=['POST'])
def adicionar_nota():
    data = request.get_json()

    message = data.get('message')
    user_id = data.get('user_id')

    if not message or not user_id:
        return jsonify({'message': 'Campos "message" e "user_id" são obrigatórios.'}), 400

    nova_nota = Note(message=message, user_id=user_id)
    db.session.add(nova_nota)
    db.session.commit()

    return jsonify(nova_nota.to_dict()), 201


@note_bp.route('/<int:note_id>', methods=['DELETE'])
def excluir_nota(note_id):
    nota = Note.query.filter_by(id=note_id, deleted_at=None).first()

    if not nota:
        return jsonify({'message': 'Nota não encontrada'}), 404

    nota.deleted_at = datetime.utcnow()
    db.session.commit()

    return jsonify({'message': 'Nota excluída com sucesso.'}), 200