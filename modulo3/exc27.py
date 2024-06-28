import random
perdeu = 0
venceu = 0
def derrota(numero):
    global perdeu
    if numero == 11 and jogada ==1 or numero == 7:
        perdeu = 1
        return print("Você tirou 11 ou 7 e  perdeu") 
    else:
        return True

def vitoria_primeira(x):
    global venceu
    if x ==3 and jogada ==1:
        venceu = 1
        return print("Você tirou 3 e Ganhou!") 
    elif x ==2 and jogada ==1:
        venceu = 1
        return print("Você tirou 2 e Ganhou!")
    
    elif x ==12 and jogada ==1:
        venceu = 1
        return print("Você tirou 12 e Ganhou!")
    else: 
        
        return print(f"Seu número foi {num} jogue os dados e tire {num} novamente para ganhar") and True
def vitoria_segunda(x):
    if num == num2:
        return print(f"Parabéns, Voce tirou de novo {num2} então ganhou o jogo")
    else:
        return print(f"Você tirou {num2} continue tentando")
while True:
    jogada = 1
    input("Digite algo para rolar os dados:")
    num = random.randint(2,12) 
    derrota(num)
    if perdeu == 0:
        vitoria_primeira(num)
    break
if perdeu == 0 and venceu == 0:
    while True:
        jogada = 2
        input("Digite algo para rolar os dados pela segunda vez:")
        num2 = random.randint(2,12)
        vitoria_segunda(num2)
        derrota(num2)