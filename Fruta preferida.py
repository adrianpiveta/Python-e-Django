import random

def fruta_preferida():
    palpite, tentativas = "", 0
    frutas = ['maçã', 'melancia', 'pera', 'uva', 'melao']
    minha_preferida = random.choice(frutas)
    while (palpite!=minha_preferida):
        print(frutas)
        palpite = input("Adivinhe minha fruta preferida:  ")
        tentativas = tentativas+1
        if (palpite!=minha_preferida):
            print("Errou, vai tentar novamente!")
    print("esta é minha fruta do <3. "
          " numero de tentativas = {}".format(tentativas))

def fatiamento_string(variavel, inicio, fim):
    #primeiro elemento (inicio é incluido) e fim é omitido
    size = len(variavel)
    print(variavel[inicio:fim])

fatiamento_string('banana', 2,4)

def passo(palavra, passo):
    #percorre a palavra de acordo com o salto definido, que também pode ser negativo
    print(palavra[::passo])
    
    
    

