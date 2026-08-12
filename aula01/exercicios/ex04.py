import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "produto": ["Arroz", "Feijão", "Café", "Açúcar", "Leite", "Óleo", "Macarrão"],
    "preco": [32, 11, 24, 6, 8, 9, 7]
}

df = pd.DataFrame(dados) 

# construir gráfico
plt.bar(
    df["produto"], df["preco"]
)
# alterar título
plt.title("Produtos de Mercado")
# nomear eixos
plt.xlabel("Produto")
plt.ylabel("Preço")
plt.show()