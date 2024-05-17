dia , mes, ano = map(int,input("Digite uma data no formatoDD/MM/AAAA:").split("/"))

meses = ["Janeiro","Fevereiro","Março", "Abril","Maio","Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]
def data(d,m,a):
    return print(f"{dia} de {meses[int(mes)-1]} de {ano}")
data(dia, mes, ano)