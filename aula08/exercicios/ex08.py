import random

# Quantidade de usuários
N = 100000

# Contadores
android = 0
python = 0
android_python = 0

# Simulação
for i in range(N):

    # Sorteia o sistema operacional
    so = random.choice(["Android", "iOS"])

    # Sorteia a linguagem
    linguagem = random.choice(["Python", "Java"])

    # Conta Android
    if so == "Android":
        android += 1

    # Conta Python
    if linguagem == "Python":
        python += 1


 # Conta Android E Python
    if so == "Android" and linguagem == "Python":
        android_python += 1

   

# Probabilidades experimentais
p_android = android / N
p_python = python / N
p_intersecao = android_python / N

# Probabilidade da união
p_uniao = p_android + p_python - p_intersecao


# Resultados
print("RESULTADOS")
print("-" * 40)

print(f"P(Android) = {p_android:.4f}")
print(f"P(Python) = {p_python:.4f}")
print(f"P(Android ∩ Python) = {p_intersecao:.4f}")
print(f"P(Android ∪ Python) = {p_uniao:.4f}")

print("\nVERIFICAÇÃO DA EQUAÇÃO")

print(
    f"{p_uniao:.4f} = "
    f"{p_android:.4f} + "
    f"{p_python:.4f} - "
    f"{p_intersecao:.4f}"
)
