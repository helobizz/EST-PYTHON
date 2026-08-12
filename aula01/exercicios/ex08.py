import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Nome": ["O Morro dos Ventos Uivantes", "Reino das Bruxas", "Trono de Vidro", "A Empregada", "Jantar Secreto", "Princípe Cruel", "Mentirosos", "Lucky", "Human Among Gods", "Heartopper"],
    "Autor": ["Emilly Bronte", "Kerri Maniscalco", "Sarah J. Mars", "Freida McFadden", "Rafael Montes", "Holly Black", "E. Lockhart", "Ella Mevil", "Ella Mevil", "Alice Oseman"],
    "Paginas": [291, 382, 478, 354, 279, 348, 290, 396, 520, 321]
}

df = pd.DataFrame(dados)

# exibir tabela
print(df)
# gerar gráfico
plt.bar(
    df["Nome"], df["Paginas"],
    color= "#efa7ff"
)

plt.show()

# usar head()
print(df.head())
# usar describe()
print(df.describe())
# usar info()
df.info()
