import pandas as pd

tempos = pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])

# 1. Calcular a Média Aritmética simples.
print(f"Média: {tempos.mean()}")

# 2. Calcular a Mediana dos tempos registrados.
print(f"Mediana: {tempos.median()}")

# 3. Calcular a Moda (ou modas) deste conjunto.
moda = tempos.mode()
print(f"Moda: {moda}")

# 4. Calcular os valores Mínimo e Máximo observados.
print(f"Mínimo: {tempos.min()}")
print(f"Máximo: {tempos.max()}")
# 5. Refletir: Qual dessas medidas melhor representa o comportamento central dos dados?