__author__ = 'fhca'


def siguiente(n=[0]):
    # ejemplo de uso estático de valores
    n[0] += 1
    return n[0]


print(siguiente())  # devuelve 1
print(siguiente())  # devuelve 2
print(siguiente())  # devuelve 3
print(siguiente())
print(siguiente())
print(siguiente())
print(siguiente())
print(siguiente())
