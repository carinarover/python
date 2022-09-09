# 101 Funções para votação
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
# um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.

def voto():
    print('-' * 30)
    from datetime import date #economiza memória importar aqui dentro
    ano = float(input('Em que ano você nasceu? '))
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        print(f'Vocé possui {idade} anos e NÃO VOTA.')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Vocé possui {idade} e o VOTO É OPCIONAL')
    else:
        print(f'Você possui {idade} anos e o VOTO É OBRIGATÓRIO.')

voto()

# ou
def voto(ano):
    print('-' * 30)
    from datetime import date #economiza memória importar aqui dentro
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        return f'Vocé possui {idade} anos e NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Vocé possui {idade} e o VOTO É OPCIONAL'
    else:
        return f'Você possui {idade} anos e o VOTO É OBRIGATÓRIO.'

nasc = float(input('Em que ano você nasceu? '))
print(voto(nasc))