import pandas as pd

notas = pd.Series([7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 
9, 8, 10])

# 1. Calcule a Média, a Mediana e a Moda das notas dos 20 alunos listados.
print(f"Média: {notas.mean()}")
print(f"Mediana: {notas.median()}")
moda = notas.mode()
print(f"Moda: {moda}")

# 2. Extraia o valor mínimo e máximo do conjunto usando Pandas.
print(f"Mínimo: {notas.min()}")
print(f"Máximo: {notas.max()}")
