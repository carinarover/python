# 069 Análise de dados do grupo
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos
# b) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos

maior = 0
homens = 0
mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo com F ou M: ')).strip().upper()[0]
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade >= 20:
        mulher += 1
    if cont == 'N':
        break
print('Cadastro finalizado!')
print(f'O número de pessoas maiores de 18 anos é {maior}.')
print(f'Foram cadastrados {homens} homens.')
print(f'Há {mulher} mulheres maiores de 18 anos.')