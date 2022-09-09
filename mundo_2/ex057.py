# 057 Validação de Dados
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o seu sexo: [F/M] ')).strip().upper()[0] #pega somente primeira letra
print('FIM')

#ou

sexo = str(input('Digite o seu sexo: [F/M] ')).strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados inválidos. Digite o seu sexo: [F/M] ')).strip().upper()[0] #pega somente primeira letra
print('FIM')

#ou
sexo = str(input('Digite o seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Digite o seu sexo: [F/M] ')).strip().upper()[0] #pega somente primeira letra
print('FIM')