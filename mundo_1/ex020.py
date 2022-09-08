# 020 Sorteando uma ordem na lista
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a = input('Digite um nome: ')
b = input('Digite um nome: ')
c = input('Digite um nome: ')
d = input('Digite um nome: ')
nomes = [a, b, c, d]
random.shuffle(nomes)
print('A ordem de apresentação dos alunos será: ')
print(nomes)