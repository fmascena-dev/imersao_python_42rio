#!/usr/bin/env python3


menu = { # => Dicionário que representa o menu da lanchonete.
    1: {"nome": "Hamburguer", "preco": 15.00},
    2: {"nome": "Batata frita", "preco": 8.00},
    3: {"nome": "Refrigerante", "preco": 12.00},
    4: {"nome": "Milk-shake", "preco": 5.00},
}


pedido = [] # => Lista que irá armazenar os itens pedidos pelo cliente.


def mostrar_menu(): # => Função que exibe o menu da lanchonete formatado.
    print("\n==== MENU DA LANCHONETE ====")
    print(" ID | ITEM               | PREÇO")
    print("-" * 30)
    for id_item, info in menu.items():
        print(f"{id_item:2} | {info['nome']:<15} | {info['preco']:6.2f}")
    print("Digite 0 ou sair para finalizar o pedido!")


def validar_id(id_str): # => Função para validar a entrada do usuário referente ao ID do item.
    if id_str.lower() == "sair":
        return 0  # => Permite que o usuário digite "sair" em vez de 0 para encerrar.

    try:
        id_item = int(id_str)
        if id_item == 0 or id_item in menu:
            return id_item  # => Retorna o ID se for válido (existe no menu ou é 0).
        else:
            print("ID inválido, insira um ID do menu!")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'sair'! ")
        return None


def validar_quantidade(qtd_str): # => Função para validar a quantidade de itens informada pelo usuário.
    try:
        qtd = int(qtd_str)
        if qtd >= 1: # => Verifica se a quantidade é válida (maior ou igual a 1).
            return qtd 
        else:
            print("Quantidade deve ser pelo menos 1 item!")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número inteiro!")
        return None

def adicionar_item(id_item, quantidade): # => Função para adicionar um item ao pedido.
    item = menu[id_item]  # => Recupera os dados do item a partir do ID.

    
    if id_item in [2, 3]: # => Aplica promoção "Leve 3, Pague 2" para Batata frita e Refrigerante.
        qtd_paga = (quantidade // 3) * 2 + (quantidade % 3)  # => Calcula a quantidade a ser paga.
        subtotal = qtd_paga * item['preco']  # => Subtotal com promoção.

        if quantidade >= 3:
            print(f"Promoção: Compre 3, pague 2! Você pagará por {qtd_paga} unidades.")
    else:
        subtotal = quantidade * item['preco']  # => Subtotal sem promoção.

    pedido.append({ # => Adiciona o item ao pedido.
        "id": id_item,
        "nome": item['nome'],
        "quantidade": quantidade,
        "preco_unitario": item['preco'],
        "subtotal": subtotal
    })

def mostrar_recibo(): # => Função para exibir o recibo final com todos os itens do pedido.
    if not pedido:
        print("\nNenhum item no pedido!")  # => Caso o pedido esteja vazio.
        return

    print("\n=== Recibo ===")
    print("Item            | Qtd | Preço Unit. | Subtotal")
    print("-" * 45)
    total = 0

    for item in pedido:
        print(f"{item['nome']:<15} | {item['quantidade']:3} | R${item['preco_unitario']:9.2f} | R${item['subtotal']:7.2f}")
        total += item["subtotal"]  # => Soma o subtotal de cada item ao total.

    print("-" * 45)
    print(f"Total: R${total:.2f}")  # => Exibe o total geral do pedido.

def main(): # => Função principal que controla o fluxo do programa.
    while True:
        mostrar_menu()
        id_str = input("\nDigite o ID do item (ou sair): ")
        id_item = validar_id(id_str)
        
        if id_item == 0:  # => Se o usuário quiser sair, encerra o loop.
            break

        if id_item is None:
            continue  # => Volta ao menu caso o ID seja inválido.

        qtd_str = input(f"Quantidade de {menu[id_item]['nome']}: ")
        quantidade = validar_quantidade(qtd_str)

        if quantidade is None:
            continue  # => Volta ao menu se a quantidade for inválida.

        adicionar_item(id_item, quantidade) # => Adiciona o item ao pedido.
        print(f"{quantidade} x {menu[id_item]['nome']} adicionado ao pedido!")

    mostrar_recibo() # => Exibe o recibo ao final do pedido.


if __name__ == "__main__": # => Ponto de entrada do script: executa a função main se este arquivo for executado diretamente.
    print("Bem vindo a Lanchonete!")
    main()
