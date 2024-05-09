populacao_a = 5000000
populacao_b = 7000000
taxa_natalidade_a = 0.03
taxa_natalidade_b = 0.02
anos = 0
while populacao_a <= populacao_b:
    populacao_a *= 1 + taxa_natalidade_a
    populacao_b *= 1 + taxa_natalidade_b
    anos += 1
print("Demorou", anos, "anos para a população do país A ultrapassar a população do país B.")