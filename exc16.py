modelos = ["fusca", "gol", "uno", "Vectra", "Peugeout"]
consumos = [7, 10, 12.5, 9, 14.5]
preco_gasolina = 2.25
print("Comparativo de Consumo de Combustível")
for i in range(len(modelos)):
    print(f"Veículo {i + 1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {consumos[i]}")
print("\nRelatório Final")
menor_consumo = float('inf')
modelo_mais_economico = ""
for i in range(len(modelos)):
    litros_necessarios = 1000 / consumos[i]
    custo = litros_necessarios * preco_gasolina
    print(f"{i + 1} - {modelos[i]} - {consumos[i]:.1f} - {litros_necessarios:.1f} litros - R$ {custo:.2f}")
    if litros_necessarios < menor_consumo:
        menor_consumo = litros_necessarios
        modelo_mais_economico = modelos[i]
print(f"\nO menor consumo é do {modelo_mais_economico}")