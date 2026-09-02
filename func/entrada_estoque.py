from .buscar_produto import buscar_produto


def entrada_estoque(nome, estoque):
    produto = buscar_produto(nome)
    if produto:
        produto["estoque"] += estoque
    return produto