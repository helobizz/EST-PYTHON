import numpy as np

# # Sorteando um número entre 1 e 6 (o 7 não é conmtemplado)
# resultado = np.random.randint(1, 7)
# print(50*"-")
# print("LANÇANDO DADO...")
# print(resultado)

# # size -> quantidade de vezes que ele vai executar o comando
# resultado_1000 = np.random.randint(1, 7, size=1000)
# print(50*"-")
# print("DEPOIS DE 1000x LANÇADO...")
# print("15 primeiros resultados...")
# print(resultado_1000[:15]) # mostra só os 15 primeiros


# resultado_10000 = np.random.randint(1, 7, size=10000)

# qtd_cinco = np.sum(resultado_10000 == 5)

# print(f"Quantidade de vezes que caiu o número 5: {qtd_cinco}")

# probabilidade = qtd_cinco / len(resultado_10000)

# print(f"Probabilidade de 5s obtidos: {probabilidade}")

# print(f"Probabilidade real teorica 1/6: {1/6:.4f}")


# Estimando taxa de erro em produção