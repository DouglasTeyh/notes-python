from app.utils.functions import verify_string
from app.repository.notes_repository import NotesRepository
from app.exceptions.exceptions import NotaNaoEncontradaException
import datetime, pytz

class NotesController:

    @staticmethod
    def criar_nota(data: object):
        nota = data
        nota.message = verify_string(data.message, 'message')
        nota_criada = NotesRepository.criar_nota(nota)
        return nota_criada
    
    @staticmethod
    def buscar_nota_por_id(id_nota: int):
        nota = NotesRepository.buscar_nota_por_id(id_nota)
        if not nota:
            raise NotaNaoEncontradaException('Nota não encontrada no banco de dados')
        return nota

    @staticmethod
    def buscar_nota_por_usuario():
        pass

    @staticmethod
    def editar_nota(id_nota: int, data: object):
        nota = NotesController.buscar_nota_por_id(id_nota)
        if not nota:
            raise NotaNaoEncontradaException('Nota não encontrada no banco de dados')
        nota.title = data.title
        nota.message = verify_string(data.message, 'message')
        try:
            nota.updated_at = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
        except Exception as e:
            raise e('Erro ao atualizar horário de atualização da nota')
        return NotesRepository.editar_nota(nota)

    @staticmethod
    def excluir_nota(id_nota: int):
        nota_a_excluir = NotesController.buscar_nota_por_id(id_nota)
        
        return NotesRepository.excluir_nota(nota_a_excluir)
    