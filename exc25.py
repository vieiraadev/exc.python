import random

palavra = input("Digite uma palavra: ")
def embaralha_palavra(palavra):
    palavra = palavra.lower()
    caracteres = list(palavra)
    random.shuffle(caracteres)
    palavra_embaralhada = ''.join(caracteres)
    return palavra_embaralhada

resultado = embaralha_palavra(palavra)
print("Palavra embaralhada:", resultado)