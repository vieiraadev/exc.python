nome = input("digite seu nome: ")
idade = (input("digite sua idade: "))

if nome and idade:
    print("seu nome é:",nome)
    print("seu nome invertido é", nome[::-1])
    if  '' in nome:
      print("seu nome contem espaços")
    else:
      print("seu nome nao contem espaços")


    print(f"seu nome tem",{len(nome)}, "letras" )
    print(f"a primeira letra do seu nome é",{nome[0:1]})
    print(f"a ultima letra do seu nome é",{nome[-1]})
else:
   print("este campo esta vazio")