salarios = []
abonos = []

print("Projeção de Gastos com Abono")
print("============================")
while True:
    try:
        salario = float(input("Salário(0 para sair): "))
        if salario == 0:
            break
        salarios.append(salario)
        abono = max(0.2 * salario, 100)
        abonos.append(abono)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
if not salarios:
    print("Nenhum salário foi informado.")
else:
    print("Salário - Abono")
    for salario, abono in zip(salarios, abonos):
        print(f"R$ {salario:10.2f} - R$ {abono:10.2f}")
    total_funcionarios = len(salarios)
    total_abonos = sum(abonos)
    min_abono_count = sum(1 for abono in abonos if abono == 100)
    max_abono = max(abonos)
    print(f"Foram processados {total_funcionarios} colaboradores")
    print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
    print(f"Valor mínimo pago a {min_abono_count} colaboradores")
    print(f"Maior valor de abono pago: R$ {max_abono:.2f}")