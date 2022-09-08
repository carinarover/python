# 024 Verificando as primeiras letras de um texto
# Crie um programa que lai o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite o nome da cidade que você mora: ')).strip()
print(city[0:5].upper() == 'SANTO')

# strip() remove espaços no início e final. lstrip() remove espaços left e rstrip() remove espaços right