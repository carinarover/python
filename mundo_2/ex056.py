# 056 Analisador completo
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

from statistics import mean

lista_idade = []
maisvelho = ''
mulheres = 0

for c in range(1, 5):
    print('--------- {}ª PESSOA ---------'.format(c))
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    lista_idade.append(idade)
    sexo = str(input('Digite seu sexo com F ou M: ')).strip().upper()
    if sexo == 'M' and (max(lista_idade)):
        maisvelho = nome
    if sexo == 'F' and idade < 20:
         mulheres += 1

print('A média de idade do grupo é {:.0f} anos.'.format(mean(lista_idade)))
print('A idade do homem mais velho tem {} anos, e seu nome é {}.'.format(max(lista_idade), maisvelho))
print('O número de mulheres menores que 20 anos é {}.'.format(mulheres))

# OBS: ao invés de colocar o sexo para maísuculo (upper), pode deixar assim, e escrever "if sexo in 'Ff' and idade < 20: