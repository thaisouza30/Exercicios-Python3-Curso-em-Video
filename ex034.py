salario = float(input('Digite o valor de seu salário :'))
if salario <= 1250:
    aumento = salario + (salario * 15/100)
    print('Seu salário teve 15% de aumento, passando a ser R${:.2f}'.format(aumento))
else:
    salario > 1250
    aumento = salario + (salario * 10/100)
    print('Seu salário teve 10% de aumento , passando a ser R${:.2f}'.format(aumento))


