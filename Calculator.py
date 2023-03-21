# Calculadora Conversora de Unidades: Graus Celsius, Fahrenheit e Kelvin

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Celsius para Kelvin')
    print('3. Converter de Fahrenheit para Kelvin')
    print('4. Converter de Fahrenheit para Celsius')
    print('5. Converter de Kelvin para Fahrenheit')
    print('6. Converter de Kelvin para Celsius')


def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def cel_kel():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    K = C + 273
    print('Valor em Kelvin: {0} K'.format(K))

def fahr_kel():
        F = float(input('Entre com a temperatura em graus Fahrenheit: '))
        K = (F - 32) * (5 / 9) + 273
        print('Valor em Kelvin: {0} K'.format(K))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

def  kel_fahr():
    K = float(input('Entre com a temperatura em graus Kelvin: '))
    F = (K - 273) * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def  kel_cel():
    K = float(input('Entre com a temperatura em graus Kelvin: '))
    C = K - 273
    print('Valor em Celsius: {0}°C'.format(C))
while True:

    if __name__=='__main__':
        menu_inicial()
        escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        cel_kel()

    if escolha == '3':
        fahr_kel()

    if escolha == '4':
        fahr_cel()

    if escolha == '5':
        kel_fahr()

    if escolha == '6':
        kel_cel()

    else:
        print ("erro 21216: insira um numero válido de 1 a 6")
