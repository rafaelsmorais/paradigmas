from .buscar_produto import buscar_produto


def saida_estoque(nome, estoque):
    produto = buscar_produto(nome)

    if not produto:
        return "Produto não encontrado"

    if produto["estoque"] < estoque:
        return "Estoque insuficiente"

    produto["estoque"] -= estoque
    return produto