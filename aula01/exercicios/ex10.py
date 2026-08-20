import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "Cadeira", "Memória RAM", "SSD", "Processador"],
    "Preco": [110, 250, 820, 710, 650, 980, 1200],
    "qtd": [50, 68, 40, 37, 24, 43, 12]
}

df = pd.DataFrame(dados)

df["Valor Total"] = df["Preco"] * df["qtd"]

print(df)