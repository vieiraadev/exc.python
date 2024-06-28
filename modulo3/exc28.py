def converterHora(hora, minuto):
    if hora == 0:
        return 12, minuto, 'A'
    elif 1 <= hora < 12:
        return hora, minuto, 'A'
    elif hora == 12:
        return 12, minuto, 'P'
    else:
        return hora - 12, minuto    , 'P'

def mostraHora(hora, minuto, ap):
    if ap == "A":
        apSrc = "A.M."
    else:
        apSrc = "P.M."

    print(f"A hora convertida é: {hora}:{minuto:02d} {apSrc}")

while True:
    hora = int(input("Digite as horas (0-23): "))
    minuto = int(input("Digite os minutos (0-59): "))
    
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
        print("Por favor, insira valores válidos para horas (0-23) e minutos (0-59).")
        continue
    
    else:
        hora12, minuto12, ap = converterHora(hora, minuto)
        mostraHora(hora12, minuto12, ap)

        repetir = input("Deseja converter outra hora? (s/n): ").lower()  
        if repetir != 's':
            break