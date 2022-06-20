"""
coleções sem ordem definida
sem repetição de elementos
suporta operações matematicas de conjuntos

"""
def conjunto():
    reais = {1.0, 2.0, 4.0, 8.0, 16.0, 160}
    inteiros = set([1,2,4,8,16, 32])
    print(reais)
    print(inteiros)
    print(4 in inteiros)
    print(4 in reais)
    print(inteiros - reais)
    print(reais - inteiros)
    print(reais | inteiros) #operação de numeros que estão em um ou outro conjuntos
    print(reais & inteiros) #numeros em ambos conjuntos
    print(reais ^ inteiros) #Numeros que fazem parte de somente um ou outro conjunto
    

if __name__=='__main__':
    conjunto()
