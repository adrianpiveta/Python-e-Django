from datetime import datetime, timedelta

"""
Manipulação de datas em python
"""
def datas():
    data = datetime(2022,6,17,21,39,55)
    print(data)
    print(repr(data))
    print(type(data))
    print(data.year, data.month, data.day)
    print(data.hour, data.minute)
    print(data.strftime("%d/%m/%Y %H:%M:%S"))

def data_teste():
    return datetime(2010,3,20, 10,10,4)

def data_informada(dia, mes, ano):
    return datetime(ano, mes, dia)

def hoje(today = datetime.today):
    return today()

def agora(agora=datetime.now):
    return agora()

def diferenca():
    hoje=datetime(2022,11,14, 21,59,44, 875421)
    ontem = hoje - timedelta(days=1)
    amanha=hoje + timedelta(days=1)
    periodo_anterior = hoje - timedelta(hours=12)
    periodo_seguinte = hoje + timedelta(hours=12)
    print(ontem, amanha, periodo_anterior)

if __name__ == '__main__':
    #datas()
    print(data_informada(17, 6, 2022))
    print(hoje(data_teste))
    print(agora())
    diferenca()



    
    
    
