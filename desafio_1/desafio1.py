#!/usr/bin/env python3

menu = {
    1: {"nome": "Hamburguer", "preco": 15.00},
    2: {"nome": "Batata frita", "preco": 8.00},
    3: {"nome": "Refrigerante", "preco": 12.00},
    4: {"nome": "Milk-shake", "preco": 5.00},
}

pedido = []

def mostrar_menu():
    print("\n==== MENU DA LANCHONETE ====")
    print(" ID | ITEM               | PREÇO")
    print("-" * 30)
    for id_item, info in menu.items():
        print(f"{id_item:2} | {info['nome']:<15} | {info['preco']:6.2f}")
    print("Digite 0 ou sair para finalizar o pedido!")

def validar_id(id_str):
    if id_str.lower() == "sair":
        return 0

    try:
        id_item = int(id_str)
        if id_item == 0 or id_item in menu:
            return id_item
        else:
            print("ID inválido, insira um ID do menu!")
            return None

    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'sair'! ")
        return None
    
def validar_quantidade(qtd_str):
    try:
        qtd = int(qtd_str)
        if qtd >= 1:
            return qtd
        else:
            print("Quantidade deve ser pelo menos 1 item!")
            return None
        
    except ValueError:
        print("Entrada inválida. Digite um número inteiro!")
        return None
    
def adicionar_item(id_item, quantidade):
    item = menu[id_item]

    if id_item in [2, 3]:
        qtd_paga = (quantidade // 3) * 2 + (quantidade % 3)
        subtotal = qtd_paga * item['preco']

        if quantidade >= 3:
            print(f"Promoção: Compre 3, pague 2! Você pagará por {qtd_paga} unidades.")
    else:
        subtotal = quantidade * item['preco']
    pedido.append({
    "id": id_item,
    "nome": item['nome'], 
    "quantidade": quantidade,
    "preco_unitario": item['preco'],
    "subtotal": subtotal
    })

def mostrar_recibo():
    if not pedido:
        print("\nNenhum item no pedido!")
        return 
    
    print("\n=== Recibo ===")
    print("Item            | Qtd | Preço Unit. | Subtotal")
    print("-" * 45)
    total = 0

    for item in pedido:
        print(f"{item['nome']:<15} | {item['quantidade']:3} | R${item['preco_unitario']:9.2f} | R${item['subtotal']:7.2f}")
        total += item["subtotal"]
    print("-" * 45)
    print(f"Total: R${total:.2f}")

def main():
    while True:
        mostrar_menu()
        id_str = input("\nDigite o ID do item (ou sair): ")
        id_item = validar_id(id_str)
        
        if id_item == 0:
            break

        if id_item is None:
            continue
        qtd_str = input(f"Quantidade de {menu[id_item]['nome']}: ")
        quantidade = validar_quantidade(qtd_str)

        if quantidade is None:
            continue

        adicionar_item(id_item, quantidade)
        print(f"{quantidade} x {menu[id_item]['nome']} adicionado ao pedido!")

    mostrar_recibo()

if __name__ == "__main__":
    print("Bem vindo a Lanchonete!")
    main()