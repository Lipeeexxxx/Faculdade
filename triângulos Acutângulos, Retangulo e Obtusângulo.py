print ('Diferenciando os triângulos Acutângulos, Retangulo e Obtusângulo\n')

try:
    angulo1 = float(input('Digite o primeiro angulo:'))
    angulo2 = float(input('Digite o segundo angulo:'))
    angulo3 = float(input('Digite o terceiro angulo:'))

    if angulo1<=0 or angulo2<=0 or angulo3<=0 or angulo1 + angulo2 + angulo3 != 180:
        print('Os angulos devem ser positivos ou iguais a 180')
    elif angulo1<= 90 and angulo2<=90 and angulo3<=90:
        print('Esse triangulo é Acutângulo')
    elif angulo1==90 or angulo2==90 or angulo3==90:
        print('Esse triangulo é Retângulo')
    else :
        print('Esse triangulo é Obtusângulo')
except ValueError:
    print('Não há possibilidade de usar texto')

print('\nOBRIGADO POR USAR ESSE PROGRAMA')