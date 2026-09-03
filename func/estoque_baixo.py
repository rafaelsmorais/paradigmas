from .data import data


def estoque_baixo():
    produtos_baixo = []

    for produto in data:
        if produto["estoque"] < 5:
            produtos_baixo.append(produto)

    return produtos_baixo