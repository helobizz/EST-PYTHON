import pandas as pd

salarios = pd.Series([2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 
2800, 20000])

# 1. Calcule a Média, a Mediana e a Moda dos salários acima utilizando Panda.
print(f"Média: {salarios.mean()}")
print(f"Mediana: {salarios.median()}")
moda = salarios.mode()
tamanho = len(salarios)
tamanho_moda = len(salarios.mode())

if tamanho_moda == tamanho:
    print("Amodal")
else:
    print(f"Moda: {moda}")