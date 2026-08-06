import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto": ["Cookie", "Brownie", "Cone", "Brookie"],
    "Preco": [10, 5, 11, 15],
    "Quantidade": [20, 15, 10, 5]
}

df = pd.DataFrame(dados)

print(df)

plt.bar(
    df["Produto"], df["Preco"],
    color= "#EE05EE",
    width=0.5
    )
plt.title("Preço dos Produtos")
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.show()

plt.bar(
    df["Produto"], df["Quantidade"],
    color= "#06CEAD",
    width=0.5
    )
plt.title("Quantidade de produtos")
plt.show()
plt.xlabel("Produto")
plt.ylabel("Quantidade")

plt.bar(
    df["Quantidade"], df["Preco"],
    color= "#0EDE2D",
    width=0.5
    )
plt.show()
plt.xlabel("Quantidade")
plt.ylabel("Preço")