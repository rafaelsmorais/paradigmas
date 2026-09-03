#!/usr/bin/python

from func.cadastrar_produto import cadastrar_produto
from func.listar_produtos import listar_produtos
from func.buscar_produto import buscar_produto
from func.entrada_estoque import entrada_estoque
from func.saida_estoque import saida_estoque
from func.calcular_valor_estoque import calcular_valor_estoque

from func.maior_estoque import maior_estoque
from func.menor_estoque import menor_estoque
from func.mais_caro import mais_caro
from func.estoque_baixo import estoque_baixo

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
        print('7 - Produto com maior estoque')
        print('8 - Produto com menor estoque')
        print('9 - Produto mais caro')
        print('10 - Produtos com estoque baixo')
        print('0 - Sair')
        print()
        escolha = input('Digite sua opção: ')
        match escolha:
            case "1":
                nome = input('Digite o nome do produto: ')
                valor = input('Digite o valor do produto: ')
                estoque = input('Digite o estoque do produto: ')
                cadastrar_produto(nome, float(valor), int(estoque))
                print('Produto cadastrado com sucesso')
                print('\n\n')
            case "2":
                print("===== Produtos cadastrados: =====")
                listar_produtos()
                print('\n\n')
            case "3":
                produto = input('Digite o produto que deseja buscar: ')
                resultado_busca = buscar_produto(produto)
                print("===== Resultado da Busca =====")
                if resultado_busca:
                    print(resultado_busca)
                    print('\n\n')
                else:
                    print('Nenhum produto encontrado')
                    print('\n\n')
            case "4":
                nome = input('Digite o produto que deseja adicionar estoque: ')
                estoque = input('Digite o quantidade de estoque entrando: ')
                novo_estoque = entrada_estoque(nome, int(estoque))
                print("===== Novo Estoque =====")
                if novo_estoque:
                    print(novo_estoque)
                    print('\n\n')
                else:
                    print('Produto não encontrado')
                    print('\n\n') 
            case "5":
                nome = input('Digite o produto que deseja retirar estoque: ')
                estoque = input('Digite o quantidade de estoque saindo: ')
                novo_estoque = saida_estoque(nome, int(estoque))
                print("===== Novo Estoque =====")
                if novo_estoque:
                    print(novo_estoque)
                    print('\n\n')
                else:
                    print('Produto não encontrado')
                    print('\n\n') 
            case "6":
                total = calcular_valor_estoque()
                print(f"Valor total do estoque: R$ {total:.2f}")
                print('\n\n')
            case "7":
                produto = maior_estoque()

                print("===== Produto com maior estoque =====")
                print(produto)
                print('\n\n')
            case "8":
                produto = menor_estoque()

                print("===== Produto com menor estoque =====")
                print(produto)
                print('\n\n')
            case "9":
                produto = mais_caro()

                print("===== Produto mais caro =====")
                print(produto)
                print('\n\n')
            case "10":
                produtos = estoque_baixo()

                print("===== Produtos com estoque baixo =====")

                if produtos:
                    for produto in produtos:
                        print(produto)
                else:
                    print("Nenhum produto com estoque baixo")

                print('\n\n')
            case "0":
                continuar=False

main()