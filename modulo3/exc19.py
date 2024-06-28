NUM_JOGADORES = 23
votos = [0] * NUM_JOGADORES
while True:
    jogador = int(input("Número do jogador (0=fim): "))
    if jogador == 0:
        break
    elif jogador < 0 or jogador > NUM_JOGADORES:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        continue
    votos[jogador - 1] += 1
total_votos = sum(votos)
print("\nResultado da votação:")
print(f"Foram computados {total_votos} votos.")
print("{:<10} {:<5} {}".format("Jogador", "Votos", "%"))
for i, v in enumerate(votos):
    if v > 0:
        percentual = (v / total_votos) * 100 if total_votos > 0 else 0
        print("{:<10} {:<5} {:.1f}%".format(i + 1, v, percentual))
melhor_jogador = votos.index(max(votos)) + 1
percentual_melhor_jogador = (max(votos) / total_votos) * 100 if total_votos > 0 else 0

print(f"\nO melhor jogador foi o número {melhor_jogador}, com {max(votos)} votos, correspondendo a {percentual_melhor_jogador:.1f}% do total de votos.")