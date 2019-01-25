__author__ = 'fhca'


def potencia(base, exponente):
    """
    Eleva una base a un exponente dado.
    :param base: int
    :param exponente: int
    :return:
    """
    resultado = 1
    for cuenta in range(exponente):
        resultado *= base
    return resultado


print(potencia(2, 3))  # uso posicional de parámetros

print(potencia(base=2, exponente=3))  # uso nombrado de los parámetros

print(potencia(exponente=3, base=2))  # las posiciones se pueden alterar con parámetros nombrados


def nuevo_print(*cosas, fin='\n\n'):  # parámetro posicional múltiple y valor de default
    print("Muy buenas noches...", end=" ")
    print(*cosas, end=fin)


nuevo_print("Hola", "este", "es un", "nuevo", "print", fin=" ")
nuevo_print("y estas", "son algunas", "operaciones:", 2+3, 5*4)
nuevo_print("tan tan")


"""Pregúntenme a la próxima sobre parametros nombrados multiples."""
