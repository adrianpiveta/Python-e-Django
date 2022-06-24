class Material:
  def __init__(self, historico):
    self.historico = []
    self.__atualiza(historico)
  def atualiza(self, historico):
   for historia in historico:
    self.historico.append(historia)
  __atualiza = atualiza  # chama o metodo atualiza 

class Escritorio(Material):
 def atualiza(self, mapa):
  for item in mapa.items():
   self.historico.append(item)

if __name__ == '__main__':
 martelo = Material(['compra', 'uso', 'concerto'])
 print(martelo.historico)
 cartucho = Escritorio(['compra', 'descarte'])
 hist = cartucho.historico
 print(sorted(hist) == ['compra', 'descarte'])
 cartucho.atualiza({'recarga': 5, 'nivel': 2})
 hist = cartucho.historico
 print(sorted(hist, key=str))
