import pandas as pd

dados = {
    "nome": ["João", "Maria", "Pedro", "Ana"],
    "idade": [18, 20, 19, 22]
}

df = pd.DataFrame(dados)

# exibir
print(df.head()) # ou print(df)

# contar registros
print(df.shape) # ou print(len(df))

# visualizar informações
df.info()