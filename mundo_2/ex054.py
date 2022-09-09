# 054 Grupo da Maioridade
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores (considerando maioridade como 21 anos).

from datetime import date
hoje = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = hoje - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("O número de pessoas maiores de idade é {} e o número de pessoas menores de idade é {}.".format(maior, menor))