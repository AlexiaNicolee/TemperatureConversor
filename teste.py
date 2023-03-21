while True:
    try:
        numero= float, int,(input("digite um numero inteiro"))

        break
    except ValueError:
        print("erro 52: Numero ivalido. por favor, tente novamente")
    print("fim do prpgrama")