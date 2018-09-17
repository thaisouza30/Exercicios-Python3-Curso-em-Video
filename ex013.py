salario = float(input('Qual o valor do salário? R$'))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava salário de R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,aumento))
