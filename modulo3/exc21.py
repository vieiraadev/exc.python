perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]
respostas_positivas = 0
print("Responda com 'sim' ou 'não' às seguintes perguntas:")
for pergunta in perguntas:
    resposta = input(pergunta + " ").strip().lower()
    if resposta == "sim":
        respostas_positivas += 1
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"
print(f"\nClassificação: {classificacao}")