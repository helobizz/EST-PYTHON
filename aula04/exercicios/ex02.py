import pandas as pd
import matplotlib.pyplot as plt

# BASE DE DADOS
linguagens = []

serie = pd.Series(linguagens)

# frequência de cada linguagem;
frequencia_absoluta = serie.value_counts()

# frequência relativa;
frequencia_relativa = serie.value_counts(normalize=True)

# linguagem mais frequente.
frequencia_absoluta.idxmax() # retorna o index/nome
frequencia_absoluta.max() # retorna o valor

# Depois crie um gráfico de barras.
frequencia_absoluta.plot(kind="bar")

plt.title("Linguagem de Programação")
plt.xlabel("Linguagens")
plt.ylabel("Quantidade")

plt.show()