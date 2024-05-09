estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
while True:
    print("(:Cardápio(:")
    for item in cardapio:
        print(f"{item}: {', '.join(cardapio[item])}")
    print("================")
    print("O que deseja pedir (0 para sair)?")
    pedido = input().strip()
    if pedido == '0':
        print("Até logo!")
        break
    if pedido not in cardapio:
        print("Item não localizado no cardápio")
        continue
    ingredientes_faltando = []
    for ingrediente in cardapio[pedido]:
        if ingrediente not in estoque or estoque[ingrediente] <= 0:
            ingredientes_faltando.append(ingrediente)
    if ingredientes_faltando:
        for ingrediente in ingredientes_faltando:
            print(f"Infelizmente acabou o {ingrediente}")
    else:
        for ingrediente in cardapio[pedido]:
            estoque[ingrediente] -= 1
        print(f"Um {pedido} saindo no capricho!!!")