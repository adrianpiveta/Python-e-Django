def funcao_soma(numero, numero2):
    """
    Soma 2 numeros e retorna-os
    """
    soma = numero + numero2
    return soma

def imprime(valor):
    print(valor)


imprime(funcao_soma(10,8))

#funcao help imprime docstring
help(funcao_soma)

def funcao_passagem(base, expoente=2): #assim se define um padrão quando iguala valor
    resultado = base ** expoente
    return resultado

def somatorio(*args):  # o * define como tupla, que pode receber numero indefinido de parametros
    resultado = 0
    print(args)
    for numero in args:
        resultado +=numero
    return resultado

def itens():
    item = {'calca': 1}
    compras_c1 = lista_compras(item)
    print(compras_c1)
    item = {'camiseta': 1}
    compras_c2 = lista_compras(item)
    print(compras_c2)

def lista_compras(item, compras=None):
    if compras is None:
        compras =[]
    compras.append(item)
    return compras

def lista_compras(*args, valores=None):
    if valores is None:
        valores = []
    for item in args:
        valores.append(item)
    return valores

elementos =[9,7,8]
print(lista_compras(1,2,4,3, valores=elementos)) #com *args se necessita passar outros argumentos de forma explicita
imprime(funcao_passagem(3,4))
imprime(funcao_passagem(4))
print(somatorio(5,7,9,5,4,2))

def listar_musica(
        nome, genero='Rock',
        subgenero='Classico', artista='Led Zeppelin'):
    print('Nome ', nome, ', Genero: ', genero, ' ,subgenero: ', subgenero, ' artista: ', artista)

listar_musica('Stairway to heaven')
listar_musica(artista=' Michael Jackson', nome='Thriller')

def montar_pizza(nome, *args, **kwargs):
    print('Pizza: ',nome)
    print('Ingredientes: ', end='')
    for ingrediente in args:
        print(ingrediente, ' ', end='')
    print()
    print(20*'-')
    print('Opicionais: ', end='')
    chaves = sorted(kwargs.keys())
    for chave in chaves:
        print(chave, '=', kwargs[chave], ' ', end='')
    print()

montar_pizza('Portuguesa', 'cebola', 'mussarela', 'pimenta', borda='chedar', adicional='bacon')
ingredientes=('queijo', 'presunto', 'orégano', 'pimenta')
adicionais={'borda':'parlmito',
            'ponto':'Bem passado'}
montar_pizza('portuguesa', *ingredientes, **adicionais)

def escopo_var():
    variavel_global ='sou global'
    print(variavel_global)
    def escopo_nLocal():
        variavel_nao_local = 'náo sou local'
        print(variavel_nao_local, variavel_global)
        def escopo_local():
            variavel_local='sou local'
            print(variavel_local, variavel_nao_local, variavel_global)

        escopo_local()
    escopo_nLocal()


escopo_var()