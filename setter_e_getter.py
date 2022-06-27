class Computador():
    def __init__(self, codigo, nome, aquisicao, vida, marca):
        self.codigo = codigo
        self.nome = nome
        self.aquisicao = aquisicao
        self.vida = vida
        self.marca = marca

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        if(codigo > 0):
            self._codigo = codigo
        else:
            raise ValueError("Codigo precisa ser maior que 0 (zero)")

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        if vida < 0:
            raise ValueError("vida útil deve ser maior ou igual a 0")
        else:
            self._vida = vida

    def alerta_manutencao(self):
        pass

if __name__ == '__main__':
    acer = Computador(1, 'aspire', '24/06/2022', 600, 'asus')
    acer.codigo = 0
    acer.vida = 0

