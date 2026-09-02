from .data import data


def listar_produtos():
    for produto in data:
        print("nome: " + produto["nome"])
        print("valor: " + str(produto["valor"]))
        print("estoque: " + str(produto["estoque"]))