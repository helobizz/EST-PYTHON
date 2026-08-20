import pandas as pd

clientes = pd.read_csv("clientes.csv")

# Calcule o gasto médio da população
gasto_medio = clientes["Valor_Gasto"].mean()
print(f"Gasto médio da população: {gasto_medio}")

# Retire uma amostra aleatória de 10 clientes
amostra1 = clientes.sample(n=10)
media1 = clientes["Valor_Gasto"].sample(10).mean()
print(amostra1)
print(f"A média da amostra de 10 alunos é: {media1}")

# Retire uma amostra aleatória de 30 clientes
amostra2 = clientes.sample(n=30)
media2 = clientes["Valor_Gasto"].sample(30).mean()
print(amostra2)
print(f"A média da amostra de 30 alunos é: {media2}")

# compare as duas estimativas
print(f"A média de 10 alunos é igual a {media1} e a média de 30 alunos é igual a {media2}, com uma direfença entre elas de {media1 - media2}")