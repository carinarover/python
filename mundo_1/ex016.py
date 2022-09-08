import emoji
print(emoji.emojize('Olá, Mundo :smiley:', language='alias'))
# https://www.webfx.com/tools/emoji-cheat-sheet/

# 016 Quebrando um número
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Exemplo: digite 6.127  e mostre a parte inteira 6.
import math
n = float(input('Digite um número Real: '))
i = math.floor(n)
print("O número {} tem a parte inteira {}.".format(n, i))

#ou
import math
n = float(input('Digite um número Real: '))
print("O número {} tem a parte inteira {}.".format(n, math.trunc(n)))

#ou
from math import trunc
n = float(input('Digite um número Real: '))
print("O número {} tem a parte inteira {}.".format(n, trunc(n)))

# ou
n = float(input('Digite um número Real: '))
print("O número {} tem a parte inteira {:.0f}.".format(n, n))

# ou
n = float(input('Digite um número Real: '))
print("O número {} tem a parte inteira {}.".format(n, int(n)))