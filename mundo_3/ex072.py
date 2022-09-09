# 072 Número por extenso
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# seu programa deverá ler pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre zero e 20: '))
    if 0 <= numero <= 20:
        break
    else:
        print('Número não corresponte. ', end='')
print(f'O número {numero} por extenso é {contagem[numero]}.')