__author__ = 'fhca'

import math


def n_primos(n):
    respuesta = [2]
    x = 3
    for i in range(n):
        encontrado = False
        while not encontrado:
            encontrado = True
            for j in range(3, int(math.sqrt(x)+1), 1):
                if x % j == 0:
                    encontrado = False
                    break
            if encontrado:
                respuesta.append(x)
            x += 2
    return respuesta

def primos_menores_que(n):
    respuesta = [2]
    for x in range(3, n, 2):
        encontrado = True
        for j in range(3, int(math.sqrt(x)+1), 1):
            if x % j == 0:
                encontrado = False
                break
        if encontrado:
            respuesta.append(x)
    return respuesta

def f(x):
    "# de dígitos de x."
    return int(math.log(x)/math.log(10))+1

def d(n, x):
    "dígito n-esimo de x."
    return int((x % 10**n - x % 10**(n-1))/10**(n-1))

def d2(n, x):
    "dígito n-esimo de x."
    return int((x % 10**n - x % 10**(n-2))/10**(n-2))

def mas_significativo(x):
    return d(f(x), x)

def menos_significativo(x):
    return d(1, x)

def mas_significativo2(x):
    return d2(f(x), x)

#primos_menores_que(10000)

#x = 1234567
#print(d(f(x), x))  # dígito más significativo de x
#print(d(1, x)) # dígito menos significativo

p= n_primos(100)
print(p)

p = primos_menores_que(1000000)
print(p)

#print(list(map(menos_significativo, p)))
#print(list(map(mas_significativo, p)))

# zipf de mas significativo
#import matplotlib.pyplot as plt
#plt.hist(list(map(mas_significativo, p)), bins=9)
#plt.show()

#p=p[4:]
#print(p)
#print(list(map(mas_significativo2, p)))

#plt.hist(list(map(mas_significativo2, p)), bins=90)
#plt.show()

