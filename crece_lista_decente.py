__author__ = 'fhca'

def crece_lista_decente(lista=None):
    if lista is None:
        lista = [1]
    else:
        lista += [1]
    return lista


a = crece_lista_decente()
print(a)  # devuelve [1]

a = crece_lista_decente(a)
print(a)  # devuelve [1, 1]

b = crece_lista_decente()
print(b)  # devuelve [1]

b = crece_lista_decente(b)
print(b)  # devuelve [1, 1]

print("a=", a)
