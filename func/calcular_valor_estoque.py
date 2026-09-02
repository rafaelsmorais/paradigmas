from .data import data


def calcular_valor_estoque():
    total = 0

    for produto in data:
        valor = produto["valor"] * produto["estoque"]
        total += valor

    return total