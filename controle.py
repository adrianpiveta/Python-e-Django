"""
Estruturas que definem o fluxo do programa

if - elif - else: é semelhante ao switch case
"""
def comando_if():
    numero  = int(input("Digite um numero entre 1 e 10: "))
    if numero < 1:
        print("Numero deve ser maior ou igual a 1")
    elif numero > 10:
        print("Numero deve ser menor ou igual a 10")
    else:
        print("O Quadrado é: ", numero ** 2)

#comando_if()


"""
Laço while se executa enquanto a condição for tida como verdade
e pode ter um else, que execulta quando o laço parar
"""
def comando_while():
    teste = True
    while teste:
        teste = input('Digite algo. Pressione <ENTER> para sair.')
    else:
        print('Vazei do while')

#comando_while()

def mensagem():
    texto = True
    while texto:
        texto = input('Digite algo, digite break para sair')
        if(texto=='break'):
            break
        else:
            continue # recomeça mais uma exec do laço
        #Aqui nunca será executado devido break e continue
        print('Esquecido')
    else:
        print('Saí do laço')

#mensagem()

"""
Laço for, percorre uma sequencia
possui clausula else
"""
def laco_for():
    doces=['churros', 'gelatina', 'paçoca']
    for x in doces:
        print(x)

    palavra='azeitona'
    for letra in palavra:
        print(letra)
    else:
        print('executei o else')

    for letra in palavra:
        if letra=='e':
            continue
        if letra=='t':
            break
        print(letra)

laco_for()

    
    
