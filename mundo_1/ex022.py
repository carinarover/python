# 022 Analisador de Textos
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maíusculas e minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ').strip()

print('O nome {} em maiúsculo é {}.'.format(nome, nome.upper()))
print('O nome {} em minúsculo é {}.'.format(nome, nome.lower()))
print('O nome {} tem {} letras.'.format(nome, len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras.'.format(nome.find(' ')))

#ou
separar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separar[0], len(separar[0])))