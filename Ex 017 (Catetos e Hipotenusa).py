from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) **(1/2)
# print('A hipotenusa vai medir {:.2f} '.format(hi))
# hi = math.hypot(ca, co)
hi = hypot(ca,co)
print('A hipotenusa vai medir {:.2f}'.format(hi))


# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO
# CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA