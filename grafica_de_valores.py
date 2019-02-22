__author__ = 'fhca'

import numpy as np
import matplotlib.pyplot as plt


def grafica(datos):
    plt.figure()  # muestra la ventana de dibujo

    # obtiene valores a graficar
    y = datos
    x = np.linspace(0, 1, len(datos))

    # hace el dibujo
    plt.plot(x, y, linewidth=.5)

    # lo muestra
    plt.show()


# grafica([5, 6, 12, 15, 17, 21, 23, 23, 23.5, 24, 25, 24, 23, 22, 18, 15, 10])

# grafica(np.random.rand(1000))

# grafica(np.random.randn(1000))

# grafica(np.random.randn(1000))

def grafica4(datos1, datos2, datos3, datos4):
    f = plt.figure()

    f.add_subplot(221)
    y = datos1
    x = np.arange(len(y))
    plt.plot(x, y, linewidth=.4)

    f.add_subplot(222)
    y = datos2
    x = np.arange(len(y))
    plt.plot(x, y, linewidth=.4)

    f.add_subplot(223)
    y = datos3
    x = np.arange(len(y))
    plt.plot(x, y, linewidth=.4)

    f.add_subplot(224)
    y = datos4
    x = np.arange(len(y))
    plt.plot(x, y, linewidth=.4)


grafica4(
    [5, 6, 12, 15, 17, 21, 23, 23, 23.5, 24, 25, 24, 23, 22, 18, 15, 10],
    np.random.rand(1000),
    np.random.randn(700),
    np.sin(np.arange(-2 * np.pi, 2 * np.pi, .1)))
