__author__ = 'fhca'


def crece_lista(lista=[]):
    lista += [1]
    return lista


def siguiente(n=0):
    n += 1
    return n


a = crece_lista()  # devuelve [1]
a = crece_lista()  # devuelve [1, 1]
a = crece_lista()  # devuelve [1, 1, 1]
print("a=", a)

b = crece_lista()  # devuelve [1, 1, 1, 1]
print("b=", b)

print("a=", a)  # devuelve [1, 1, 1, 1]

crece_lista()
crece_lista()
crece_lista()
crece_lista()
crece_lista()

print(a)
print(b)


a = siguiente()
print("a=", a)  # imprime 1

a = siguiente(siguiente())
print("a=", a)  # imprime 2

b = siguiente()
print("b=", b)  # imprime 1

b = siguiente()
print("b=", b)  # imprime 1

siguiente()
siguiente()
siguiente()
siguiente()
siguiente()
siguiente()

print(b)
