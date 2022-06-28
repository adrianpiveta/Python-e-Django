def dobra(numeros):
    for numero in numeros:
        yield numero * 2
        #yield retorna o numero calculado

if __name__ == '__main__':
    for numero in dobra([3,4,5]):
        print(numero)

gerador = dobra([3,4,9])
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))