import pandas as pd

dados = {
    "usuario": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "idade": [18, 22, 25, 31, 28, 35, 42, 24, 29, 33],
    "requisicoes": [10, 15, 8, 20, 12, 25, 18, 9, 14, 21],
    "tempo_ms": [120, 130, 115, 140, 125, 150, 135, 110, 128, 145],
    "erros": [0, 1, 0, 2, 0, 3, 1, 0, 1, 2],
    "sistema": [
        "Android", "iOS", "Android", "Android", "iOS",
        "Android", "Windows", "Android", "iOS", "Android"
    ]
}

df = pd.DataFrame(dados)

# a) as cinco primeiras linhas;
print(f"Cinco primeiras linhas: \n${df.head()}")

# b) quantidade de linhas e colunas;
print(f"\nQuantidade de linhas e colunas: {df.shape}\n")

# c) informações gerais do DataFrame;
{df.info()}

# d) estatísticas descritivas das variáveis numéricas.
print(f"\nEstatísticas descritivas: \n{df.describe()}")