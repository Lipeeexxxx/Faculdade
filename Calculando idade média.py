# Calculando idade média 

print('PROGRAMA PARA CALCULAR A MEDIA DAS IDADES')

idade = int(input("Quantidade de pessoas"))
i = 0
somaI = 0
while i < idade:
    ida = int(input("Informe a idade"))
    somaI = somaI + ida #somaI +=ida
    i += 1; #i = i + 1 
mediaI = somaI / idade

print("Média das idade é: ",mediaI)
