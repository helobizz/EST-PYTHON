import numpy as np

lancamentos = np.random.randint(1, 7, size=10000)

n_primo = np.sum((lancamentos == 2) | (lancamentos == 3) | (lancamentos == 5))

p_teorica = 3 / 6

p_experimental = n_primo / len(lancamentos)

print(f"Probabilidade teorica: {p_teorica * 100}%")

print(f"Quantidade de resultados primos: {n_primo}")

print(f"Probabilidade de obter um número primo: {p_experimental * 100}%")