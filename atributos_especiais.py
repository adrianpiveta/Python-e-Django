
variavel_global = 5

def soma(a, b=5):
    """
    Soma 2 valores
    >>> soma(3,4)
    12
    """
    b = b+variavel_global
    return a+b

if __name__ == '__main__':
    print(soma.__code__)
    print(soma.__defaults__)
    soma.dicionario = 'irei para o __dict__.'
    print(soma.__dict__)
    print(soma.__doc__)
    print('variavel_global' in soma.__globals__)
    print(soma.__module__ == __name__)
    print(soma.__name__)




