from .data import data


def buscar_produto(nome):
    resultado_busca = False
    for produto in data:
        if produto["nome"] == nome:
            resultado_busca = produto
    return resultado_busca