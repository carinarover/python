# 026 Primeira e última ocorrência de uma string
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
print('A letra "A" aparece {} vezes na frase digitada.'.format(frase.upper().count('A')))
print('A primeira letra "A" está na posição {}.'.format(frase.upper().find('A')+1))
print('A última letra "A" está na posição {}.'.format(frase.upper().rfind('A')+1))