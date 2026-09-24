import numpy as np

#Lançar a moeda 10.000 vezes
resultados = np.random.choice(["Cara", "Coroa"], size=10000)

#Os 30 primeiros resultados
print(f"Primeiros resultados dos lançamentos: {resultados[:30]}")

#Contando a quantidade de caras
caras = np.sum(resultados == "Cara")

#Probabilidade de Cara na simulação
prob_simulacao = caras / len(resultados)

print(f"Total de caras: {caras}")
print(f"Probabilidade experimental: {prob_simulacao:.4f} ou {prob_simulacao * 100:.2f}%")

print(f"Probabilidade teórica: {(1/2)*100:.2f}%")