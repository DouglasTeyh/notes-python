from functools import wraps #Garante que eu não modifique os dados da requisição 'f'
from flask import request, jsonify
import jwt

def login_required(f): # 'f' são todos os dados da requisição 
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization') #Pega o token enviado na requisição
        if not auth_header:
            return jsonify({'Error':'Token não enviado'}), 401
        auth_header = auth_header.replace('Bearer ', '') #Subistitui "Bearer" por espaço vazio
        payload = validate_token(auth_header) #Válida o token enviado na requisição
        if not payload:
            return jsonify({'Error':'Authentication required'}), 401
        request.user_email = payload.get('subject') #Pega o email enviado no token
        return f(*args, **kwargs)
    return decorated_function

def role_required(required_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({'Error':'Authentication required'}), 401
            
            auth_header = auth_header.replace('Bearer ', '')
            payload = validate_token(auth_header)
            if not payload:
                return jsonify({'Error':'Token inválido'}), 401

            user_role = payload.get('role')
            if user_role not in required_roles:
                return jsonify({'Error':'Permissão negada'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_token(token):
    try:
        payload = jwt.decode(token, 'NOTESFAP', algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError('Token expirado')
    except jwt.InvalidTokenError:
        raise ValueError('Token inválido')

def verify_string(string:str, key:str):
    '''Verifica se a variável é do tipo string, é vazia e contém somente espaços'''
    
    if isinstance(string, str):
        if isinstance(string, str):
            raise ValueError(f'{key} Valor deve ser do tipo string')
        elif string == '': #Verifica se string é vazia
            raise ValueError(f'{key} não pode ser vazia')
        elif string.isspace(): #Verifica se string contem somente espaços
            raise ValueError(f'{key} não pode conter somente espaços')
        return string
