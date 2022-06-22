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
