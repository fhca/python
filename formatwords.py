__author__ = 'fhca'


def formatWords1(lista):
    """Dada una lista de cadenas, crear una sola cadena compuesta de juntar
    cada cadena de la lista, separadas por comas salvo la última cadena que
    está separada por 'y'. Omitir cadenas vacías. La lista vacía devuelve
    una cadena vacía. Ejs.

    formatWords(['Jesús', 'Alejandra', 'Arturo']) =>
        'Jesús, Alejandra y Arturo'
    formatWords(['Jesús', 'Alejandra']) =>
        'Jesús y Alejandra'
    formatWords(['Jesús']) =>
        'Jesús'
    formatWords([]) =>
        ''

    +
    len(lista)  => # de elementos de la lista
    "separador".join(lista)  => une las cadenas de la lista con el separador
    """
    if len(lista) > 1:
        return ", ".join(lista[:-1]) + ' y ' + lista[-1]
    else:
        return "".join(lista)


def formatWords2(lista):
    return " y ".join([", ".join(lista[:-1]), lista[-1]]) if len(lista) > 1 \
        else "".join(lista)


def formatWords3(lista):
    longitud = len(lista)
    separador = ', '
    if longitud >= 1:
        resultado = lista[0]
    else:
        resultado = ''
    for i in range(1, longitud):
        if i == longitud - 1:
            separador = ' y '
        resultado = resultado + separador + lista[i]
    return resultado


def formatWords(lista):
    longitud = len(lista)
    separador = ', '
    if longitud >= 1:
        resultado = [lista[0]]
    else:
        resultado = ['']
    for i in range(1, longitud):
        if i == longitud - 1:
            separador = ' y '
        resultado.append(separador + lista[i])  # un poco más rapida que la anterior
    return "".join(resultado)


print(formatWords(['1', '2', '3', '4', '5', '6']))
print(formatWords(['Jesús', 'Alejandra', 'Arturo']))
print(formatWords(['Jesús', 'Alejandra']))
print(formatWords(['Jesús']))
print("'" + formatWords([]) + "'")
