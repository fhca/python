__author__ = 'fhca'

import numpy as np  # 'jala' la biblioteca numerica de python


def imprime_bonito(arreglo):
    ren, col = arreglo.shape
    for i in range(ren):
        for j in range(col):
            if arreglo[i, j] == '':
                arreglo[i, j] = ' '
            print(arreglo[i, j], end=' ')
        print()


# ------------------------------
pantalla = np.zeros((10, 10), dtype=str)  # matriz de cadenas vacías

"""
pantalla[0, 0] = '*'
pantalla[1, 1] = '*'
pantalla[2, 2] = '*'
pantalla[3, 3] = '*'
pantalla[4, 4] = '*'
pantalla[5, 5] = '*'
pantalla[6, 6] = '*'
pantalla[7, 7] = '*'
pantalla[8, 8] = '*'
pantalla[9, 9] = '*'
"""


def equis():
    for i in range(10):
        pantalla[i, i] = '*'
        pantalla[i, 9 - i] = '*'


def uno():
    for i in range(10):
        pantalla[i, 4] = '*'


def dos():
    for i in range(10):
        pantalla[0, i] = '*'  # 1er renglón
        pantalla[9, i] = '*'  # 2o renglón
        pantalla[4, i] = '*'  # 3er renglón
    for i in range(5):
        pantalla[i, 9] = '*'
        pantalla[i + 5, 0] = '*'


dos()

imprime_bonito(pantalla)
