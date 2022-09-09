# 043 Índice de Massa Corporal
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com as
# informações abaixo:
# - Abaixo de 18.5: abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - Acima de 40: obesidade mórbida

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.1f} e você está com peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.1f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade mórbida.'.format(imc))

