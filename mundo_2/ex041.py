# 041 Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de
# acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SENIOR
# Acima: MASTER

from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))
hoje = date.today().year
idade = hoje - ano

if idade <= 9:
    print('O atleta possui {} anos e está na categoria MIRIM.'.format(idade))
elif 14 >= idade > 9: #ou idade <= 14 porque já passou pelo 9
    print('O atleta possui {} anos e está na categoria INFANTIL.'.format(idade))
elif 19 >= idade > 14: #ou idade <= 19 porque já passou pelo 14
    print('O atleta possui {} anos e está na categoria JUNIOR.'.format(idade))
elif 25 >= idade > 19: #ou idade <= 25 porque já passou pelo 19
    print('O atleta possui {} anos e está na categoria SENIOR.'.format(idade))
else:
    print('O atleta possui {} anos e está na categoria MASTER.'.format(idade))