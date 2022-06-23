class ObjetoContavel:
    contador = 0
    limite = 3

class ComentarioContavel(ObjetoContavel):
    def __init__(self, comentario):
        if (self.contador >= self.limite):
            raise Exception
        else:
            self.__class__.contador += 1 #Altera contador da classe mãe, no caso ObjetoContavel
        self.comentario = comentario

class PostagemContavel(ObjetoContavel):
    def __init__(self, postagem):
        if(self.contador >= self.limite):
            raise Exception
        else:
            self.__class__.contador += 1
        self.postagem = postagem

if __name__ == '__main__':
    postagem = PostagemContavel('Python é top')
    postagem2 = PostagemContavel('Python o filósofo')
    comentario = ComentarioContavel('Cobra venenosa')
    print(postagem.contador)
    print(PostagemContavel.contador)
    print(ComentarioContavel.contador)
    print(comentario.contador)

    postagem3 = PostagemContavel('sou a 3')
    ComentarioContavel.limite=4
    print(ComentarioContavel.limite)
    PostagemContavel.limite=4
    postagem4 = PostagemContavel('sou a 4')

class Receita:
    etapas = []
    def __init__(self, etapas=None):
        self.etapas.extend((etapas))

class Alimento(Receita):
    def __init__(self, etapas=None):
        super().__init__(etapas)

class Remedio(Receita):
    def __init__(self, etapas=None):
        super().__init__(etapas)

if __name__ == '__main__':
    panetone = Alimento(etapas=['assar em forno quente'])
    dipirona = Remedio(['adicionar corante'])
    print(panetone.etapas)
    print(dipirona.etapas)
    bolo = Alimento(['Cobertura de murango'])
    print(bolo.etapas)


#metodos estaticos
class Aluno:
    def __init__(self, nome):
        self.nome = nome

class Disciplina:
    limite_vagas = 20
    def __init__(self, nome):
        self.nome = nome
        self.total_matriculas=0
        self.matriculados = []

    def matricular(self, aluno):
        if self.verifica_vagas(self.total_matriculas,
                               self.limite_vagas):
            self.matriculados.append(aluno)
            self.total_matriculas += 1
        else:
            print("Turma já está cheia na disciplina {}".format(self.nome))

    @staticmethod
    def verifica_vagas(total_matriculas, limite_vagas):
        return limite_vagas > total_matriculas

if __name__ == '__main__':
    calculo = Disciplina(nome = 'Calculo')
    jose = Aluno('Jose')
    calculo.matricular(jose)
    print(calculo.verifica_vagas(19,20))
