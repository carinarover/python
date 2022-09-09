# 071 Simulador de Caixa Eletrônico
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50,00, R$ 20,00, R$ 10,00 e R$ 1,00.


valor = int(input('Digite o valor que gostaria de sacar: R$ '))
cinquenta = valor // 50
resto50 = valor % 50
vinte = resto50 // 20
resto20 = resto50 % 20
dez = resto20 // 10
resto10 = resto20 % 10
um = resto10 // 1
print(f'Você deseja sacar {valor}. O valor será entregue com {cinquenta} notas de R$ 50, {vinte} notas de '
      f'R$20, {dez} notas de R$ 10 e {um} notas de R$ 1.')

#ou
print('=' * 30)
print('{:^30}'.format('BANCO DO DINHEIRO'))
print('=' * 30)
valor = int(input('Digite o valor que gostaria de sacar: R$ '))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced},00.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break