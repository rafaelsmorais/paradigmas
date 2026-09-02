#!/usr/bin/python

data = [{"nome": 'teclado logitech', "valor": 300.00, "estoque": 6 }, {"nome": 'mouse razer', "valor": 200.00, "estoque": 6 }]

def cadastrar_produto(nome, valor, estoque):
    data.append({"nome": nome, "valor": valor, "estoque": estoque})

def listar_produtos():
    for produto in data:
        print("nome: " + produto["nome"])
        print("valor: " + str(produto["valor"]))
        print("estoque: " + str(produto["estoque"]))

def buscar_produto(nome):
    resultado_busca = False
    for produto in data:
        if produto["nome"] == nome:
            resultado_busca = produto
    return resultado_busca

def entrada_estoque(nome, estoque):
    produto = buscar_produto(nome)
    if produto:
        produto["estoque"] += estoque
    return produto

def saida_estoque(nome, estoque):
    produto = buscar_produto(nome)

    if not produto:
        return "Produto não encontrado"

    if produto["estoque"] < estoque:
        return "Estoque insuficiente"

    produto["estoque"] -= estoque
    return produto
    
def calcular_valor_estoque():
    total = 0

    for produto in data:
        valor = produto["valor"] * produto["estoque"]
        total += valor

    return total

def mais_caro():
    mais_caro = {"valor": 0}
    for produto in data:
        if produto["valor"] > mais_caro["valor"]:
            mais_caro = produto
    print(mais_caro)

def main():
    continuar=True
    while(continuar):
        print('===== SISTEMA DE ESTOQUE =====')
        print('1 - Cadastrar produto')
        print('2 - Listar produtos')
        print('3 - Buscar produto')
        print('4 - Entrada de estoque')
        print('5 - Saída de estoque')
        print('6 - Mostrar valor total do estoque')
        print('0 - Sair')
        escolha = input('Digite sua opção: ')
        match escolha:
            case "1":
                nome = input('Digite o nome do produto: ')
                valor = input('Digite o valor do produto: ')
                estoque = input('Digite o estoque do produto: ')
                cadastrar_produto(nome, float(valor), int(estoque))
                print('Produto cadastrado com sucesso')
            case "2":
                print("===== Produtos cadastrados: =====")
                listar_produtos()
            case "3":
                produto = input('Digite o produto que deseja buscar: ')
                resultado_busca = buscar_produto(produto)
                print("===== Resultado da Busca =====")
                if resultado_busca:
                    print(resultado_busca)
                else:
                    print('Nenhum produto encontrado')
            case "4":
                nome = input('Digite o produto que deseja adicionar estoque: ')
                estoque = input('Digite o quantiade de estoque entrando: ')
                novo_estoque = entrada_estoque(nome, int(estoque))
                print("===== Novo Estoque =====")
                if novo_estoque:
                    print(novo_estoque)
                else:
                    print('Produto não encontrado') 
            case "5":
                nome = input('Digite o produto que deseja retirar estoque: ')
                estoque = input('Digite o quantiade de estoque saindo: ')
                novo_estoque = saida_estoque(nome, int(estoque))
                print("===== Novo Estoque =====")
                if novo_estoque:
                    print(novo_estoque)
                else:
                    print('Produto não encontrado') 
            case "6":
                total = calcular_valor_estoque()
                print(f"Valor total do estoque: R$ {total:.2f}")
            case "0":
                continuar=False

main()