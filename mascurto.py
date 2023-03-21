def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Celsius para Kelvin')
    print('3. Converter de Fahrenheit para Kelvin')
    print('4. Converter de Fahrenheit para Celsius')
    print('5. Converter de Kelvin para Fahrenheit')
    print('6. Converter de Kelvin para Celsius')

def converter_temperatura():
    escolha = int(input('Escolha o tipo de conversão que deseja realizar: '))

    if escolha == 1:
        celsius = float(input('Entre com a temperatura em graus Celsius: '))
        fahrenheit = (celsius * 9/5) + 32
        print(f'Valor em Fahrenheit: {fahrenheit}°F')

    elif escolha == 2:
        celsius = float(input('Entre com a temperatura em graus Celsius: '))
        kelvin = celsius + 273.15
        print(f'Valor em Kelvin: {kelvin} K')

    elif escolha == 3:
        fahrenheit = float(input('Entre com a temperatura em graus Fahrenheit: '))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f'Valor em Kelvin: {kelvin} K')

    elif escolha == 4:
        fahrenheit = float(input('Entre com a temperatura em graus Fahrenheit: '))
        celsius = (fahrenheit - 32) * 5/9
        print(f'Valor em Celsius: {celsius}°C')

    elif escolha == 5:
        kelvin = float(input('Entre com a temperatura em graus Kelvin: '))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f'Valor em Fahrenheit: {fahrenheit}°F')

    elif escolha == 6:
        kelvin = float(input('Entre com a temperatura em graus Kelvin: '))
        celsius = kelvin - 273.15
        print(f'Valor em Celsius: {celsius}°C')

if __name__=='__main__':
    menu_inicial()
    converter_temperatura()
