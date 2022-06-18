"""
truplas armazenam sequencias, são imutaveis

"""

def truplas():
    coordenada=(2,1)
    trupla=(32,21)
    print(trupla)
    print(trupla[1])
    vazia=()
    unica = (3,) #necessita de virgula para indicar tupla
    x, y = coordenada #cada elemento recebe um dos valores
    print(x)
    print(y)
    tupla_vazia = tuple()
    print(tupla_vazia)


if(__name__ == '__main__'):
    truplas()
