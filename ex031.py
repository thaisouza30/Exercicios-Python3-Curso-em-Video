distancia = float(input('Escreva qual a distância da viagem em km:'))
if distancia <= 200:
    preço = distancia * 0.50
    print('Sua passagem irá custar R${:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('A sua passagem irá custar R${:.2f}'.format(preço))


