# 092 Cadastro de Trabalhador em Python
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso
# a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente além da idade,
# com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = {}
dados['nome'] = str(input('Digite o seu nome: '))
dados['ano'] = int(input('Digite o seu ano de nascimento: '))
dados['cart'] = int(input('Digite o número da sua carteira de trabalho (0 se não tem): '))
if dados['cart'] != 0:
    dados['contr'] = int(input('Digite o ano da sua contratação: '))
    dados['salario'] = float(input('Digite o seu salário: R$ '))
else:
    print('Você não trabalha ainda. O programa não se adequa a você.')

hoje = date.today().year
dados['idade'] = hoje - dados['ano']
dados['aposentar'] = dados['contr'] + 35
dados['idadeapos'] = dados['aposentar'] - dados['ano']
# print(dados)

print(f'O funcionário {dados["nome"]}, Carteira de Trabalho nº {dados["cart"]}, tem {dados["idade"]} anos e trabalha de '
      f'carteira assinada desde {dados["contr"]}. \nSeu salário é de R$ {dados["salario"]} e sua aposentadoria está prevista '
      f'para {dados["aposentar"]}, quando ele terá {dados["idadeapos"]} anos. ')