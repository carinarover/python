# 014 Conversor de Temperaturas
# Escreva um programa que leia uma temperatura digitada em °C e converta para °F.
temp = int(input('Digite a temperatura em °C: '))
f = temp * 9/5 + 32
print('A temperatura de {}°C corresponde a {:.0f}°F.'.format(temp, f))