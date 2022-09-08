# 019 Sorteando um item na lista
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
# escrevendo o nome escolhido.
import random
a = input('Digite o nome de um aluno: ')
b = input('Digite o nome de outro aluno: ')
c = input('Digite o nome de outro aluno: ')
d = input('Digite o nome de outro aluno: ')
alunos = [a, b, c, d]
print('O aluno que irá apagar o quadro é: {}'.format(random.choice(alunos)))