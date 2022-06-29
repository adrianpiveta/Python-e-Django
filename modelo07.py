import glob
import sys

def list_dir(coringa):
    #glob retorna lista de nomes de acordo com um parametro
    return sorted(glob.glob(coringa))

def main(argumentos):
    if argumentos is None:
        argumentos = sys.argv
    if len(argumentos) < 2:
        msg = 'Numero invalido de argumentos'
        sys.stderr.write(msg)
        sys.exit(1)
    return list_dir(argumentos[1])

if __name__ == '__main__':
    print(list_dir('*.py'))
    print(list_dir('*.txt'))
    #print(main(['*.py']))
    print(main(['modelo07','*.py']))
