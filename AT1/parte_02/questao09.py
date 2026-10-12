import pandas as pd

tempo_com_outlier = [120, 130, 115, 140, 125, 150, 135, 110, 128, 500]

tempo = pd.Series(tempo_com_outlier)

# Média
print(f"Média: {tempo.mean()}")

# Mediana 
print(f"Mediana: {tempo.median()}")

# amplitude
print(f"Amplitude: {tempo.max() - tempo.min()}")

# Desvio padrão
print(f"Desvio padrão: {tempo.std(ddof=0) :.2f}")
