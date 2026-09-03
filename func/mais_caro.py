from .data import data


def mais_caro():
    mais_caro = data[0]

    for produto in data:
        if produto["valor"] > mais_caro["valor"]:
            mais_caro = produto

    return mais_caro