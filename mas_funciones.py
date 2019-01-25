__author__ = 'fhca'


def suma_hasta_v1(n):  # esta linea se llama "encabezado" de la función
    """
    Suma de los enteros 1, 2, 3,..., n.
    Versión recursiva.
    recursiva significa, que se llama a si misma en su cuerpo.
    """  # descripción de la función
    if n == 1:  # caso para detenerse
        return 1
    else:  # de lo contrario
        # aquí pones otras operaciones
        return n + suma_hasta_v1(n - 1)

#print(suma_hasta_v1(7))


def hace_frio(temperatura):
    print("Para una temperatura de", temperatura, end=" ")
    if temperatura < 16:
        print("Hace mucho frio!!!")
    elif temperatura < 25:
        print("Esta agradable!!!")
    else:
        print("Esto es un infierno!!!")

hace_frio(7)
# print("La temperatura es", temperatura)  # error: temperatura 'vive dentro de' hace_frio
hace_frio(16)
hace_frio(17)
hace_frio(25)
hace_frio(27)

hace_frio(temperatura=23)

# hace_frio(el_queso="ladra") # error: no sabe que hacer con el parámetro el_queso




