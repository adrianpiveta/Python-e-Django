class StringInteiro(str):

    def __new__(cls, str_inteiro):
        valor = int(str_inteiro)
        return super(StringInteiro, cls).__new__(cls, str_inteiro)

    def __init__(self, str_inteiro):
        return super(StringInteiro, self).__init__()

    def __repr__(self):
        return '{}({})'.format('StringInteiro', self)

    def __str__(self):
        return self

    def __lt__(self, other):
        return int(self) < int(other)

    def __add__(self, other):
        return str(int(self) + int(other))

if __name__ == '__main__':
    string10=StringInteiro('10')
    string2 = StringInteiro('2')

    print(repr(string2))
    print(eval(repr(string10)))
    print(string10)
    print(string10 < string2)
    print('10' < '2')
    print(10 < 2)
    print(string10 + string2)

