import random

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



