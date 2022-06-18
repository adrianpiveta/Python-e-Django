"""
Lista de estados
"""

def lista():
    estados = ['AC', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MS', 'MG', 'PR', 'PI',
               'RO', 'PI', 'PR', 'RO', 'RR', 'TO']
    print(estados[0])
    print(estados[-1])
    estados[-1] = estados[0]
    print(estados[-1])
    print("estados a partir da posicao 10: \n", estados[10:])
    print("Tamanho estados: ", len(estados))
    estados = estados +['SP', 'SE']
    
    estados.append('TO')
    print(estados)
    estados[-2:] =[]
    print(estados)
    vogais = ['a', 'e', 'i', 'o', 'u']
    numerais = [1, 2, 3, 4, 5]
    relacao = [vogais, numerais]
    print(relacao[0])
    print(relacao[0][3])
    vogais_maiusculas = [letra.upper() for letra in vogais]
    print(vogais_maiusculas)
    numerais_quadrados = [numero ** 2 for numero in numerais]
    print(numerais_quadrados)

if(__name__ == "__main__"):
    lista()
    
