# 🧾 Desafio 1 da Lanchonete

**Sistema simples de pedidos de lanches via terminal (linha de comando), feito em Python. Permite que o usuário selecione itens do menu, informe quantidades e veja um recibo detalhado ao final — com promoção "Leve 3, Pague 2" em itens selecionados!**

## 📋 Funcionalidades

- **Menu com 4 opções de produtos.**

- **Validação de entrada para IDs e quantidades.**

- **Promoção automática para Batata Frita e Refrigerante:**
    - ➡️ *Leve 3, pague apenas 2.*

- **Cálculo de subtotal por item e total geral.**

- **Geração de recibo com formatação limpa.**

### 📦 Itens do Menu
- ID | Item | Preço(R$)

- 1	| Hamburguer | 15.00
- 2	| Batata Frita | 8.00
- 3	| Refrigerante | 12.00
- 4	| Milk-shake | 5.00

### 🚀 Como executar

**Clone este repositório:**

```
git clone https://github.com/fmascena-dev/imersao_python_42rio/tree/main/desafio_1

```

### Execute o script:

```
python3 lanchonete.py
```

## 🧠 Exemplo de uso
```
Bem vindo a Lanchonete!

==== MENU DA LANCHONETE ====
 ID | ITEM               | PREÇO
------------------------------
 1  | Hamburguer        |  15.00
 2  | Batata frita      |   8.00
 3  | Refrigerante      |  12.00
 4  | Milk-shake        |   5.00
Digite 0 ou sair para finalizar o pedido!

Digite o ID do item (ou sair): 2
Quantidade de Batata frita: 3
Promoção: Compre 3, pague 2! Você pagará por 2 unidades.
3 x Batata frita adicionado ao pedido!

...

=== Recibo ===
Item            | Qtd | Preço Unit. | Subtotal
---------------------------------------------
Batata frita    |   3 | R$     8.00 | R$  16.00
Milk-shake      |   2 | R$     5.00 | R$  10.00
---------------------------------------------
Total: R$26.00
```

### 🔧 Requisitos

- **Python 3.6 ou superior**