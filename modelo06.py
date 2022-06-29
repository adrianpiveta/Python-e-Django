import os
import shutil
from random import shuffle

def main():
   #os.mkdir('pasta_criada')
   #os.chdir('pasta_criada')
   print(os.getcwd())
   #gera_conteudo('arquivo.txt')
   #os.mkdir('sub_diretorio_n2')
   #gera_conteudo('sub_diretorio_n2/arquivo1.txt')
   #gera_conteudo('sub diretorio n2/arquivo1.txt')
   #os.mkdir('sub_diretorio_n2/sub_dir1_n3')
   #gera_conteudo('sub_diretorio_n2/sub_dir1_n3/arquivo2.txt')
   """
   os.walk opercorre diretorio e para cada diretorio encontrado, retorna 
   mp,e doretprop percorrido, subdiretorios e nomes de arquivos
   """
   for topo, dirs, arqs in os.walk('sub_diretorio_n2'):
       print(topo, dirs, arqs)
   #os.rmdir('sub_diretorio_n2/sub_dir1_n3')


   shutil.rmtree('sub_diretorio_n2') #remove a arvore sem reclamar, apaga arquivos e pastas
   os.chdir('..')

def gera_conteudo(nome_arquivo):
    numeros = list(range(70))
    numeros =[str(numero) for numero in numeros]
    with open(nome_arquivo, 'w') as arquivo:
        for indice in range (30):
            shuffle(numeros)
            arquivo.write(''.join(numeros))


main()
if __name__ == '__main__':
    main()