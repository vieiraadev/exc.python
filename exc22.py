import math
def converterGrausParaRad(numero):
  rad=(numero/180)*math.pi
  return rad
print(' Funcoes trigonometricas')
angulo = float(input('digite o valor em graus:'))
conv = converterGrausParaRad(angulo)
print(f'angulo {angulo} em graus equivale a {conv:.2f} radianos')