__author__ = 'fhca'

"""
INSTRUCCIONES:
    A partir de dos cadenas de diferente longitud (cad1 y cad2), crear una nueva cadena
    de la forma corta-larga-corta, es decir, determinar la cadena mas corta y ponerla
    antes y después de la cadena más larga.
    Ej.
    
    solution("1", "22")  => "1221"
    solution("22", "1")  => "1221"
    
    la más corta puede ser vacía.
"""


def solution(cad1, cad2):
    "Asume que son de diferente tamaño."
    "len(cad) => tamaño de la cad."
    "len('Felipe') => 6"
    "len('Claudia') => 7"
    " 'papa'+'lote' => 'papalote'  "
    if len(cad1) > len(cad2):
        corta = cad2
        larga = cad1
    else:
        corta = cad1
        larga = cad2
    return corta + larga + corta


print(solution("1", "22"))
print(solution("22", "1"))
print(solution("Felipe", "Claudia"))
print(solution("Jesús", "Alejandra"))
print(solution("blanco", ""))


def solution2(cad1, cad2):
    if len(cad1) > len(cad2):
        return cad2 + cad1 + cad2
    else:
        return cad1 + cad2 + cad1


print(solution2("1", "22"))
print(solution2("22", "1"))
print(solution2("Felipe", "Claudia"))
print(solution2("Jesús", "Alejandra"))
print(solution2("blanco", ""))

