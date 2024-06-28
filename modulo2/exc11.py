pontos = int(input("digite a quantidade de pontos para vencer o jogo: "))
jogador_num_1 = 0
jogador_num_2 = 0
while jogador_num_1 > pontos and jogador_num_2 > pontos: 
 print("\nPontos: Jogador 1 -", jogador_num_1, "Jogador 2 -", jogador_num_2)
print("ESCOLHA PEDRA, PAPEL, TESOURA: ")
jogador1_escolha = (input("Escolha JOGADOR 1:"))
jogador2_escolha = (input("Escolha JOGADOR 2:"))

if jogador1_escolha == jogador2_escolha:
        print("EMPATE!!")
elif (jogador1_escolha == 'PEDRA' and jogador2_escolha == 'TESOURA') or \
         (jogador1_escolha == 'TESOURA' and jogador2_escolha == 'PAPEL') or \
         (jogador1_escolha == 'PAPEL' and jogador2_escolha == 'PEDRA'):
        print("JOGADOR 1 GANHOU")
        jogador_num_1 += 1
elif (jogador2_escolha == 'PEDRA' and jogador1_escolha == 'TESOURA') or \
         (jogador2_escolha == 'TESOURA' and jogador1_escolha == 'PAPEL') or \
         (jogador2_escolha == 'PAPEL' and jogador1_escolha == 'PEDRA'):
        print("JOGADOR 2 GANHOU!!")
        jogador_num_2 += 1