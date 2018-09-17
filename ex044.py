preco = float(input('Digite o valor do produto:'))
vista = preco - (preco * 10 / 100)
vista_cartao = preco - (preco * 5 / 100)
duas_cartao = preco
tres_cartao = preco + (preco * 20 / 100)
print('=*='*20)
print('''[1]- Dinheiro / Cheque á vista
[2]- Á vista no cartão 
[3]- Em 2 vezes no cartão sem juros
[4]- Em 3 vezes ou mais com juros''')
print('=*='*20)
opcao = int(input('Digite o número correspondente para forma de pagamento:'))
if opcao == 1:
    print('O valor total do produto será R${:.2f}'.format(vista))
elif opcao == 2:
    print('O valor total do produto será R${:.2f}'.format(vista_cartao))
elif opcao == 3:
    parcela = preco / 2
    print('O valor total do produto será R${:.2f} em duas parcelas de R${:.2f} sem juros'.format(duas_cartao, parcela))
elif opcao == 4:
    totparcela = int(input('Quantas parcelas? '))
    parcela = tres_cartao / totparcela
    print('O valor total do produto será R${:.2f} em {} parcelas de R${:.2f} com juros'.format(tres_cartao, totparcela, parcela))
else:
    opcao = 0
    print('Opção inválida, tente novamente.')



