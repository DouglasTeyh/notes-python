from flask import Blueprint, jsonify, request
from app.models.note import Note
from app.controller.notes_controller import NotesController
from app.exceptions.exceptions import NotaNaoEncontradaException

note_bp = Blueprint('note_bp', __name__)

@note_bp.route('/<int:id_usuario>', methods=['POST'])
def adicionar_nota(id_usuario):
    data = request.get_json()
    
    try:
        nova_nota = NotesController.criar_nota(Note(message=data['message'])) # user_id=id_usuario
        return jsonify(nova_nota.to_dict()), 201
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except AttributeError as ae:
        return jsonify({'Error': str(ae)}), 400

@note_bp.route('/<int:id_nota>', methods=['GET'])
def buscar_nota_por_id(id_nota): 
    try:
        nota = NotesController.buscar_nota_por_id(id_nota)
        return jsonify(nota.to_dict()), 200
    except NotaNaoEncontradaException as nnee:
        return jsonify({'Error': str(nnee)}), 400
    except Exception as e:
        return jsonify({'Error': 'Erro desconhecido'}), 500

@note_bp.route('/<int:id_usuario>', methods=['GET'])
def buscar_nota_por_usuario(id_usuario): #A fazer

        nota = Note.query.filter_by(id=id).first()
        if nota:
            return jsonify(nota.to_dict()), 200
        else:
            return jsonify({'message': 'Nota não encontrada'}), 404
    
@note_bp.route('/<int:id_nota>', methods=['PUT'])
def editar_nota(id_nota):
    data = request.get_json()
    
    try:
        nota = NotesController.editar_nota(Note(id_nota, data['message']))
        return jsonify({nota.to_dict()}),200
    except NotaNaoEncontradaException as nnee:
        return jsonify({'Error': str(nnee)}), 400
    except ValueError as ve:
        return jsonify({'Error': str(ve)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 400

@note_bp.route('/<int:id_nota>', methods=['DELETE'])
def excluir_nota(id_nota):
    try:
        NotesController.excluir_nota(id_nota)
        return jsonify({'message': 'Nota excluída com sucesso.'}), 200
    except NotaNaoEncontradaException as nnee:
        return jsonify({'Error': str(nnee)}), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 400
