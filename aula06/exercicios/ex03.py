import pandas as pd

servidorA = pd.Series([100, 102, 98, 101, 99])
servidorB = pd.Series([70, 130, 90, 110, 100])

# Média
print(f"Média (servidor A): {servidorA.mean()}")
print(f"Média (servidor B): {servidorB.mean()}")

# Amplitude 
print(f"Amplitude (Servidor A): {servidorA.max() - servidorA.min()}")
print(f"Amplitude (Servidor B): {servidorB.max() - servidorB.min()}")

# Desvio padrão populacional de cada um
print(f"Desvio padrão (servidor A): {servidorA.std(ddof=0)}")
print(f"Desvio padrão (servidor B): {servidorB.std(ddof=0)}")