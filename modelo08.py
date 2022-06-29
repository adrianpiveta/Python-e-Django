"""
Busca de expressões regulares
"""
import re

def verifica_cep(cep):
    #possui 5 caracteres no inicio, traço e 3 caracteres
    expressao = '\d{5}-\d{3}'
    # retorna true se retorna alguma coisa da compracão
    return re.match(expressao, cep) is not None

def verifica_horario(hora):
    expressao = '([01]\d|2[0-4]):[0-5]\d'
    return re.match(expressao, hora) is not None

def verifica_nome_identificador(identificador):
    expressao = '[a-zA-Z_][a-zA-Z0-9_]*'
    return re.match(expressao, identificador) is not None


if __name__ == '__main__':
    print(verifica_cep('87360-000'))
    print(verifica_cep('87360-999'))
    print(verifica_cep('8736r-999'))
    print(verifica_horario('24:00'))
    print(verifica_nome_identificador('Jose3_cavare9'))
    print(verifica_nome_identificador('cabar'))
