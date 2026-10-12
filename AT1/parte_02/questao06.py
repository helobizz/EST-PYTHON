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

df = pd.DataFrame(dados)

qtd_usuario_sistema = df["sistema"].value_counts()

# Crie um gráfico adequado para representar a quantidade de usuários por sistema operacional.
qtd_usuario_sistema.plot(kind="bar")
plt.title("Quantidade de usuários por SO")
plt.xlabel("Sistema Operacional")
plt.ylabel("Usuários")
plt.show()
