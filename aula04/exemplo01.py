import pandas as pd

tabela = pd.read_csv('dados.csv')

serie = tabela["renda_mensal"] # posso fazer isso com qualquer dado da tabela

# print(serie.value_counts().sort_index()) # frequencia absoluta

# print(serie.value_counts(normalize=True).sort_index()) # Frequencia Relativa ordenada pela idade

frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()

tabela = pd.DataFrame({
    "frequencia": frequencia,
    "frequencia_relativa": frequencia / len(serie),
    "frequencia_acumulada": frequencia_acumulada
})

print(tabela)