def verify_string(string:str, key:str):
    '''Verifica se a variável é do tipo string, é vazia e contém somente espaços'''
    
    if isinstance(string, str):
        if string == '': #Verifica se string é vazia
            raise ValueError(f'{key} não pode ser vazia')
        elif string.isspace(): #Verifica se string contem somente espaços
            raise ValueError(f'{key} não pode conter somente espaços')
        return string
