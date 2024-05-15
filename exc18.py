votos = [0] * 7 
while True:
    try:
        print('1 - Windows Server \n 2 - Unix \n 3 - Linux\n 4 - Netware\n 5 - Mac IOS\n 6 - Outro')
        voto = int(input("Informe o seu voto (1-6) ou 0 para encerrar: "))
        if voto == 0:
            break
        if 1 <= voto <= 6:
            votos[voto] += 1
        else:
            print("Voto inválido. Por favor, insira um valor entre 1 e 6.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
total_votos = sum(votos)
if total_votos == 0:
    print("Nenhum voto foi registrado.")
else:
    sistemas_operacionais = ["", "Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
    print("\nSistema Operacional  Votos  %")
    print("-------------------  -----  ---")
    for i in range(1, 7):
        percentual = (votos[i] / total_votos) * 100
        print(f"{sistemas_operacionais[i]:<18} {votos[i]:>5}  {percentual:>3.0f}%")
    print("-------------------  -----")
    print(f"Total               {total_votos:>5}")
    vencedor_index = votos.index(max(votos[1:]))
    vencedor_nome = sistemas_operacionais[vencedor_index]
    vencedor_votos = votos[vencedor_index]
    vencedor_percentual = (vencedor_votos / total_votos) * 100
    print(f"\nO Sistema Operacional mais votado foi o {vencedor_nome}, com {vencedor_votos} votos, correspondendo a {vencedor_percentual:.0f}% dos votos.")