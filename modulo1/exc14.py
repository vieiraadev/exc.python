pessoa = []
while True:
    name = input("digite o nome:")
    rg = input("digite o rg:")
    cpf = input("digite o cpf:")
    person = (name, rg, cpf)
    pessoa.append(person)
    resp= input("deseja continuar cadastrando(S/N)")
    if resp == 'N': 
     break
for person in pessoa:
   print(f"nome: {person[0]}")
   print(f"RG: {person[1]}")
   print(f"CPF: {person[2]}\n")