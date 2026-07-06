def soma_lista(numeros):
    """Retorna a soma de uma lista de números."""
    return sum(numeros)


def media_lista(numeros):
    """Calcula a média de uma lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
