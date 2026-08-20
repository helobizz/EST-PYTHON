import pandas as pd

dados = {
    "Nome": ["Ana", "Carlos", "João", "Felipe", "Marcos", "José"],
    "Idade": [20, 25, 63, 10, 58, 25],
    "Nota": [10, 5, 9, 8, 7, 3]
}

df = pd.DataFrame(dados)

# print(df.shape) -> retorna o tamanho do DF

# print(df.columns) # retona as colunas

# print(df["Nome"]) # retorna os valores dessa coluna -> série de dados 

# print(df[["Nome", "Nota"]]) # retornando mais que uma coluna -> add 2 colchetes

# print(df.iloc[0]) # seleciona um determinado elemento (ex.: primeira linha)

# print(df.iloc[0:2]) # selecionando várias linhas (vai selecionar as linhas 0 e 1 - não pega o 2)

# print(df.iloc[4, 2]) # selecionando uma célula/posição específica (linha 4, coluna 2)

# print(df["Nota"].max()) # Selecionando a maior nota com o método do PANDAS

# print(df["Nota"].min())

# print(df["Nota"].mean()) # média


# # Criando uma nova coluna
# df["Nota Final"] = df["Nota"] + 1.3
# print(df)

# print(df.sort_values("Nota")) # ordena da menor para a menor
# print(df.sort_values("Nota", ascending=False)) # ordena do menor para o maior

# print(df["Nota"] < 7) # Retorna true e false para os atributos que atendam ou não a condição

# print(df[df["Nota"] < 7]) # retorna os índices que atendam a condição

print(df[(df["Nota"] < 7) & (df["Idade"] > 20)]) # combinando condições