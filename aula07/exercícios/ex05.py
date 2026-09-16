import pandas as pd
import numpy as np

# 1. Simular 10.000 lançamentos de um dado.
lancamento = np.random.randint(1, 7, size=10000)
print("LANÇANDO DADOS...")
print(lancamento[:15])

# 2. Calcular a frequência relativa de CADA uma das 6 faces (1 a 6).
serie = pd.Series(lancamento)
frequencia_relativa = serie.value_counts(normalize=True)
frenquencia = serie.value_counts().sort_index()
# frequencia_relativa = frequencia / lancamento
print(f"Frequência Relativa de cada uma das face: \n{frequencia_relativa}")

# 3. Comparar os resultados obtidos com a probabilidade teórica de 1/6 (16.67%).
probabilidade = 1/ 6 
print(f"Probabilidade teórica 1/6: {probabilidade}")

tabela = pd.DataFrame({
    "Frequencia": frenquencia,
    "Fequencia Relativa": frequencia_relativa * 100,
    "Probabilidade Teorica": probabilidade * 100
})

print(tabela)