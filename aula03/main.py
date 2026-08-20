import random

alunos = ["Rogério", "Ricardo", "Shimada", "Kaio", "Camila", "Vitor", "Geovana", "Renan", "Carlos", "Miguel", "Ana", "Sthevens", "Guilherme", "Raissa", "Matheus", "Felipe", "Endrew",
"Arthur", "Gabriela", "Pedro"]

# Amostragem aleatória simples (retorna amostras diferentes)
amostra = random.sample(alunos, 3) # sample pede dois argumentos -> conjunto a ser utilizado e quantidade a ser usada (selecina de forma aleatória (não repete os elementos da amostra))

print(amostra)

# quero obter sempre a mesma amostra (reprodutibilidade)
random.seed(15) # seed -> semente aleatória
amostra = random.sample(alunos, 3)
print(amostra)