# 094 Unindo dicionários e listas
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
# a) Quantas pessoas cadastradas
# b) A média de idade
# c) Uma lista com mulheres
# d) Uma lista com idade acima da média

galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear() #apaga pessoa quando vem pessoa nova
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Responda apenas com F ou M: ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas com F ou M: ')
    if resp == 'N':
        break
print(galera)
print('_' * 50)
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print()
midade = soma / len(galera)
print(f'A média de idade das pessoas do grupo é {midade:5.1f} anos.')
print()
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end="")
print()
print()
print('Listas das pessoas que possuem idade acima da média: ')
for p in galera:
    if p['idade'] >= midade:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()