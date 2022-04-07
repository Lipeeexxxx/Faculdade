larg= float(input('Qual a largura da parede? '))
alt= float(input('Qual a altura da parede? '))
area= larg*alt
tinta= area/2

print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e a sua área é de {:.2f}m² '.format(larg,alt,area))
print('Para pintar uma parede de {}m², você precisará de {} Litros de tinta! '.format(area,tinta))



# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DA PAREDE EM METROS 
# CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LÁ, SABENDO QUE CADA LITRO  DE TINTA, PINTA UMA AREA DE 2m²
