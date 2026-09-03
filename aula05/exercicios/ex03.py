import pandas as pd
import matplotlib.pyplot as plt

tempos = pd.Series([100, 105, 110, 108, 115, 120, 125, 130, 500, 550])

# 1. Calcule a Média, a Mediana e a Moda dos tempos de resposta.
print(f"Média: {tempos.mean()}")
print(f"Mediana: {tempos.median()}")
moda = tempos.mode()
tamanho = len(tempos)
tamanho_moda = len(tempos.mode())

if tamanho_moda == tamanho:
    print("Amodal")
else:
    print(f"Moda: {moda}")

# 2. Escreva códigos para criar um Histograma e um Boxplot desses dados utilizando Matplotlib.
tempos.plot(kind="hist")
plt.title("Histograma dos tempos")
plt.show()

tempos.plot(kind="box")
plt.title("Boxplot dos tempos")
plt.show()