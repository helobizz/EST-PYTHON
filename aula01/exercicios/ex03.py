import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "lista": [12, 25, 18, 40, 32, 11, 9, 28, 37, 15]
}

df = pd.DataFrame(dados)

# Quantidade de elementos
print(len(df))

# Soma
print(sum(df["lista"]))

# Média
print(df["lista"].mean())

# Maior valor
print(max(df["lista"]))

# Menor valor 
print(min(df["lista"]))

# Ordene a lista em ordem crescente
crescente = df.sort_values(by="lista")
print(crescente)