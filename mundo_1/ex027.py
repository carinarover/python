# 027 Primeiro e último nome de uma pessoa
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('O primeiro nome é {}.'.format(separado[0]))
print('O último nome é {}.'.format(separado[-1]))