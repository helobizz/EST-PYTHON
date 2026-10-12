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

# a) quantidade de usuários por sistema operacional;
qtd_usuario_sistema = df["sistema"].value_counts()

# b) percentual de usuários por sistema operacional.
percentuais = df["sistema"].value_counts(normalize=True) * 100

# Apresente os resultados.
print(f"Quantidade de usuários por SO:\n{qtd_usuario_sistema}\n")
print(f"Percentual de usuários por SO:\n{percentuais}\n")

tabela = pd.DataFrame({
    "Frequencia Absoluta": qtd_usuario_sistema,
    "Frequencia Relativa": percentuais
})

print(tabela)