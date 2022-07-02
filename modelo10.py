#importação e manipulação sqlite
import sqlite3
from datetime import date

def conectar_banco(nome_bd):
    return sqlite3.connect(nome_bd)

#cursor é estrutura de controle, uma área de memoria que permite manipular objeto do banco
def criar_cursor(conexao):
    return conexao.cursor()

def criar_tabela_computador(cursor):
    comando = 'CREATE TABLE IF NOT EXISTS' \
              ' computador ( '\
              '         codigo INTEGER PRIMARY KEY,'\
              '         nome VARCHAR, '\
              '         aquisicao DATE,  '\
              '         vida INTEGER, ' \
              '         marca VARCHAR'\
              '        )'
    executar_comando(cursor, comando)

def executar_comando(cursor, comando, parametros=None):
    if parametros:
        cursor.execute(comando, parametros)
    else:
        cursor.execute(comando)
    return cursor

if __name__ == '__main__':
    conexao = conectar_banco(':memory:') #cria na RAM
    print(type(conexao))
    print(conexao)
    cursor = criar_cursor(conexao)
    print(type(cursor))
    print(cursor)
    criar_tabela_computador(cursor)