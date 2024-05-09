'''Criar um programa que efetua a soma de duas matrizes 3x3, sabendo
que a soma das matrizes 3x3 é uma nova matriz 3x3 onde cada elemento
é resultado da soma dos elementos das matrizes na mesma posição.
'''
matriz_3x3 = []
matriz1_3x3 = []
matriz2_3x3 = []
matriz_resultado = [[0 for _ in range(3)] for _ in range(3)] #lista das lista

print("Insira os valores para a primeira matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Elemento [{i + 1}, {j + 1}]: "))
        linha.append(valor)
    matriz_3x3.append(linha)
print("\nInsira os valores para a segunda matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Elemento [{i + 1}, {j + 1}]: "))
        linha.append(valor)
    matriz1_3x3.append(linha)
print("\nInsira os valores para a terceira matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Elemento [{i + 1}, {j + 1}]: "))
        linha.append(valor)
    matriz2_3x3.append(linha)
for i in range(3):
    for j in range(3):
        matriz_resultado[i][j] = matriz_3x3[i][j] + matriz1_3x3[i][j] + matriz2_3x3[i][j]
print("\nA matriz resultado da soma das três matrizes é:")
for i in range(3):
    for j in range(3):
        print(f"{matriz_resultado[i][j]:.2f}", end="\t")
    print()