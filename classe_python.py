#modelo de classe
class computador():
    """
    Esta classe representa um computador, associado a marca e com componentes agregados
    """
    def __init__(self, codigo, nome, aquisicao, vida, marca):
        self.codigo = codigo
        self.nome = nome
        self.aquisicao = aquisicao
        self.vida = vida
        self.marca = marca

    def alerta_manutencao(self):
        # TODO: calcula período de manutenção
        pass

class Marca():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

if __name__ == '__main__':
    dell = Marca(1, 'DELL')
    hp = Marca(2, 'HP')

    monstro = computador(1, 'Monstro', '14/06/2022', 830, dell)
    monstro2 = computador(2, 'Monstro HP', '14/06/2022', 830, hp)

    print(type(dell))
    print(type(hp))
    print(type(monstro))
    print(isinstance(dell, Marca))
    print(isinstance(monstro2, Marca))
    print(isinstance(monstro, computador))


"""
Métodos são instancias das classes na qual se faz uma interação da classe
"""
class Aluno():
    def __init__(self, nome, matricula):
        self.matricula = matricula
        self.nome = nome
        self.livros = []
    def empresta_livro(self, livro):
        self.livros.append(livro)

if __name__ == '__main__':
    print(type(Aluno.empresta_livro))
    jorge = Aluno(nome='Jorge', matricula=12321)
    print(type(jorge))
    print(type(jorge.empresta_livro))
    Aluno.empresta_livro(jorge, 'Introducao ao calculo')
    jorge.empresta_livro('pedagogia do oprimido')
    print(jorge.livros)

class Produto():
    def __init__(self, nome, imposto, custo):
        self.nome = nome
        self.imposto = imposto
        self.custo = custo
    def preco(self, quantidade):
        return (self.custo * quantidade + self.custo * self.imposto * quantidade)

class Alimento(Produto):
    def __init__(self, nome, imposto, custo, validade):
        super().__init__(nome, imposto,custo)
        self.validade = validade

class Roupa(Produto):
    def __init__(self, nome, imposto, custo, tamanho):
        super().__init__(nome,imposto, custo)
        self.tamanho = tamanho

if __name__ == '__main__':
    produto_generico = Produto(nome='generico', imposto=0.1, custo=10)
    roupa_teste = Roupa(produto_generico, imposto=0.1,  custo=100, tamanho=44)
    camiseta = Roupa(nome='camiseta', tamanho=44, imposto=0.1, custo=10)
    churros = Alimento(nome='churros doce de leite', imposto=.3, custo=1, validade='28/06/2022')
    print(camiseta.nome)
    print(camiseta.preco(10))





