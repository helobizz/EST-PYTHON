import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "produto": ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "preco": [85, 150, 980, 220, 320],
    "qtd": [12, 8, 4, 10, 6]
}

df = pd.DataFrame(dados)

# Quantos produtos existem?
print(len(df["produto"]))

# Qual possui maior preço?
print(max(df["preco"]))

# Qual possui menor preço?
print(min(df["preco"]))

# Qual a soma das quantidades?
print(sum(df["qtd"]))