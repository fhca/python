__author__ = 'fhca'


def incrementa(lista=[0, 0, 0, 0, 0]):
    resultado = list()
    for elemento in lista:
        resultado.append(elemento + 1)
    lista[0] += 1
    lista[2] += 1
    return resultado


a = [1, 2, 3, 4, 5, 6]
b = incrementa()

print(b)
"""
blah blah
"""
c = incrementa()
print(c)

d = incrementa()
print(d)