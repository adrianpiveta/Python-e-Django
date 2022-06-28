class Dobra:
    def __init__(self, numeros):
        self.indice = 0
        self.numeros = numeros
        self.tamanho = len(self.numeros)

    # retorna proprio objeto
    def __iter__(self):
        return self

    #implementa funcionamento do iterador
    def __next__(self):
        if(self.indice == self.tamanho):
            raise StopIteration

        proximo = self.numeros[self.indice] * 2
        self.indice += 1
        return proximo

if __name__ == '__main__':
    dobra = Dobra([1,2,4,8])
    for numero in dobra:
        print(numero)
    iterador = Dobra([4,8,12])
    for x in range(1,5):
        print(next(iterador))


