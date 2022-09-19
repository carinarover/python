# 113 Funções aprofundadas em Python
# Reescreva a função leaiInt() que fizemos no Desafio 104., incluindo agora a possibilidade da digitação de um número de tipo inválido.
# aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, figite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')