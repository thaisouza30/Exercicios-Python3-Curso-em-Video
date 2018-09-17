valor_casa = float(input('Digite o valor da casa : R$'))
salario = float(input('Digite o valor do salário : R$'))
prestacoes = int(input('Digite em quantas prestações irá pagar:'))
mensal = valor_casa / prestacoes
criterio = salario - (salario * 30/100)
if mensal >= criterio:
    print('Empréstimo foi negado, prestações excederam a 30% do salário ')
else:
    print('Empréstimo aprovado, em breve entraremos em contato')
