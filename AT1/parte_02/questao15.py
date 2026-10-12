import pandas as pd
import matplotlib.pyplot as plt

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

tempos = pd.Series(dados["tempo_ms"])

# a) Estatística descritiva
# média do tempo de resposta;
media = tempos.mean()
print(f"Média: {media}")

# mediana;
mediana = tempos.median()
print(f"Mediana: {mediana}")

# amplitude;
amplitude = tempos.max() - tempos.min()
print(f"Amplitude: {amplitude}")

# desvio padrão.
desvio = tempos.std(ddof=0)
print(f"Desvio padrão: {desvio :.2f}")



# b) Análise de frequência
# Apresente a distribuição dos usuários por sistema operacional
df = pd.DataFrame(dados)

frenquencia = df["sistema"].value_counts()

percentuais = df["sistema"].value_counts(normalize=True) * 100

print(f"\nQuantidade por sistema:\n{frenquencia}\n")
print(f"Percentual por sistema:\n{percentuais}\n")



# c) Probabilidade
# Calcule a probabilidade estimada de uma requisição apresentar erro.
com_erro = df['erros'] > 0
qtd_com_erro = com_erro.sum()
total = len(df)
prob_erro = qtd_com_erro / total

print(f"Probabilidade estimada: {prob_erro * 100}%")



# d) Visualização: Crie dois gráficos:
# 1. distribuição dos sistemas operacionais;
frenquencia.plot(kind="bar")
plt.title("Distribuição dos SO")
plt.xlabel("SO")
plt.ylabel("Qtd de Usuários")
plt.show()

# 2. distribuição dos tempos de resposta.
plt.hist(df["tempo_ms"], bins=5, edgecolor="black")
plt.title("Distribuição dos Tempos de Resposta")
plt.xlabel("Tempo de resposta (ms)")
plt.ylabel("Frequência")
plt.show()