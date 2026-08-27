import pandas as pd
import matplotlib.pyplot as plt

# notas = [5, 6, 7, 8, 9, 10]
# frequencias = [2, 3, 5, 6, 3, 2]

# plt.bar(notas, frequencias) # cria o gráfico de barras

# plt.xlabel("Nota") 
# plt.ylabel("Frequência")
# plt.title("Distribuição das Notas")

# plt.show()


notas = [5, 6, 7, 8, 9, 10, 5, 6, 7, 8, 7, 8, 9, 10, 8, 7, 6, 8, 9, 8] # dados brutos

serie = pd.Series(notas) 

frequencia = serie.value_counts().sort_index()

# frequencia.plot(kind="bar") # cria o gráfico

# plt.title("Frequência das Notas")
# plt.xlabel("Nota")
# plt.ylabel("Quantidade")

# plt.show()

# GRÁFICO DE PIZZA

# frequencia.plot(
#  kind="pie",
#  autopct="%1.1f%%"
# )
# plt.title("Distribuição das Notas")
# plt.ylabel("")
# plt.show()

# HISTOGRAMA
# idades = [18, 19, 20, 21, 22, 25, 27, 30, 31, 35]

# plt.hist(idades, bins=2) # cria o histograma / bins = intervalos

# plt.xlabel("Idade")
# plt.ylabel("Frequência")
# plt.title("Distribuição das Idades")

# plt.show()

# BOXPLOT
tempos = [
 120, 130, 115, 140, 150,
 180, 175, 190, 210, 220,
 250, 280, 300, 320, 350
]

plt.boxplot(tempos)

plt.ylabel("Tempo (ms)")
plt.title("Distribuição do Tempo de Resposta")

plt.show()