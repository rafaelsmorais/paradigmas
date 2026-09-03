from .data import data


def maior_estoque():
    maior = data[0]

    for produto in data:
        if produto["estoque"] > maior["estoque"]:
            maior = produto

    return maior