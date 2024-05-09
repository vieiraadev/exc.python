times = []
pontuacoes = {}

for i in range(4):
    time = input(f"Digite o nome do {i+1}º time de futebol: ")
    times.append(time)
    pontuacoes[time] = 0

for i in range(len(times)):
    for j in range(i + 1, len(times)):
        gols_a = int(input(f"Quantos gols o {times[i]} marcou contra o {times[j]}? "))
        gols_b = int(input(f"Quantos gols o {times[j]} marcou contra o {times[i]}? "))
        
        if gols_a > gols_b:
            pontos_time_i, pontos_time_j = 3, 0
        elif gols_a < gols_b:
            pontos_time_i, pontos_time_j = 0, 3
        else:
            pontos_time_i, pontos_time_j = 1, 1
        
        pontuacoes[times[i]] += pontos_time_i
        pontuacoes[times[j]] += pontos_time_j

pontuacoes_ordenadas = sorted(pontuacoes.items(), key=lambda x: x[1], reverse=True)
pontuacao_maxima = pontuacoes_ordenadas[0][1]
campeoes = [time for time, pontuacao in pontuacoes_ordenadas if pontuacao == pontuacao_maxima]

print("Times campeões:")
for campeao in campeoes:
    print(campeao)