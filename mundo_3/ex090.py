# 090 Dicionário em Python
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da
# estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Digite a média do aluno: '))
if aluno['média'] < 5:
    aluno['final'] = 'Reprovado'
elif 5 <= aluno['média'] < 7:
    aluno['final'] = 'Recuperação'
else:
    aluno['final'] = 'Aprovado'
print(f'O aluno {aluno["nome"]} tem média {aluno["média"]} e por isso está {aluno["final"]}.')
