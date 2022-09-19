# 115 Criando um menu em Python
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma noa pessoa
        cabeçalho('NOVO CADASTRO')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        nome = str(input('Nome: '))
        idade = leaiInt('Idade: ')
        cadastrar(arq, nome, idade)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida! \033[m')
    sleep(2)