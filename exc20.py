while True:
    nome_atleta = input("Nome do atleta: ")
    if nome_atleta == "":
        break
    
    saltos = []
    for i in range(1, 6):
        salto = float(input(f"{i}º Salto: "))
        saltos.append(salto)
    
    media_saltos = sum(saltos) / len(saltos)
    
    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media_saltos:.1f} m\n")