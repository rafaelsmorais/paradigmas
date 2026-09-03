from .data import data


def menor_estoque():
    menor = data[0]

    for produto in data:
        if produto["estoque"] < menor["estoque"]:
            menor = produto

    return menor