#open abre arquivo, retorna o objeto

def main():
    arquivo = open('texto.txt', 'r')
    conteudo = arquivo.read()
    print(conteudo)

    arquivo.seek(0)
    conteudo = arquivo.read()
    print(conteudo)

    arquivo.seek(0)
    autores = []
    for linha in arquivo:
        autor = linha.split('-')[0]
        autores.append((autor))
        print(linha, end=' ')
    print(autores)

    #sobrescrita
    saida = open('autores.txt', 'w')
    saida.write(autores[0])
    saida.close()

    #saida.readlines()
    #a é modo de append (adição)
    with open('autores.txt', 'a') as saida:
        for autor in autores[1:]:
            saida.write(autor)
    saida.closed





if __name__ == '__main__':
    main()