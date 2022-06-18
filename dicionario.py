"""
Armazena conjuntos chave:valor
chaves sao unicas e imutaveis
"""
def dicionario():
    estados ={'AC': 'Acre', 'AL': 'Alagoas', "AP": "Amapá",
              "AM": "Amazonas", "BA": "Bahia", "CE": "Ceará",
              "DF": "Distrito Federal", "ES": "Espírito Santo",
              "GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso",
              "MS": "Mato Grosso do Sul", "MG": "Minas Gerais",
              "PA": "Pará", "PB": "Paraíba", "PR": "Paraná",
              "PE": "Pernambuco", "PI": "Piauí", "RJ": "Rio de Janeiro",
              "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul",
              "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina",
              "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"}
    siglas = sorted(estados.keys())
    print(siglas)
    print(estados['PR'])
    print(estados)
    
    estados["PR"] = 'Paranaué'
    print(estados)
    print("PR" in estados)
    del estados["PR"]
    print("PR" in estados) #retorna True ou False se está contido ou nao
    

dicionario()

