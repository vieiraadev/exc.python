anos_luz = {
    "pc": 0.31,
    "al": 1,
    "ae": 63241.09,
    "ml": 525960.23,
    "sl": 31557600.0  
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
print("Lista de unidades de conversão:")
for i, unidade in enumerate(unidades):
    print(f"{i + 1}. {unidade}")
valor = float(input("Valor a ser convertido: "))
print("Escolha a unidade de origem:")
for i, unidade in enumerate(unidades):
    print(f"{i + 1}. {unidade}")
origem_index = int(input("Converter de (digite o número correspondente): ")) - 1
origem = unidades[origem_index].split("(")[1].split(")")[0]
print("Escolha a unidade de destino:")
for i, unidade in enumerate(unidades):
    print(f"{i + 1}. {unidade}")
destino_index = int(input("Converter para (digite o número correspondente): ")) - 1
destino = unidades[destino_index].split("(")[1].split(")")[0]
valor_convertido = valor * anos_luz[origem] / anos_luz[destino]
print(f"Conversão: {valor} {origem} = {valor_convertido} {destino}")