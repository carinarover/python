# 008 Conversor de medidas
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite a distância: '))
print('A distância é de {} metros, que é equivalente a {:.0f} centímetros ou {:.0f} milímetros.'.format(valor, (valor*100), (valor*1000)))

# outra opção
medida = float(input('Digite a distância: '))
quil = medida / 1000
hec = medida / 100
code = medida /10
deci = medida * 10
cen = medida * 100
mil = medida * 1000
print('A distância é de {} metros, que é equivalente a: \n{:.4f} quilômetros; \n{:.4f} hectômetros; \n{:.2f} decâmetros; \n{} '
      'decímetros; \n{:.0f} centímetros; \n{:.0f} milímetros.'.format(medida, quil, hec, code, deci, cen, mil))