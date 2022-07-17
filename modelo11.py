from datetime import date
from modelo10 import conectar_banco, criar_cursor, criar_tabela_computador, executar_comando

def inserir_registro_computador(
        cursor, codigo, nome, aquisicao, vida, marca):
    comando = 'INSERT INTO computador( '\
              'codigo, nome, aquisicao, vida, marca' \
              ') Values (?, ?, ?, ?, ?)'
    parametros = (codigo, nome, aquisicao, vida, marca)
    executar_comando(cursor, comando, parametros)

def main():
    conexao = conectar_banco(':memory:')
    cursor = criar_cursor(conexao)
    criar_tabela_computador(cursor)
    inserir_registro_computador(cursor, 1, 'Vastra', date(2022,7,1), 365, 'acera')
    inserir_registro_computador(cursor, 2, 'Nitra', date(2020, 7, 1), 365, 'leveio')
    comando_sql = 'SELECT * FROM computador'
    registros = executar_comando(cursor, comando_sql)
    registro_unico = registros.fetchone()
    print('Registro Unico: \n ', registro_unico)
    print('OBJETO: ', registros)
    registro_unico = registros.fetchone()
    print(registro_unico)
    comando_sql = "UPDATE computador "\
                  " set vida = ? where codigo = ?"
    parametros = (600, 1)
    registros = executar_comando(cursor, comando_sql, parametros)
    print(registros.rowcount)
    parametros=(200, 2)
    registros =executar_comando(cursor, comando_sql, parametros)
    print(registros.rowcount)
    comando_sql = "SELECT * FROM computador"
    registros = executar_comando(cursor, comando_sql)
    for registro in registros:
        print(registro)
				print(registro.toString())



if __name__ == '__main__':
    main()


