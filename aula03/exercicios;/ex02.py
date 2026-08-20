import pandas as pd

alunos = pd.DataFrame({
    "Nome": [
        "Heloísa", "Carlos", "Raissa", "Vitor", "Renan", "Ana", "Matheus", "Yuri", "Marcos", "Denis", "Pedro", "Bruno", "Jonathan", "Gustavo", "Letícia", "Eduarda", "Joana", "Antônio", "João", "Jorge", "Ruth", "Izabel", "Maria", "Rosimeire", "Josevaldo", "Rogério", "Kauan", "Vinicius", "Miguel", "Jovana"
    ],
    "Idade": [
        20, 21, 32, 34, 15, 18, 19, 23, 36, 67, 43, 14, 17, 45, 21, 16, 42, 52, 19, 32, 28, 47, 32, 65, 26, 75, 54, 28, 67, 21
    ],
    "Nota": [
        10, 8, 9, 7, 6, 8, 7, 6, 3, 9, 10, 8, 7, 6.7, 9.8, 8.9, 6, 8, 4, 6, 7, 4, 2, 8, 10, 7, 9, 6, 8, 7
    ]
})

# Calcule a média da população
populacao = alunos["Idade"].mean()

# Selecione aleatoriamente 5 alunos
amostra = alunos["Nome"].sample(5)
print(amostra)

# Calcule a média da amostra
amostra5 = alunos["Idade"].sample(5)
idade_media5 = amostra5.mean()

# Selecione aleatoriamente 10 alunos
amostra2 = alunos["Nome"].sample(10)
amostra10 = alunos["Idade"].sample(10)
idade_media10 = amostra10.mean()

# Compare os resultados
print(f"Média de 5 alunos: {idade_media5}")
print(f"Média de 10 alunos: {idade_media10}")
print(f"Média da população: {populacao}")
