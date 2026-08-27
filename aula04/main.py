import pandas as pd

notas = [
    7, 8, 6, 9, 7,
    5, 8, 7, 10, 6,
    8, 9, 7, 5, 6,
    8, 7, 9, 8, 10
]

# Series (coluna da minha tabela - serie de dados)
serie = pd.Series(notas)

# # traz todos os elementos com os indíces
# print(serie)

# # todas as frequências das notas (retorna uma tabela com as frequências absolutas)
# # conta quantas vezes cada valor aparece
# print(serie.value_counts()) 

# # ordenando as frequências (ordena a partir do index)
# print(serie.value_counts().sort_index())

# # ordena pelo valor (menor frequência)
# print(serie.value_counts().sort_values())


# # FREQUÊNCIA RELATIVA
# print(serie.value_counts(normalize=True) * 100) # * 100 para retornar em porcentagem  
# # false -> mostra a frequência absoluta

frequencia = serie.value_counts().sort_index()

# FREQUÊNCIA ACUMULADA
frequencia_acumulada = frequencia.cumsum() # soma as frequeências absolutas
# print(frequencia_acumulada)

# CRIANDO TABELA COM DF
tabela = pd.DataFrame({
    "Frequencia": frequencia,
    "Frequencia_Relativa": frequencia / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada # o valor da última linha sempre deve ser igual ao valor de elementos
})

print(tabela)