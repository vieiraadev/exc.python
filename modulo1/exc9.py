numero_binario = input("Digite um número em binário: ")
numero_decimal = 0
tamanho = len(numero_binario)
for i in range(tamanho):
    digito = numero_binario[tamanho - 1 - i]  
    if digito == '1':
        valor_decimal_digito = 2 ** i
        numero_decimal += valor_decimal_digito
print(f"O valor decimal de {numero_binario} é: {numero_decimal}")