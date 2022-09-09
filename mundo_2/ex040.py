# 040 Aquele clássico da média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média é {:.1f} e você está REPROVADO.'.format(media))
elif media >= 5 and media <= 6.9: #ou 7 > media >= 5
    print('Sua média é {:.1f} e você está de RECUPERAÇÃO.'.format(media))
else: #ou elif media >= 7
    print('Sua média é {:.1f} e você está APROVADO.'.format(media))