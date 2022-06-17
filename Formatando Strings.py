def formatando():
    texto = ('[]'.format('string test'))
    texto = ' formatando strings '
    print('{:<30}'.format(texto)) #alinhamento esquerda, pelo menos 30 caracteres
    print('{:>30}'.format(texto)) #Alinhamento 30 a direira
    print('{:^30}'.format(texto)) #centra
    print('{:*^30}'.format(texto)) #centra e se tiver menos de 30 caracteres, completa com *
    print('Alo, tô no {:-^30} !!!'.format(texto.lower())) #onde está {:*^30} espaço é substituido pelo txt (*)
    print('{0} é uma {1}'.format('Maçã', 'Fruta'.lower()))
    print('{0} bebe {1}, {0} é {2}'.format('gato', 'leite', 'felino'))
    print('idade -> {0}'.format(21)) #int
    print('idade -> {0:0>3d}'.format(21)) #alinhamento e largura D é modificador de inteiro
    print('Idade --> {0:x>3d}'.format(20)) #alinha á direita e preenche com x esquerda
    print('Idade --> {0:x<3d}'.format(20)) #alinha a esquerda, preenche com x direita
    print('Idade --> {0:x^10d}'.format(20)) 
    print("int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(20)) #modificadores que representam em outra base
    print("int: {0:d}; hex: {0:#X}; oct: {0:#o}; bin: {0:#b}".format(20))

    #ponto flutuante
    desconto = 0.15
    print('desconto= {:.2%}'.format(desconto)) # representa em percentual um numero
    preco=222
    print('preco: {:f}'.format(preco)) #float sem restrições 
    print('preco: {:.2f}'.format(preco)) # 2 casas decimais
    print('preco: {:+f}'.format(preco)) #sinal de + para positivo
    print("preco: {:+.2f}".format(preco)) # float com sinal positivo e qtd decimais controlada
    print("preco: {:7.2f}".format(preco)) #controlando espaço da casa inteira do float (minimo possivel)
    print("preco: {:+21.2f}".format(preco)) # descolamento minimo, qtd casas e sinal de +
    

formatando()

""" Função que faz algo
na vdd, isso é um teste de docstring
"""

def dobro(numero):
    """Retorna dobro do numero
    >>> dobro(6)
    12
    >>> dobro(7)
    14
    """
    return (numero * 2)

print(dobro.__doc__) #print de docstring

def triplo(numero):
    """Retorna triplo de um numero
    >>> triplo(3)
    9
    >>> triplo(9)
    27
    """
    return (3*numero)

#doctestes
"""Modulo exemplo
>>> dobro(3) + triplo(2)
12
>>> dobro(5) + triblo(5)
25
Quando o retorno é diferente do que se têm no docteste, ele retorna erro
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()

