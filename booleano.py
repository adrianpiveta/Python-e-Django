"""
verdade ou mentira
"""
def boolean():
    print(bool(''))
    print(bool('A')) #Strings com qualquer conteudo sao verdadeiras
    print(bool(0)) #0 é falso
    print(bool(1)) #diferente de 0 é verdadeiro
    print(bool([False])) #Listas, dicionários, tuplas com algum conteudo são verdadeiras
    print(bool(set())) #Com conjuntos, acontece a mesma coisa, se não tiverem conteudo, falso


if __name__ == '__main__':
    boolean()
