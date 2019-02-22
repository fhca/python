__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

temperatura = 25  # grados
medio = np.zeros((100, 100))  # sin comida


class Bacteria:
    def __init__(self, localizacion, tamaño, nivel_de_prod_de_azucares, defensas, puede_contar=True):
        ancho, alto = medio.shape
        if 0 <= localizacion[0] < ancho and 0 <= localizacion[1] < alto:
            self.localizacion = localizacion
        else:
            self.localizacion = int(np.random.rand(1) * ancho), int(np.random.rand(1) * alto)
        self.tamaño = tamaño
        self.nivel_de_prod_de_azucares = nivel_de_prod_de_azucares
        self.defensas = defensas
        self.puede_contar = puede_contar

    # def mueve(self):


def gradiente(medio, cuanta_comida, temperatura):
    "cuanta_comida es un porcentaje de 'unos' iniciales en el medio."
    ancho, alto = medio.shape
    prob = np.random.rand(ancho * alto).reshape((ancho, alto))  # matriz de probabilidades para cada celda
    medio[prob < cuanta_comida] = 1  # solo aquellas celdas del medio cuya prob sea menor que 'cuanta_comida', serán uno
    # generando el gradiente
    pct = 0.99
    iteraciones = 200  # estos dos valores dependen de la temperatura
    for _ in range(iteraciones):  # que significa el guion bajo?
        medio = medio * pct  # disminuye globalmente en el pct
        for i in range(1, alto - 1):
            for j in range(1, ancho - 1):
                vde = medio[i, j]  # valor de enmedio
                medio[i + 1, j] += vde * (1 - pct) / 4  # cuanto le toca a cada vecino
                medio[i - 1, j] += vde * (1 - pct) / 4
                medio[i, j + 1] += vde * (1 - pct) / 4
                medio[i, j - 1] += vde * (1 - pct) / 4
        # condiciones en la frontera, un poco chafa, hay que mejorar esto
        medio[0, :] += 2 * (1 - pct) / 3
        medio[alto - 1, :] += 2 * (1 - pct) / 3
        medio[:, 0] += 2 * (1 - pct) / 3
        medio[:, ancho - 1] += 2 * (1 - pct) / 3
    return medio


medio = gradiente(medio, 0.03, 25)

plt.figure()
plt.imshow(medio, cmap=cm.Greys)
plt.show()
