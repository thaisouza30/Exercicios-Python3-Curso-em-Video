soma = totmil = menor = cont = 0
barato = ''
print('*-' * 20)
print('Lojas Super Baratão')
print('*-' * 20)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'O total da sua compra foi R${soma:.2f}')
print(f'Temos {totmil} produtos custando acima de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor :.2f}')
