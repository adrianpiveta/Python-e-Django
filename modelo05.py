"""
API de ceps

https://viacep.com.br/ws/04538133/json/
https://viacep.com.br/ws/22220000/json/
"""

import json
ceps = {"google_sp": {
 "cep": "04538-133",
 "logradouro": "Avenida Brigadeiro Faria Lima",
 "complemento": "de 3253 ao fim - lado ímpar",
 "bairro": "Itaim Bibi",
 "localidade": "São Paulo",
 "uf": "SP",
 "ibge": "3550308",
 "gia": "1004"
 }}
msf_brasil = {
 "cep": "22220-000",
 "logradouro": "Rua do Catete",
 "complemento": "até 195/196",
 "bairro": "Catete",
 "localidade": "Rio de Janeiro",
 "uf": "RJ",
 "ibge": "3304557",
 "gia": ""
}

def serializa(ceps):
    with open ('local.json', 'w') as arquivo:
        json.dump(ceps, arquivo)


#with lê e automaticamente fecha arquivo
def deserializa():
    with open('local.json') as arquivo:
        return json.load(arquivo)

if __name__ == '__main__':
    google_sp = json.dumps(ceps['google_sp'])
    print(google_sp)
    serializa(ceps)
    novo_ceps = deserializa()
    print('msf_brasil' in novo_ceps)
    ceps['msf_brasil'] = msf_brasil
    serializa(ceps)
    novos_ceps = (deserializa())
    print('msf_brasil' in novo_ceps)
    for local in novos_ceps:
        print(local)

    print(novos_ceps['msf_brasil']['logradouro'])
    print(novos_ceps['msf_brasil']['bairro'])
    print(novos_ceps['msf_brasil']['localidade'])
    print(novos_ceps['msf_brasil']['uf'])
    print(novos_ceps['msf_brasil']['complemento'])
    print(novos_ceps['msf_brasil']['erro'])