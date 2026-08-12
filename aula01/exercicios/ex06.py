import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Time": ["Palmeiras", "Flamengo", "Corinthians", "São Paulo", "Santos"],
    "Pontos": [48, 46, 41, 38, 35]
}

df = pd.DataFrame(dados)

# exibir tabela
print(df)

# gerar gráfico
plt.bar(
    df["Time"], df["Pontos"],
    color= "green"
)
# alterar título
plt.title("Campeonato")

plt.show()