import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Filme": ["Avatar", "Matrix", "Interestelar", "Vingadores", "Barbie"],
    "Nota": [9.2, 9.5, 9.8, 8.9, 7.5]
}

df = pd.DataFrame(dados)

# exibir df
print(df)
# usar head()
print(df.head())
#usar describe
print(df.describe())

# construir gráfico
plt.bar(
    df["Filme"], df["Nota"],
    width= 0.4,
    color= "blue"
)
plt.title("Avaliações")
plt.xlabel("Filme")
plt.ylabel("Nota")

plt.show()