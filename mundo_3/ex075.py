# 075 Análise de dados em uma Tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No finall, mostre:
# a) quantas vezes apareceu o valor 9
# b) em que posição foi digitado o valor 3
# c) quais foram os números pares

listan = []
for c in range (0, 4):
    n = int(input('Digite um número: '))
    listan.append(n)
    tup = tuple(listan)
print(f'Você digitou os valores {tup}')
if 9 in tup:
    print(f'O valor 9 apareceu {tup.count(9)} vezes.')
else:
    print('Não foi digitado o valor 9.')
if 3 in tup:
    print(f'O valor 3 foi digitado na posição {tup.index(3) + 1}.')
else:
    print('Não foi digitado o valor 3.')
print('Os valores pares digitados são: ', end='')
for p in tup:
    if p % 2 == 0:
        print(p, end='')
