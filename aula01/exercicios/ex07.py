import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Nome": ["Heloísa", "Renan", "Raissa", "Carlos", "Ana", "Jorge", "Vitor", "Miguel", "Geovana", "Vinicius", "Guilherme", "Rogério", "Roberto", "Beatriz", "Isaac", "Camila", "Maylon", "Matheus", "João", "Pedro"],
    "Idade": [20, 19, 20, 20, 19, 24, 21, 20, 21, 23, 25, 32, 21, 26, 56, 23, 18, 28, 31, 17],
    "Nota": [10, 9, 8, 9, 7, 5, 8, 9.3, 4.7, 8.4, 7, 6, 9, 10, 8.7, 4.8, 7, 3.4, 9, 8.9]
}

df = pd.DataFrame(dados)

# exibir df
print(df)
# utilizar head()
print(df.head())
# utilizar describe()
print(df.describe())
# utilizar info()
df.info()