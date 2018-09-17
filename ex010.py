real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 4.06
euro = real / 4.71
print('Com R${} você pode comprar {:.2f}U$$'.format(real,dolar))
print('Com R${} você pode comprar {:.2f}EUR'.format(real,euro))



