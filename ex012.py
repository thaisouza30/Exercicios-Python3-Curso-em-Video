preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f} agora na promoção com desconto de 5% irá custar R${:.2f}'.format(preço,novo))


