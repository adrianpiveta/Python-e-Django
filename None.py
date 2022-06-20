"""
Fato de que none representa um tipo que não possui valor algum
"""
def nonet():
    print(None)

def printa(texto):
    if (texto):
        print(texto)
    else:
        print("Texto vazio")


resultado = printa('Vai chover')
print(resultado)
resultado = printa('')
print(resultado)
nonet()


