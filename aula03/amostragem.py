import pandas as pd

df = pd.read_csv("aula03/dados.csv")

# # saber a quantidade de elementos/população
# print(df.shape)

# print(df.head())

# # criar amostra
# amostra = df.sample(n=50)

# # quero mostrar sempre a mesma amostra
# amostra = df.sample(n=100, random_state=15)
# # quero ver o shape da amostra
# print(amostra.shape)

# # exibir a média de idade da população
# print(f"Media da população: {df["idade"].mean()}")
# # média de idade da amostra (pega da amostra criada, podendo ter o seed ou não)
# print(f"Média da amostra: {amostra["idade"].mean()}")

# # ERRO AMOSTRAL
# amostra = df.sample(n=100)

# medPopulacao = df["idade"].mean()
# print(f"Média da população: {medPopulacao}")

# medAmostra = amostra["idade"].mean()
# print(f"Média amostra: {medAmostra}")

# print(f"Erro amostral: {medPopulacao - medAmostra}")

# Tamanho da amostra (quanto maior, mais precisa)
nAmostra = 100
amostra = df.sample(n=nAmostra)

medPopulacao = df["idade"].mean()
print(f"Média da população: {medPopulacao}")

medAmostra = amostra["idade"].mean()
print(f"Média amostra: {medAmostra}")

print(f"Erro amostral: {medPopulacao - medAmostra}")