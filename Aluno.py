class Aluno:
    def __init__(self, codigo=0, nome='', media=0):
        self.codigo = codigo
        self.nome = nome
        self.media = media

    def situacao(self):
        if self.media < 4:
            return 'reprovado'
        elif self.media < 7:
            return "recuperação"
        else:
            return "aprovado"

if __name__ == '__main__':
    alunos = [ Aluno(1, 'zé', 4),
               Aluno(2, 'João', 6),
               Aluno(3, 'Gabriel', 4),
               Aluno(4, 'Stella', 8)]
    codigos = (aluno.codigo for aluno in alunos) #cria uma vetor de codigo de alunos percorrendo lista alunos
    print(type(codigos))
    situacoes = (aluno.situacao() for aluno in alunos) #isso é generator
    print(type(situacoes))
    print('situacoes', situacoes)
    resultados ={cod: sit for cod, sit in zip(codigos, situacoes)}
    #transforma resultados em dicionarios
    print(resultados)
