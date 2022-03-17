print ('PROGRAMA PARA CALCULAR O TROCO')

valorcompra= int(input('Insira o valor da compra: '))
valorpagamento= int(input('Insira o valor do pagamento: '))
troco=valorpagamento-valorcompra

notade50= troco//50
print ('Nota de 50: ',notade50)
notade20= troco%50//20
print ('Nota de 20: ',notade20)
notade10= troco%50%20//10
print ('Nota de 10: ',notade10)
notade5= troco%50%20%10//5
print ('Nota de 5: ',notade5)
notade1= troco%50%20%10%5//1
print ('Nota de 1: ',notade1)