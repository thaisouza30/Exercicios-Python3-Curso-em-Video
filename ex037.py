numero = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1]Converter para Binário
[2]Converter para Octal
[3]Converter para Hexadecimal''')
opcao = int(input('Sua opção :'))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(numero,bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numero,oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida, tente novamente.')

