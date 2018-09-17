num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('A unidade {}'.format(u))
print('A dezena {}'.format(d))
print('A centena {}'.format(c))
print('A milhar {}'.format(m))
