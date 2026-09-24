import numpy as np

#Gerar 100.000 lançamentos para cada dado independente
dado1 = np.random.randint(1, 7, 100000)
dado2 = np.random.randint(1, 7, 100000)

#Verificar a prob de ambos sairem 6
result_duplo_6 = (dado1 == 6) & (dado2 == 6)

prob_simulacao = result_duplo_6.mean()
prob_teorica = 1/36

print(f"Probabilidade Do Experimento: {prob_simulacao:.4f} ({prob_simulacao*100:.2f}%)")
print(f"Probabilidade Teórica: {prob_teorica:.4f} ({prob_teorica*100:.2f}%)")
