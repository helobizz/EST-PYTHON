import pandas as pd

grupoA = [100, 100, 100, 100, 100]
grupoB = [80, 90, 100, 110, 120]

serieA = pd.Series(grupoA)
serieB = pd.Series(grupoB)

# Média aritmética e amplitude
print(f"Média aritmética (grupo A): {serieA.mean()}")
print(f"Média aritmética (grupo B): {serieB.mean()}")

print(f"Amplitude (grupo A): {serieA.max() - serieA.min()}")
print(f"Amplitude (grupo B): {serieB.max() - serieB.min()}")


# Variância amostral e populacional
print(f"Variância amostral (grupoA): {serieA.var()}")
print(f"Variância amostral (grupoB): {serieB.var()}")
print(f"Variância populacional (grupoA): {serieA.var(ddof=0)}")
print(f"Variância populacional (grupoB): {serieB.var(ddof=0)}")


# Desvio padrão correspondente
print(f"Desvio padrão amostral(grupo A): {serieA.std()}")
print(f"Desvio padrão amostral(grupo B): {serieB.std()}")

print(f"Desvio padrão populacional(grupo A): {serieA.std(ddof=0)}")
print(f"Desvio padrão populacional(grupo B): {serieB.std(ddof=0)}")