def lista_quadrados(numeros):
    return [numero ** 2 for numero in numeros]


def lista_comprehension(numeros):
    return [numero * 2 for numero in numeros if numero % 2 == 0]


def filtra_strings(items):
    return [item.upper() for item in items if isinstance(item, str)]


def lista_ordenada(numeros):
    return sorted(numeros)
