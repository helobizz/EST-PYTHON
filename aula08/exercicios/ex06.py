import numpy as np

#Gerar 100.000 lançamentos para cada dado independente
dado1 = np.random.randint(1, 7, 100000)
dado2 = np.random.randint(1, 7, 100000)

#Verificar a prob de ambos sairem 6
result_duplo_1 = (dado1 == 1) & (dado2 == 1)
result_duplo_2 = (dado1 == 2) & (dado2 == 2)
result_duplo_3 = (dado1 == 3) & (dado2 == 3)
result_duplo_4 = (dado1 == 4) & (dado2 == 4)
result_duplo_5 = (dado1 == 5) & (dado2 == 5)
result_duplo_6 = (dado1 == 6) & (dado2 == 6)

result_um_dois = (dado1 == 2) | (dado2 == 2)
resultado_um_dois = result_um_dois.mean()

result_duplo_igual = (dado1 == dado2)
soma_result_duplo = result_duplo_igual.mean()


prob_simulacao1 = result_duplo_1.mean()
prob_simulacao2 = result_duplo_2.mean()
prob_simulacao3 = result_duplo_3.mean()
prob_simulacao4 = result_duplo_4.mean()
prob_simulacao5 = result_duplo_5.mean()
prob_simulacao6 = result_duplo_6.mean()

prob_duplo_igual = prob_simulacao1 + prob_simulacao2 + prob_simulacao3 + prob_simulacao4 + prob_simulacao5 + prob_simulacao6
prob_teorica = 11/36

print(f"Probabilidade Do Experimento: {resultado_um_dois:.4f} ({resultado_um_dois*100:.2f}%)")
print(f"Probabilidade Teórica: {prob_teorica:.4f} ({prob_teorica*100:.2f}%)")
