import numpy as np

# Requisição: API (100 ms, 500 qtd) | Banco (200 ms, 300 qtd) | 
# Arquivo (500 ms, 200 qtd)
tempos = [100, 200, 500]
qtd = [500, 300, 200]

# 1. Utilize a fórmula da média ponderada para calcular o tempo de latência médio das requisições do sistema.
m_ponderada = np.average(
    tempos,
    weights=qtd
)

print("Média ponderada dos tempos de requisição:")
print(m_ponderada)

# 2. Dica: utilize como pesos (w_i) as quantidades de acessos correspondentes a cada tipo de requisição.
# 3. Desenvolva o código em Python puro (com zip) e em NumPy (np.average) para validação
numerador = sum(
    tempos * qtd
    for tempos, qtd in zip(tempos, qtd)
)

denominador = sum(qtd)

m_pond = numerador / denominador

print("Média ponderada usando zip e for:")
print(m_pond)