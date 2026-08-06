# Primeiro DataFrame
import pandas as pd # pd é apelido
import matplotlib.pyplot as plt

dados = {
    "Aluno": ["Heloísa", "Renan", "Raissa", "Carlos"],
    "Nota": [8, 5, 9, 6]
}

df = pd.DataFrame(dados) # criando um novo dataframe a partir dos dados(converte em um tipo que é fácil manipular)

# df.info() # mostra algumas informações do dataframe

# print(df.describe()) # retorna uma descrição/resumo do dataframe (preciso usar print)

# print(df.head()) # traz apenas os primeiros dados/registros para não pesar o sistema

# (df) # traz o dataframe completo

# print(df.shape) # retorna a quantidade de linhas e colulas


# Primeiro Gráfico (importa matplotlib)
plt.bar( #.plot (gráfico de linhas)
    df["Aluno"], df["Nota"], # define as barras do meu gráfico 
    width = 0.5,
    color = "#5d6cc3"
    ) 
plt.title("Nota dos Alunos") # define o título
plt.xlabel("Aluno") # nomeia o eixo x
plt.ylabel("Nota") # nomeia o eixo y

plt.show() 