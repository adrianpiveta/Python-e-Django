from urllib.request import urlopen
from json import loads

def consulta_cep(cep):
    url_template = 'https://viacep.com.br/ws/{cep}/json/'
    url = url_template.format(cep=cep)
    local_json = urlopen(url).read() #urlopen obtem da internet
    local_str = local_json.decode() # decode transforma em string
    local = loads(local_str)
    return local

#filtro de formatação de json
def formata_cep(local):
    return 'Endereço : {logradouro} - '\
            'Cidade: {localidade} = ' \
            'Estado: {uf}.'.format(**local)

if __name__ == '__main__':
    local = consulta_cep('87360000')
    ordenados = [item for item in sorted(local.items())]
    filtra_info = [item for item in ordenados
                   if 'info' not in item[0]]
    for campo in filtra_info:
        print(campo[0], campo[1])
    print(formata_cep(local))
