meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio",
    "Junho", "Julho", "Agosto", "Setembro", "Outubro",
    "Novembro", "Dezembro"
]
temperaturas = []
for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temp)
media_anual = sum(temperaturas) / len(temperaturas)
print(f"\nA média anual de temperatura é: {media_anual:.2f}°C")
print("\nMeses com temperatura acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"- {meses[i]}: {temperaturas[i]:.2f}°C")