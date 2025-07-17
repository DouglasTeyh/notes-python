from ssl import SSLSession
from flask import Blueprint, jsonify, request
from app.models.model import Note

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