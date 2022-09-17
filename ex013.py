sálario = float(input('Qual é o sálario do funcionário? R$'))
novo = sálario + (sálario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sálario, novo))



