class PrimoInvalido(Exception):
    pass

def primo1(numero):
    if numero <=0:
        raise PrimoInvalido
    if numero == 1:
        return False
    if numero == 2:
        return True
    for valor in range(2, numero, 1):
        if(numero % valor) == 0:
            return False
    return True

def primo2(numero):
    if numero <=0:
        raise PrimoInvalido
    if numero == 1:
        return False
    if numero == 2:
        return True
    if (numero % 2) == 0:
        return False
    for valor in range(3, numero // 2, 2):
        if (numero % valor) == 0:
            return False
    return True

if __name__ == '__main__':
    #print(primo1(0))
    print(primo1(1))
    print(primo1(2))
    print(primo1(4))
    print(primo1(5))
    #print(primo2(0))
    print(primo2(1))
    print(primo2(2))
    print(primo2(4))
    print(primo2(5))
        
            
