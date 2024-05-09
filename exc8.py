hex_digitos = "0123456789ABCDEF"
numero_decimal = int(input("Digite um número decimal: "))
numero_hexadecimal = ""
while numero_decimal > 0:
    resto = numero_decimal % 16
    numero_hexadecimal = hex_digitos[resto] + numero_hexadecimal
    numero_decimal = numero_decimal // 16
print(f"O valor hexadecimal é: {numero_hexadecimal}")