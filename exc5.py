vetor1 = []
vetor2 = []
print("Digite os elementos do primeiro vetor:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor1.append(elemento)
print("\nDigite os elementos do segundo vetor:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor2.append(elemento)
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print("\nTerceiro vetor com elementos intercalados:")
print(vetor3)