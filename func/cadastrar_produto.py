from .data import data


def cadastrar_produto(nome, valor, estoque):
    data.append({"nome": nome, "valor": valor, "estoque": estoque})