import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "nome": ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda"],
    "idade": [18, 20, 19, 22, 21, 18, 23, 20]
}

df = pd.DataFrame(dados)

# exibir DataFrame
print(df)

# mostrar as 5 primeiras linhas
print(df.head(5))

# exibir informações do DataFrame
df.info()

# Exibir resumo estatístico
plt.bar(
    df["nome"], df["idade"],
    width= 0.4,
    color= "#0f5de3"
)
plt.title("Cadastro de Alunos")
plt.xlabel("Nome")
plt.ylabel("Idade")

plt.show()