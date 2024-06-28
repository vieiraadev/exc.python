tamanho_vetor = 10
caracteres = []
for i in range(tamanho_vetor):
    caractere = input(f"Digite o {i+1}º caractere: ")
    caracteres.append(caractere)
vogais = ['a', 'e', 'i', 'o', 'u']
contador_consoantes = 0
consoantes = []
for caractere in caracteres:
    if caractere.isalpha() and caractere.lower() not in vogais:
        contador_consoantes += 1
        consoantes.append(caractere)
print("\nConsoantes lidas:")
for consoante in consoantes:
    print(consoante)
print(f"\nForam lidas {contador_consoantes} consoantes.")