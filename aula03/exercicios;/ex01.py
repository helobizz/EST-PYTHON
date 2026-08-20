import pandas as pd
alunos = pd.DataFrame({
    "Nome": [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Lucas", "Marina"
    ],
    "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

# 1. Verifique o tamanho da população
print(alunos.shape[0]) # volta apenas a qtd de elementos
print(len(alunos))

# 2. Calcule a média da população 
print(alunos["Nota"].mean())

# 3. Retire uma amostra de 5 alunos
amostra = alunos.sample(n=5, random_state=42)
print(amostra)

# 4. Calcule a média da amostra
print(amostra["Nota"].mean())

# 5. Compare as duas médias
medPopulacao = alunos["Nota"].mean()
medAmostra = amostra["Nota"].mean()
print(medPopulacao - medAmostra)

# 6. Repita utilizando uma amostra de 8 alunos