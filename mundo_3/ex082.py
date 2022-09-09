# 082 Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
sn = 'S'
pares = []
impares = []

while sn == 'S':
    n = int(input('Digite um número: '))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Você criou a lista {lista}')
print(f'Na lista criada, são números pares {pares}')
print(f'Na lista criada, são números ímpares {impares}')