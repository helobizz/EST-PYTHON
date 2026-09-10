import pandas as pd

tempos = pd.Series ([110, 115, 120, 112, 118, 121, 117, 113, 119, 300])

# média e mediana 
print(f"Média: {tempos.mean()}")
print(f"Mediana: {tempos.median()}")

# Amplitude, variância e desvio padrão
print(f"Variância: {tempos.var(ddof=0)}")
print(f"Amplitude: {tempos.max() - tempos.min()}")
print(f"Desvio padrão: {tempos.std(ddof=0)}")

