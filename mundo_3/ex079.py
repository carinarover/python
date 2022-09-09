# 079 Valores únicos em uma lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista_n = []
sn = 'S'

while sn == 'S':
    n = int(input('Digite um número: '))
    if n not in lista_n:
        lista_n.append(n)
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
print(f'Você digitou os números {sorted(lista_n)}')