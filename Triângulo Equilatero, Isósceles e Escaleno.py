print('Descubra se o triangulo é Equilatero, Isósceles ou Escaleno:\n')

try: 
    lado1=float(input("Informe o primeiro lado: "))
    lado2=float(input("Informe o segundo lado: "))
    lado3=float(input("Informe o terceiro lado: "))

    if lado1<=0 or lado2<=0 or lado3<=0:
        print('Medidas devem ser positivas')
    elif lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado3 + lado1 <= lado2:
        print("Não é um triângulo!")
    elif lado1 == lado2 == lado3:
        print("Esse triangulo é Equilátero!")
    elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
        print("Esse triangulo é Isósceles!")
    elif lado1 != lado2 != lado3:
        print("Esse triangulo é Escaleno!")

except ValueError: 
    print('Não há possibilidade de usar texto')
    
print('\nObrigado por usar o programa')
