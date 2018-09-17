km = float(input('Quantos Km foram percorridos?'))
dia = int(input('Qual a quantidade de dias que foi alugado?'))
totdia = dia * 60
totkm = km * 0.15
total = totdia + totkm
print('O valor a pagar de km R${} e valor de diária R${} , sendo o total a pagar de R${}'.format(totkm,totdia,total))
