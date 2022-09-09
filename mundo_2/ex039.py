# 039 Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
hoje = date.today().year
idade = hoje - ano

if idade == 18:
    print('Esse ano você deve se alistar no serviço militar.')
elif idade < 18:
    saldo = 18 - idade
    print('Você deverá se alistar no serviço militar em {} anos.'.format(saldo))
else:
    saldo = idade - 18
    print('Você já passou do ano de alistamento em {} anos.'.format(saldo))