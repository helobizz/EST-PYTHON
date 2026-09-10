import pandas as pd

dados = [10, 12, 15, 18, 20]

serie = pd.Series(dados)

# média aritmética
print(f"média aritmética: {serie.mean()}")

#  amplitude
print(f"Amplitude: {serie.max() - serie.min()}")

# variância populacional
print(f"Variância populacional: {serie.var(ddof=0)}")

# desvio padrão populacional
print(f"Desvio padrão populacional: {serie.std(ddof=0)}")